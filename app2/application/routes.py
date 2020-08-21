from flask import Flask, jsonify, Response, request
import requests
from application import app

import random

@app.route('/key', methods=['GET'])
def key():
    numbers = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    #order = ["A", "B", "C", "D", "E", "F", "G", "H", "I"]
    number = numbers[random.randrange(20)]
    #order = order[random.randrange(8)]
    return jsonify({"Key": number})
    #return jsonify({"Key": order})