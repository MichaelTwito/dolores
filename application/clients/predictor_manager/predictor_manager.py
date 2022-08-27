from predictions_pb2 import IrisSpeciesPredictionRequest, CreateAndTrainModelRequest
from predictions_pb2_grpc import PredictionsStub
from ..grpc_client import GrpcClient

class PredictorManager(GrpcClient):
    def __init__(self, address):
        super().__init__(address)
        self.channel = super().get_channel()
    
    def predict_iris_speices(self, SepalLengthCm, SepalWidthCm,PetalLengthCm, PetalWidthCm, PathToModel):
        stub = PredictionsStub(self.channel)
        response = super().stub(lambda x: stub.IrisSpeciesPredict(x),IrisSpeciesPredictionRequest\
                    (SepalLengthCm =SepalLengthCm, SepalWidthCm = SepalWidthCm,\
                     PetalLengthCm = PetalLengthCm, PetalWidthCm = PetalWidthCm, PathToModel=PathToModel))
        return response

    def create_and_train_model(self, dataset_path ,epochs ,optimizer_params,\
                                        criterion ,model_params ,save_model_at):     
        stub = PredictionsStub(self.channel)
        response = super().stub(lambda x: stub.CreateAndTrainModel(x)\
        ,CreateAndTrainModelRequest(dataset_path=dataset_path ,epochs=epochs ,optimizer_params=optimizer_params,\
        criterion=criterion ,model_params=model_params ,save_model_at=save_model_at))
        return response
