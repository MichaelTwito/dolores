# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: predictions.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x11predictions.proto\"\x8d\x01\n\x1cIrisSpeciesPredictionRequest\x12\x15\n\rSepalLengthCm\x18\x01 \x01(\x02\x12\x14\n\x0cSepalWidthCm\x18\x02 \x01(\x02\x12\x15\n\rPetalLengthCm\x18\x03 \x01(\x02\x12\x14\n\x0cPetalWidthCm\x18\x04 \x01(\x02\x12\x13\n\x0bPathToModel\x18\x05 \x01(\t\"0\n\x1dIrisSpeciesPredictionResponse\x12\x0f\n\x07species\x18\x01 \x01(\t\"\xad\x05\n\x1a\x43reateAndTrainModelRequest\x12\x46\n\x0e\x64\x61taset_params\x18\x01 \x03(\x0b\x32..CreateAndTrainModelRequest.DatasetParamsEntry\x12\x42\n\x0ctrain_params\x18\x02 \x03(\x0b\x32,.CreateAndTrainModelRequest.TrainParamsEntry\x12@\n\x0btest_params\x18\x03 \x03(\x0b\x32+.CreateAndTrainModelRequest.TestParamsEntry\x12J\n\x10optimizer_params\x18\x04 \x03(\x0b\x32\x30.CreateAndTrainModelRequest.OptimizerParamsEntry\x12\x11\n\tcriterion\x18\x05 \x01(\t\x12\x42\n\x0cmodel_params\x18\x06 \x03(\x0b\x32,.CreateAndTrainModelRequest.ModelParamsEntry\x12\x15\n\rsave_model_at\x18\x07 \x01(\t\x1a\x34\n\x12\x44\x61tasetParamsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1a\x32\n\x10TrainParamsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1a\x31\n\x0fTestParamsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1a\x36\n\x14OptimizerParamsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1a\x32\n\x10ModelParamsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"I\n\x1b\x43reateAndTrainModelResponse\x12\x10\n\x08\x61\x63\x63uracy\x18\x01 \x01(\x02\x12\x18\n\x10saved_model_path\x18\x02 \x01(\t2\xb4\x01\n\x0bPredictions\x12S\n\x12IrisSpeciesPredict\x12\x1d.IrisSpeciesPredictionRequest\x1a\x1e.IrisSpeciesPredictionResponse\x12P\n\x13\x43reateAndTrainModel\x12\x1b.CreateAndTrainModelRequest\x1a\x1c.CreateAndTrainModelResponseb\x06proto3')



_IRISSPECIESPREDICTIONREQUEST = DESCRIPTOR.message_types_by_name['IrisSpeciesPredictionRequest']
_IRISSPECIESPREDICTIONRESPONSE = DESCRIPTOR.message_types_by_name['IrisSpeciesPredictionResponse']
_CREATEANDTRAINMODELREQUEST = DESCRIPTOR.message_types_by_name['CreateAndTrainModelRequest']
_CREATEANDTRAINMODELREQUEST_DATASETPARAMSENTRY = _CREATEANDTRAINMODELREQUEST.nested_types_by_name['DatasetParamsEntry']
_CREATEANDTRAINMODELREQUEST_TRAINPARAMSENTRY = _CREATEANDTRAINMODELREQUEST.nested_types_by_name['TrainParamsEntry']
_CREATEANDTRAINMODELREQUEST_TESTPARAMSENTRY = _CREATEANDTRAINMODELREQUEST.nested_types_by_name['TestParamsEntry']
_CREATEANDTRAINMODELREQUEST_OPTIMIZERPARAMSENTRY = _CREATEANDTRAINMODELREQUEST.nested_types_by_name['OptimizerParamsEntry']
_CREATEANDTRAINMODELREQUEST_MODELPARAMSENTRY = _CREATEANDTRAINMODELREQUEST.nested_types_by_name['ModelParamsEntry']
_CREATEANDTRAINMODELRESPONSE = DESCRIPTOR.message_types_by_name['CreateAndTrainModelResponse']
IrisSpeciesPredictionRequest = _reflection.GeneratedProtocolMessageType('IrisSpeciesPredictionRequest', (_message.Message,), {
  'DESCRIPTOR' : _IRISSPECIESPREDICTIONREQUEST,
  '__module__' : 'predictions_pb2'
  # @@protoc_insertion_point(class_scope:IrisSpeciesPredictionRequest)
  })
_sym_db.RegisterMessage(IrisSpeciesPredictionRequest)

IrisSpeciesPredictionResponse = _reflection.GeneratedProtocolMessageType('IrisSpeciesPredictionResponse', (_message.Message,), {
  'DESCRIPTOR' : _IRISSPECIESPREDICTIONRESPONSE,
  '__module__' : 'predictions_pb2'
  # @@protoc_insertion_point(class_scope:IrisSpeciesPredictionResponse)
  })
_sym_db.RegisterMessage(IrisSpeciesPredictionResponse)

