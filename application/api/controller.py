from flask import request, jsonify
from ..utils.error_handler import error_handler
from application.services import user_service, api_key_service, predictor_manager_service

@error_handler
def create_user(name: str, email: str, password: str): return jsonify(user_service.create_user(name, email, password)), 200

@error_handler
def get_user(username: str): return jsonify(user_service.get_user(username))

@error_handler
def list_users(): return jsonify(user_service.list_users())     

@error_handler
def create_and_train_model(dataset_params: dict , train_params: dict , test_params: dict,\
                         optimizer_params: dict, criterion: str,\
                         model_params: dict, save_model_at: str):
    trained_model_results = predictor_manager_service.create_and_train_model(\
                    dataset_params, train_params , test_params ,optimizer_params,criterion ,model_params ,save_model_at)
    return jsonify({"accuracy": str(trained_model_results.accuracy),\
                    "saved_model_path": str(trained_model_results.saved_model_path)}), 200

@error_handler
def predict_iris_species(SepalLengthCm: float ,SepalWidthCm: float,\
                         PetalLengthCm: float, PetalWidthCm: float, PathToModel: str):
    return jsonify({"properties": request.json ,\
                   "species": predictor_manager_service.predict_iris_speices(\
                    SepalLengthCm, SepalWidthCm,PetalLengthCm, PetalWidthCm, PathToModel)}), 200

@error_handler
def create_api_key(username: str, password: str, api_key_name: str):
    return api_key_service.create_api_key(api_key_name), 200
