### Migrations
For running migrations use:
'''
flask db init
flask db migrate 
flask db upgrade
'''
### PROTOBUFS
After updating protobufs protocol, run:
'''
python -m grpc_tools.protoc -I ../protobufs --python_out=. \
         --grpc_python_out=. ../protobufs/predictions.proto
'''