from flask import Flask
from flask import jsonify

import client_grpc

app = Flask(__name__)

@app.route('/v0/api', methods = ['GET'])
def api_hello():
    response = client_grpc.call_grpc_server() 
    data = {
        'event'  : response.event,
        'detail' : '%s + flask' % response.detail,
        'requirements': '%s,flask==1.0.2' % response.requirements
    }

    resp = jsonify(data)
    resp.status_code = 200

    return resp
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
