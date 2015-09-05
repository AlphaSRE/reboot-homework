from flask import Flask, request, render_template
app = Flask(__name__)

#@app.route('/delete',methods=["GET"])
#def index():
#    print request.args
#    id = request.args.get('id')
#    if id:
#        msg = '<input type="text" value='+id+' />'
#    else:
#        msg = 'error! '
#    return msg
#    return render_template('delete.html')

#@app.route('/reboot')
#def reboot():
#    return 'hello reboot'
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/js')
def index2():
    return render_template('index2.html')
@app.route('/cj')
def getcj():
    d = {}
    with open('demo0905.log') as f:
        for i in f.readlines():
            l = i.split(':')
            l[1] = l[1][0:2]
            d[l[0]] = l[1]
    s = ''
    for k,v in d.items():
        s=s+'<tr><td>'+k+'</td><td>'+v+'</td></tr>'
    s = '<table border="1">'+s+'</table>'
    return s
@app.route('/search')
def search():
    word = request.args.get('word')
    return 'search result is '+word

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=40000,debug=True)
