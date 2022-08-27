
from flask import Blueprint
from . import controller, requests_kwargs
from webargs.flaskparser import use_kwargs
from ..services.auth_service import api_required, super_admin_required

router = Blueprint('router', __name__)

@router.route("/api/users/", methods=["POST"])
@use_kwargs(requests_kwargs.create_user)
def create_user(name,email,password): return controller.create_user(name, email, password)

@router.route("/api/users/*", methods=["GET"])
@api_required
def list_users(): return controller.list_users()

@router.route("/api/users/", methods=["GET"])
@use_kwargs(requests_kwargs.get_user, location="query")
@api_required
def get_user(username): return controller.get_user(username)

@router.route('/api/model/train', methods=["Post"])
@use_kwargs(requests_kwargs.create_and_train_model)
@api_required
def create_and_train_model(*args, **kwargs): return controller.create_and_train_model(*args, **kwargs)

@router.route('/api/predictions/nerual_networks/predict_iris_species', methods=["Post"])
@use_kwargs(requests_kwargs.predict_iris_species)
@api_required
def predict_iris_species(*args, **kwargs): return controller.predict_iris_species(*args, **kwargs)

@router.route("/api/api_keys", methods = ['POST'])
@use_kwargs(requests_kwargs.create_api_key)
@super_admin_required
def create_api_key(*args, **kwargs): return controller.create_api_key(*args, **kwargs)
