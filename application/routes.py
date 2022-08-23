from webargs import fields
from sqlalchemy import exc
from flask import current_app
from flask import Flask, request,jsonify
from webargs.flaskparser import use_kwargs
from .services import auth_service,user_service, api_key_service
from .services.auth_service import api_required, super_admin_required

app = current_app._get_current_object()

@app.route('/')
def index():
   return "hello world"

@app.route("/api/users/<username>", methods=["GET"])
@api_required
def get_users(username):
    try:
        result = user_service.get_user(username) if username != "*" else user_service.list_users()
        return jsonify(result)
    except Exception as e:
        return '', 500

@app.route("/api/users", methods=["POST"])
@use_kwargs({"name": fields.Str(required=True), "email": fields.Str(required=True), "password": fields.Str(required=True)})
def create_user(name: str, email: str, password: str):
    try:
        user_service.create_user(
           name, email, password
       )
        return "", 204
    except exc.IntegrityError as e:
        return jsonify({"message": str(e.orig)}), 500

@app.route("/api/api_keys", methods = ['POST'])
@use_kwargs({"username": fields.Str(required=True),"password": fields.Str(required=True),  "api_key_name": fields.Str(required=True)})
@super_admin_required
def create_api_key(username: str, password: str, api_key_name: str):
  try:
     return api_key_service.create_api_key(
         api_key_name
     ), 200
  except exc.IntegrityError as e:
      return jsonify({"message": str(e.orig)}), 500
