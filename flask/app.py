from flask import Flask
from flask import jsonify

app = Flask(__name__)

@app.route('/v0/api', methods = ['GET'])
def api_hello():
    data = {
        'event'  : 'PyConES 2018',
        'detail' : 'API in flask',
        'requirements': 'flask==1.0.2'
    }

    resp = jsonify(data)
    resp.status_code = 200

    return resp
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
