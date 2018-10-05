from __future__ import print_function

import grpc

# import the generated classes
import api_pb2_grpc
import api_pb2

# call a gRPC server
def call_grpc_server():
	with grpc.insecure_channel('grpcapi:50051') as channel:
		stub = api_pb2_grpc.APIStub(channel)
		response = stub.SayHello(api_pb2.ServiceRequest())
	print("API client received: ")
	print("%s" % response)
	return response
