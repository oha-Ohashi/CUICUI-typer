from flask import Flask, request
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', title='Welcome')

@app.route('/ping')
def ping():
    return 'Hello From dev1 !!'

if __name__ == '__main__':
    #app.run(debug=True)
    app.run(debug=True, host='0.0.0.0', port=5000)
    #app.run(host='0.0.0.0', port=80)