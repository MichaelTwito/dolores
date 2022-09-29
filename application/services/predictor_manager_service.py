from flask import current_app
from ..clients.predictor_manager.predictor_manager import PredictorManager

app = current_app._get_current_object()
grpc_predictor_manager_node = app.config['GRPC_PREDICTOR_MANAGER_NODE']
predictor = PredictorManager(grpc_predictor_manager_node)

def create_and_train_model(*args):
    return predictor.create_and_train_model(*args)

def predict_iris_speices(*args):
    return predictor.predict_iris_speices(*args).species

def predict_brain_tumor_type(*args):
    return predictor.predict_brain_tumor_type(*args).type