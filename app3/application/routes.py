from flask import Flask, jsonify, Response, request
import requests
from application import app


@app.route('/anwser', methods=['GET'])
def anwser():
    anwsers = ["As I see it, yes.", "It is certain." , "It is decidedly so.", "Most likely.", "Outlook good.", "Signs point to yes.", "Without a doubt.", "Yes.", "Yes – definitely.", "You may rely on it.", "Ask again later.", "Better not tell you now.", "Cannot predict now.", "Concentrate and ask again.", "Don’t count on it.", "My reply is no.", "My sources say no.", "Outlook not so good.", "Reply hazy, try again.", "Very doubtful." ]
    #anwsers = ["Well, duh", "Yes, if you leave me alone..", "You wish", "So now you need my help...?", "You call that a question?", "Trump uses me when he decides to go to war", "Pluto says no and that he's still a planet", "Ask me when I care", "Get a life" ]
    return jsonify(anwsers)

