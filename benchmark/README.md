# How to run the benchmark

1. First create an empty virtualenv:  
```
virtualenv -p python3 .venv
```

2. Install requirements:  
```
pip install -r requirements.txt
```

3. Run benchmarks using `bash`'s **time** function:

```
Examples:

- Run 1k concurrent calls to django:  

time (for i in {1..1000}; do curl -i http://localhost:8000/v0/api/ &; done; wait)


- Run 1k concurrent calls to python grpc client:

time (python client.py 1000)

```

4. Short-sighted results:

- Average time for 1k concurrent HTTP Calls to django: **8.29 seconds**

- Average time for 1k concurrent HTTP Calls to flask: **8.10 seconds** 

- Average time for 1k concurrent HTTP Calls to grpc gateway: **8.35 seconds**

- Average time for 1k concurrent HTTP2 Calls to grpc api directly: **0.55 seconds**
