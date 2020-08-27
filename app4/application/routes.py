from flask import Flask, jsonify, Response, request
import requests
from application import app

@app.route('/generate', methods=['GET','POST'])
def outcome():
   
   dictionary = request.get_json()
   number = dictionary['key']
   answers = dictionary['value']
   
   
   return jsonify(answers[str(number)])  