from flask import Flask, request
from flask import render_template
from .python_scripts import cuicui_command as cc

app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False

@app.route("/favicon.ico")
def favicon():
    return app.send_static_file("favicon.ico")

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Welcome')

@app.route('/cuicui')
def cuicui():
    return render_template('cuicui.html', title='Welcome')

@app.route('/cuicui_command')
def cuicui_command():
    param_list = []
    for x in ['arg1', 'arg2', 'arg3', 'arg4']:
        param_list.append(request.args.get(x))
    return cc.generate_res(param=param_list)

@app.route('/ortho_heat')
def ortho_heat():
    return render_template('ortho_heat.html')

@app.route('/ortho_typing')
def ortho_typing():
    return render_template('ortho_typing.html')

@app.route('/ping')
def ping():
    return 'Hello From dev1 !!'

if __name__ == '__main__':
    #app.run(debug=True)
    app.run(debug=True, host='0.0.0.0', port=5000)
    #app.run(host='0.0.0.0', port=80)