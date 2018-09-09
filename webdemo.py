#!/usr/bin/python

from flask import Flask,render_template,request
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/str/<what>',methods=['GET'])
def str(what):
    return 'hello why%s %d'%(what,56,)

@app.route('/why/<what>')
def why(what):
    return render_template('why.html',what=what)

if __name__ == '__main__':
    app.run('127.0.0.1',8000)