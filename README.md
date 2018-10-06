!(diagram)[diagram.png]

# pycones18-grpc-vs-httpjson
PyConES2018 - Comparing gRPC+Protobuf vs JSON+HTTP in Python

## gRPC+Protobuf or JSON+HTTP?
This repository contains 5 equal APIs: gRPC using Protobuf and JSON over HTTP. The goal is to run benchmarks for all approaches and compare them. The backend is powered by 5 microservices, 4 of which happen to be written in Python and the grpc-gateway proxy is written in Go.

### Services organization

The application consists of the following application services:

| Service      | Port  | Description                                        | Language service |
|--------------|-------|----------------------------------------------------|------------------|
| django       | 8000  | Provides a django webapp                           | Python           |
| flask        | 8001  | Provides a flask webapp                            | Python           |
| grpc         | 50051 | Provides a grpc webapp                             | Python           |
| grpc-gateway | 8002  | Provides a grpc proxy                              | Golang           |
| grpc-rest    | 8003  | Provides a flask webapp where request is called    | Python           |
|              |       | to grpc webapp using stub of grpc service          |                  |
 - ---------------------------------------------------------------------------------------------- 

### Requirements

 - Install [Docker](https://www.docker.com/get-docker)
 - Install [Docker Compose](https://docs.docker.com/compose/install)

### Run

```
docker-compose build
docker-compose up
```

### Test http json services

#### django service
```
$ curl -i http://localhost:8000/v0/api/
```
#### flask service
```
$ curl -i http://localhost:8001/v0/api
```
#### grpc gateway service
```
$ curl -i http://localhost:8002/v0/api
```
#### grpc rest service
```
$ curl -i http://localhost:8003/v0/api
```
