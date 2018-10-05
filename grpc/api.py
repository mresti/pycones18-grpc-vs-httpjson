from concurrent import futures
import sys
import logging
import time

import grpc

# import the generated classes
import api_pb2_grpc
import api_pb2

log = logging.getLogger()
log.setLevel(logging.DEBUG)

ch = logging.StreamHandler(sys.stdout)
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
log.addHandler(ch)

_ONE_DAY_IN_SECONDS = 60 * 60 * 24

# create a class to define the server functions, derived from
# api_pb2_grpc.APIServicer
class API(api_pb2_grpc.APIServicer):

    def SayHello(self, request, context):
        log.info("[SayHello request] %s" % request)
        response = api_pb2.ServiceResponse()
        response.event = "PyConES 2018"
        response.detail = "API in grpc"
        response.requirements = "grpcio==1.15.0"
        log.info("[SayHello responses] %s" % response)
        return response

# create a gRPC server
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    api_pb2_grpc.add_APIServicer_to_server(API(), server)
    # listen on port 50051
    log.info('Starting server. Listening on port 50051  .')
    server.add_insecure_port('[::]:50051')
    server.start()
    log.info("server started")
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt as e:
        log.warning('Caught exception "%s"; stopping server...', e)
        server.stop(0)
        log.warning('Server stopped; exiting.')

if __name__ == '__main__':
    serve()
