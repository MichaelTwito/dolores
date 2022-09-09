from dolores_test import client, app

model_train_params = {
    "dataset_params": {"path": "./data_dir/Iris.csv", "train_test_split_ratio": "0.2"},
    "train_params": {"epochs": "100","batch_size": "30","num_of_workers": "0"},
    "test_params": {"batch_size": "30","num_of_workers": "0"},
    "optimizer_params": {"algorithm": "Adam", "lr": "0.01"},
    "criterion": "CrossEntropyLoss", 
    "model_params": {"name": "neural_network_model"},
    "save_model_at": "./saved_models/iris/neural_network_model"}

api_keys_params = {
    "username": "michael",
    "password": "123456",
    "api_key_name": "super_admin"
}

iris_prediction_params = {
"SepalLengthCm": 5.4,
"SepalWidthCm": 0.2,
"PetalLengthCm": 3.4,
"PetalWidthCm": 0.5,
"PathToModel": "./saved_models/iris/neural_network_model_08_09_2022_12_46_28.pth"
}

create_user_params = {
    "name": "michael",
    "email": "michael@twito.net",
    "password": "123456"
}


def test_api_key_required(client):
    """When the requset is missing the ApiKey, return an error """
    
    requests_tuple = (client.get('/api/users/*'), client.get('/api/users/?username=test'),\
                      client.post('/api/model/train', json=model_train_params),\
                      client.post('/api/predictions/nerual_networks/predict_iris_species', json=iris_prediction_params))
    assert all(map(lambda x:  b'Please provide an API key' in x.data,requests_tuple))

def test_super_admin_required(client):
    """When the requset is missing super_admin Credentials, return an error """

    response = client.post('/api/api_keys', json=api_keys_params)
    assert b'The provided credentials is not valid' in response.data 

def test_create_user(client):
    """When the params is valid, return 200 OK """
    response = client.post('/api/users/', json=create_user_params)
    assert  '200 OK' == response.status
    
    """When the params is invalid, return 422 error """
    del create_user_params['email']
    response_invalid_params = client.post('/api/users/', json= create_user_params)
    assert  '422 UNPROCESSABLE ENTITY' == response_invalid_params.status
