from flask import Flask, render_template, request
import logging
import time


# Setting up the app 
app = Flask(__name__)

# Setting up the mail page load
@app.route('/')
def index():
    return 'TODO'

# Setting up the forward runner
@app.route('/forward', methods=['GET'])
def forward():
    return 'forward'

# Setting up the backward runner
@app.route('/backward', methods=['GET'])
def backward():
    return 'backward'

# Setting up the left turn
@app.route('/left', methods=['GET'])
def left():
    return 'left'

# Setting up the right turn
@app.route('/right', methods=['GET'])
def right():
    return 'right'




# Setting up the main runner 
if __name__== '__main__':
    app.run(host='127.0.0.1', debug=True)
