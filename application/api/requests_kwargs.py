from webargs import fields

create_user = {"name": fields.Str(required=True),\
            "email": fields.Str(required=True),\
            "password": fields.Str(required=True)}

get_user = {"username": fields.Str(required=True)}

create_and_train_model = {"dataset_params": fields.Dict(required=True),\
                          "train_params": fields.Dict(required=True),\
                          "test_params": fields.Dict(required=True),\
                          "optimizer_params": fields.Dict(required=True),\
                          "criterion": fields.String(required=True),\
                          "model_params": fields.Dict(requires=True),\
                          "save_model_at": fields.String(required=False)}

predict_iris_species = {"SepalLengthCm": fields.Float(required=True),\
                        "SepalWidthCm": fields.Float(required=True),\
                        "PetalLengthCm": fields.Float(required=True),\
                        "PetalWidthCm": fields.Float(required=True),\
                        "PathToModel": fields.String(required=True)}

create_api_key = {"username": fields.Str(required=True),\
                  "password": fields.Str(required=True),\
                  "api_key_name": fields.Str(required=True)}