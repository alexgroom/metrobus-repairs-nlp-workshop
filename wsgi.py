import json
from flask import Flask, jsonify, request
from prediction import predict

application = Flask(__name__)

@application.route('/')
@application.route('/status')
def status():
    return jsonify({'status': 'ok'})


@application.route('/prediction', methods=['POST'])
def create_prediction():
    data = request.data or '{}'
    body = json.loads(data)
    return jsonify(predict(body))


@application.route('/getprediction', methods=['GET'])
def create_getprediction():
    dataarg = request.args.get('data') or '{}'
    data = '{ "data" : "' + dataarg + '"}'
    body = json.loads(data)
    return jsonify(predict(body))
