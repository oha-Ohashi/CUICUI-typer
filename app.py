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
    name = request.args.get('name')
    switch = request.args.get('switch')
    payload = request.args.get('payload')
    res = gr.generate_res(name, switch, payload)
    return res

if __name__ == '__main__':
    #app.run(debug=True)
    app.run(debug=True, host='0.0.0.0', port=5000)
    #app.run(host='0.0.0.0', port=80)
