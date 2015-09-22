from flask import Flask,request,render_template
import json
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('js.html')

@app.route('/get_str')
def get_str():
    return 'hello reboot!'

@app.route('/get_text')
def get_text():
    return 'hehehehehe'
@app.route('/get_data')
def get_data():
    res = [{'name':'wd','age':12},{'name':'reboot','age':123}]
    return json.dumps(res)

if __name__=='__main__':
    app.run(debug=True,port=40000,host='0.0.0.0')
