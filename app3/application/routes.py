from flask import Flask, jsonify, Response, request
import requests
from application import app


@app.route('/answer', methods=['GET'])
def answer():
    #answers = { '1' : "As I see it, Yes.", '2' : "It is certain." , '3' : "It is decidedly so.", '4' : "Most likely.", '5' : "Outlook good.", '6' : "Signs point to yes.", '7' : "Without a doubt.", '8' : "Yes.", '9' : "Yes – definitely.", '10' : "You may rely on it.", '11' : "Ask again later.", '12' : "Better not tell you now.", '13' : "Cannot predict now.", '14' : "Concentrate and ask again.", '15' : "Don’t count on it.", '16' : "My reply is no.", '17' : "My sources say no.", '18' : "Outlook not so good.", '19' : "Reply hazy, try again.", '20' : "Very doubtful."}
    answers = { "A" : "Well, Duh", "B" : "Yes, If you leave me alone..", "C" : "You wish", "D" : "So now you need my help...?", "E" : "You call that a question?...", "F" : "Trump uses me when he decides to go to war", "G" : "Pluto says no and that he's still a Planet", "H" : "Ask me when I care..", "I": "Get a life you Animal!", "I" : "You shouldn't use me to make your life decisions.."}
    return jsonify(answers)

