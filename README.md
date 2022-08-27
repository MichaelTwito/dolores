run: 
flask db init
flask db migrate 
flask db upgrade

python -m grpc_tools.protoc -I ../protobufs --python_out=. \
         --grpc_python_out=. ../protobufs/predictions.proto