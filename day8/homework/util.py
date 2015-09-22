from flask import render_template, request
import MySQLdb as mysql
import json

def con_mysql():
    db = mysql.connect(user="reboot", passwd="reboot123", db="guoshuyi", charset="utf8")
    return db

def get_results():
    users = {}
    db = con_mysql()
    cur = db.cursor()
    cur.execute('select * from user')
    for tmp_arr in cur.fetchall():
        users[tmp_arr[0]] = tmp_arr[1]
    cur.close()
    db.close()

    return json.dumps(users)

def add_user(name,age):
    db = con_mysql()
    cur = db.cursor()
    test_sql = 'select * from user where name="%s"' % name
    cur.execute(test_sql)
    tmp_arr = cur.fetchall()
    if tmp_arr==():
        rel_sql = 'insert into user values("%s",%s)' % (name,age)
        cur.execute(rel_sql)
        cur.close()
        db.close()
        return get_results()
    else:
        cur.close()
        db.close()
        return get_results()

def del_user(name):
    db = con_mysql()
    cur = db.cursor()
    test_sql = 'select * from user where name="%s"' % name
    cur.execute(test_sql)
    tmp_arr = cur.fetchall()
    if tmp_arr==():
        cur.close()
        db.close()
        return get_results('index3.html')
    else:
        rel_sql = 'delete from user where name="%s"' % name
        cur.execute(rel_sql)
        cur.close()
        db.close()
        return get_results()
