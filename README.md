
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
First create a SuperAdmin username according to configurations:

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
Now with SuperAdmin you can generate ApiKeys:

## Create ApiKey 
```curl
curl --location --request POST 'http://localhost:5000/api/api_keys' \
--header 'Content-Type: application/json' \
--data-raw '{
    "username": "michael123",
    "password": "123456",
    "api_key_name": "test"
}'
```

## Get User(ApiKey Required)
```curl
curl --location --request GET 'http://localhost:5000/api/users/?username=michael123' \
--header 'Content-Type: application/json' \
--header 'x-api-key: fb85a117-b8d6-41f1-9dc9-916d50122444' \
--data-raw ''
```

## List All Users(ApiKey Required)
```curl
curl --location --request GET 'http://localhost5000/api/users/*' \
--header 'Content-Type: application/json' \
--header 'x-api-key: fb85a117-b8d6-41f1-9dc9-916d50122444' \
--data-raw ''
```




