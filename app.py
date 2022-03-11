from flask import Flask, request
from flask import render_template
import time
from . import generate_res as gr

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    users = [ 'Rosalia','Adrianna','Victoria' ]
    return render_template('index.html', title='Welcome', members=users)

@app.route('/ping')
def ping():
    return 'Hello From dev1 !!'

@app.route('/data')
def data():
    param_dict = {}
    for x in ['name', 'switch', 'enter', 'payload']:
        param_dict[x] = request.args.get(x)
    #print(param_dict)
    res = gr.generate_res(param=param_dict)
    return res

if __name__ == '__main__':
    #app.run(debug=True)
    app.run(debug=True, host='0.0.0.0', port=5000)
    #app.run(host='0.0.0.0', port=80)
