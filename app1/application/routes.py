from flask import Flask, jsonify, render_template, url_for
import requests
from application import app

@app.route('/')
@app.route('/home', methods=['GET'])
def home():
    return render_template('home.html', title='Home')

@app.route('/8ball', methods=['GET','POST'])
def _8ball():
    number = requests.get('http://app2:5001/number')
    json_number = number.json()
    answers = requests.get('http://app3:5002/answer')
    json_answers = answers.json()
    answer = requests.post('http://app4:5003/generate', json= {"key":json_number,"value":json_answers} )
    json_answer = answer.json()
    display = str(json_answer)

    

    return render_template('8ball.html', title='8 Ball Prediction!', view=display)