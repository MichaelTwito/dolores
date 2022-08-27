from email import message
import grpc
import functools
from predictions_pb2 import *
class GrpcClient:
    def __init__(self, address):
        self.channel = grpc.insecure_channel(address)

    def get_channel(self):
        return self.channel
        
    def stub(self, func, *args):
        try:
            return func(*args) 
        except grpc.RpcError as rpc_error:
            if rpc_error.code() == grpc.StatusCode.CANCELLED:
                raise RuntimeError('Cancelled')
            elif rpc_error.code() == grpc.StatusCode.UNAVAILABLE:
               raise RuntimeError('Unavailable Grpc node')
            else:
               raise RuntimeError(f"Received unknown RPC error: code={rpc_error.code()} message={rpc_error.details()}")