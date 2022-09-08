
### Development
## PROTOBUFS
After updating protobufs protocol, run:
```
python -m grpc_tools.protoc -I ../protobufs --python_out=. \
         --grpc_python_out=. ../protobufs/predictions.proto
```

## Migrations
For running migrations use:
```
flask db init
flask db migrate 
flask db upgrade
```

### USAGE
## Create User Request
```curl
curl --location --request POST 'http://localhost:5000/api/users/' \
--header 'Content-Type: application/json' \
--data-raw '{
    "name": "michael123",
    "email": "michael@twito.net",
    "password": "123456"
}'
```



