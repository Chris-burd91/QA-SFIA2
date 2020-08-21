from flask import Flask, jsonify, Response, request
import requests
from application import app

@app.route('/generate', methods=['GET','POST'])
def generate():
    response = requests.get('http://34.89.20.169:5001/key')
    #int
    json_response = response.json()
    number = json_response["Key"]
    post = requests.post('http://34.89.20.169:5002/anwser', json= json_response)
    response2 =requests.get('http://34.89.20.169:5002/anwser')
    #list
    json_response2 = response2.json()
    anwser = json_response2["Value"]
    
    return jsonify(anwser)