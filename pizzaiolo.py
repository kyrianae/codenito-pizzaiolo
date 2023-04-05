#!/usr/bin/python3.8
from flask import Flask, json, request, Response
import random

app = Flask("pizzaiolo")

@app.route('/hello', methods=['GET'])
def hello():
    print ("Pizzaiolo says: Hello World")
    return "Pizzaiolo says: Hello World\n"

@app.route('/make_pizza', methods=['GET'])
def make_pizza():
    print ("Pizzaiolo\tMade a pizza")
    return "Pizzaiolo\tMade a pizza"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8082)
