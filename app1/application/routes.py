from flask import Flask, jsonify, render_template, url_for
import requests
from application import app


@app.route('/', methods=['GET'])
def home():
    return render_template('home.html', title='Home')

@app.route('/8ball', methods=['GET','POST'])
def _8ball():
    response = requests.get('http://app4:5004/__')
    json_response = response.json()
    display = str(json_response)
    
    
    
    return render_template('8ball.html', title='8 Ball Prediction!', view=display)