CreateAndTrainModelRequest = _reflection.GeneratedProtocolMessageType('CreateAndTrainModelRequest', (_message.Message,), {

  'DatasetParamsEntry' : _reflection.GeneratedProtocolMessageType('DatasetParamsEntry', (_message.Message,), {
    'DESCRIPTOR' : _CREATEANDTRAINMODELREQUEST_DATASETPARAMSENTRY,
    '__module__' : 'predictions_pb2'
    # @@protoc_insertion_point(class_scope:CreateAndTrainModelRequest.DatasetParamsEntry)
    })
  ,

  'TrainParamsEntry' : _reflection.GeneratedProtocolMessageType('TrainParamsEntry', (_message.Message,), {
    'DESCRIPTOR' : _CREATEANDTRAINMODELREQUEST_TRAINPARAMSENTRY,
    '__module__' : 'predictions_pb2'
    # @@protoc_insertion_point(class_scope:CreateAndTrainModelRequest.TrainParamsEntry)
    })
  ,

  'TestParamsEntry' : _reflection.GeneratedProtocolMessageType('TestParamsEntry', (_message.Message,), {
    'DESCRIPTOR' : _CREATEANDTRAINMODELREQUEST_TESTPARAMSENTRY,
    '__module__' : 'predictions_pb2'
    # @@protoc_insertion_point(class_scope:CreateAndTrainModelRequest.TestParamsEntry)
    })
  ,

  'OptimizerParamsEntry' : _reflection.GeneratedProtocolMessageType('OptimizerParamsEntry', (_message.Message,), {
    'DESCRIPTOR' : _CREATEANDTRAINMODELREQUEST_OPTIMIZERPARAMSENTRY,
    '__module__' : 'predictions_pb2'
    # @@protoc_insertion_point(class_scope:CreateAndTrainModelRequest.OptimizerParamsEntry)
    })
  ,

  'ModelParamsEntry' : _reflection.GeneratedProtocolMessageType('ModelParamsEntry', (_message.Message,), {
    'DESCRIPTOR' : _CREATEANDTRAINMODELREQUEST_MODELPARAMSENTRY,
    '__module__' : 'predictions_pb2'
    # @@protoc_insertion_point(class_scope:CreateAndTrainModelRequest.ModelParamsEntry)
    })
  ,
  'DESCRIPTOR' : _CREATEANDTRAINMODELREQUEST,
  '__module__' : 'predictions_pb2'
  # @@protoc_insertion_point(class_scope:CreateAndTrainModelRequest)
  })
_sym_db.RegisterMessage(CreateAndTrainModelRequest)
_sym_db.RegisterMessage(CreateAndTrainModelRequest.DatasetParamsEntry)
_sym_db.RegisterMessage(CreateAndTrainModelRequest.TrainParamsEntry)
_sym_db.RegisterMessage(CreateAndTrainModelRequest.TestParamsEntry)
_sym_db.RegisterMessage(CreateAndTrainModelRequest.OptimizerParamsEntry)
_sym_db.RegisterMessage(CreateAndTrainModelRequest.ModelParamsEntry)

CreateAndTrainModelResponse = _reflection.GeneratedProtocolMessageType('CreateAndTrainModelResponse', (_message.Message,), {
  'DESCRIPTOR' : _CREATEANDTRAINMODELRESPONSE,
  '__module__' : 'predictions_pb2'
  # @@protoc_insertion_point(class_scope:CreateAndTrainModelResponse)
  })
_sym_db.RegisterMessage(CreateAndTrainModelResponse)

_PREDICTIONS = DESCRIPTOR.services_by_name['Predictions']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _CREATEANDTRAINMODELREQUEST_DATASETPARAMSENTRY._options = None
  _CREATEANDTRAINMODELREQUEST_DATASETPARAMSENTRY._serialized_options = b'8\001'
  _CREATEANDTRAINMODELREQUEST_TRAINPARAMSENTRY._options = None
  _CREATEANDTRAINMODELREQUEST_TRAINPARAMSENTRY._serialized_options = b'8\001'
  _CREATEANDTRAINMODELREQUEST_TESTPARAMSENTRY._options = None
  _CREATEANDTRAINMODELREQUEST_TESTPARAMSENTRY._serialized_options = b'8\001'
  _CREATEANDTRAINMODELREQUEST_OPTIMIZERPARAMSENTRY._options = None
  _CREATEANDTRAINMODELREQUEST_OPTIMIZERPARAMSENTRY._serialized_options = b'8\001'
  _CREATEANDTRAINMODELREQUEST_MODELPARAMSENTRY._options = None
  _CREATEANDTRAINMODELREQUEST_MODELPARAMSENTRY._serialized_options = b'8\001'
  _IRISSPECIESPREDICTIONREQUEST._serialized_start=22
  _IRISSPECIESPREDICTIONREQUEST._serialized_end=163
  _IRISSPECIESPREDICTIONRESPONSE._serialized_start=165
  _IRISSPECIESPREDICTIONRESPONSE._serialized_end=213
  _CREATEANDTRAINMODELREQUEST._serialized_start=216
  _CREATEANDTRAINMODELREQUEST._serialized_end=901
  _CREATEANDTRAINMODELREQUEST_DATASETPARAMSENTRY._serialized_start=638
  _CREATEANDTRAINMODELREQUEST_DATASETPARAMSENTRY._serialized_end=690
  _CREATEANDTRAINMODELREQUEST_TRAINPARAMSENTRY._serialized_start=692
  _CREATEANDTRAINMODELREQUEST_TRAINPARAMSENTRY._serialized_end=742
  _CREATEANDTRAINMODELREQUEST_TESTPARAMSENTRY._serialized_start=744
  _CREATEANDTRAINMODELREQUEST_TESTPARAMSENTRY._serialized_end=793
  _CREATEANDTRAINMODELREQUEST_OPTIMIZERPARAMSENTRY._serialized_start=795
  _CREATEANDTRAINMODELREQUEST_OPTIMIZERPARAMSENTRY._serialized_end=849
  _CREATEANDTRAINMODELREQUEST_MODELPARAMSENTRY._serialized_start=851
  _CREATEANDTRAINMODELREQUEST_MODELPARAMSENTRY._serialized_end=901
  _CREATEANDTRAINMODELRESPONSE._serialized_start=903
  _CREATEANDTRAINMODELRESPONSE._serialized_end=976
  _PREDICTIONS._serialized_start=979
  _PREDICTIONS._serialized_end=1159
# @@protoc_insertion_point(module_scope)
