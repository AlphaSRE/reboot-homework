from flask import Flask, request, render_template
from util import *
app = Flask(__name__)


@app.route('/')
def index():
    return get_results()

@app.route('/add')
def add():
    name = request.args.get('name')
    age = request.args.get('age')
    return add_user(name,age)

@app.route('/delete')
def delete():
    name = request.args.get('name')
    return del_user(name)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=40000,debug=True)
