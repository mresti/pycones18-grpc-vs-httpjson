from concurrent.futures import ThreadPoolExecutor, wait, as_completed

import grpc
import sys

# import the generated classes
import api_pb2_grpc
import api_pb2

message = api_pb2.ServiceRequest()

def make_grpc_request(channel):
    stub = api_pb2_grpc.APIStub(channel)
    response = stub.SayHello(message)
    print("Message replied")
    #print(response)
    return response

# create a gRPC server
def request():
    
    with grpc.insecure_channel('localhost:50051') as channel:          
        pool = ThreadPoolExecutor(10)
        #future = pool.submit(make_grpc_request, (channel))
        # print(future.result())  
        futures = []
        for x in range(int(sys.argv[1])):
            futures.append(pool.submit(make_grpc_request, (channel)))
 
        for x in as_completed(futures):
            print(x.result())

if __name__ == '__main__':
    request()
