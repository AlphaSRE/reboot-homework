from flask import Flask, render_template,request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/insert')
def insert():
    name = request.args.get('name')
    age = request.args.get('age')
    with open('file1','a+') as f:
        for i in f.readlines():
            l = i.split(':')
            if l[0] == name:
                return 'This name already exists.'
        str = '%s:%s\n' % (name,age)
        f.write(str)
    return show()
@app.route('/show')
def show():
    d = {}
    with open('file1') as f:
        for i in f.readlines():
            l = i.split(':')
            l[1] = l[1][0:2]
            d[l[0]] = l[1]
    return render_template('show.html',users=d)
@app.route('/delete')
def delete():
    d = {}
    name = request.args.get('name')
    with open('file1') as f:
        for i in f.readlines():
            l = i.split(':')
            l[1] = l[1][0:2]
            d[l[0]] = l[1]
    with open('file1','w') as f:
        if name in d:
            del d[name]
        for k,v in d.items():
            str = '%s:%s\n' % (k,v)
            f.write(str)
    return show()

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=40000,debug=True)
