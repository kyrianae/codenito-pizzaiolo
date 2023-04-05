#!/usr/bin/python3.8
from flask import Flask, json, request, Response
import random
import datetime

app = Flask("pizzaiolo")

def str_now():
    return str(datetime.datetime.now())

@app.route('/hello', methods=['GET'])
def hello():
    print (str_now()+"\t"+"Pizzaiolo says: Hello World")
    return str_now()+"\t"+"Pizzaiolo says: Hello World\n"

@app.route('/make_pizza', methods=['GET'])
def make_pizza():
    print (str_now()+"\t"+"Pizzaiolo\tMade a pizza")
    return str_now()+"\t"+"Pizzaiolo\tMade a pizza"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8082)
