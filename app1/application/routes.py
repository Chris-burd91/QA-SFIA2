from flask import Flask, jsonify, render_template, url_for
import requests
from application import app

@app.route('/')
@app.route('/home', methods=['GET'])
def home():
    return render_template('home.html', title='Home')

@app.route('/8ball', methods=['GET','POST'])
def _8ball():
    response = requests.get('http://34.89.20.169:5003/generate')
    json_response = response.json()
    display = str(json_response)
    return render_template('8ball.html', title='8 Ball Prediction!', view=display)