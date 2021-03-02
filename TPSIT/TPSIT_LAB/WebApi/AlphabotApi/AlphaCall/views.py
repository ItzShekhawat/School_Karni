from flask import Flask, Blueprint, request, render_template, jsonify

views = Blueprint('views', __name__)

# Home page route
@views.route('/')
def index():
    return render_template('index.html')


#### Path Send  #### 
@views.route('/path', methods=['POST'])
def path():
    if request.method == 'POST':
        if 'pathSTART' in request.args:
            pathSTART = request.args['pathSTART']
        elif 'pathEND' in request.args:
            pathEND = request.args['pathEnd']
        else:
            return "The path Start and End must be specified."
    
    print (f"The starting point is {pathSTART} and the ending point is {pathEND}")
    
            

