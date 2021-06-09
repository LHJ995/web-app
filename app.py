from flask import Flask, render_template, session, redirect
from flask.globals import request
from code import idpw_ck
import adb

#세션처리를 위한 키
app.secret_key = b'aaa!1234/'

app = Flask(__name__)

#기본
@app.route('/')
def Main():
    return render_template('main.html')

#게임페이지
@app.route('/Game')
def Game():
    return render_template('Game.html')

#노래페이지
@app.route('/Music')
def Music():
    return render_template('Music.html')

#로그인페이지
@app.route('/Signin', methods=['GET', 'POST'])
def Signin():
    if request.method == "GET":
        return render_template('Signin.html')
    else:
        userid = request.form['userid']
        userpw = request.form['userpw']
        adb.get_user(userid, userpw)
        ret = adb.get_user(userid, userpw)
        if ret != None:
            print(ret[1])
            session['username'] = ret[1]
            return redirect('/')
        else:
            return redirect('/Signin')

#로그아웃
@app.route('/Logout')
def Logout():
    session.pop('user', None)
    return redirect('/')

#회원가입페이지
@app.route('/Signup', methods=['GET', 'POST'])
def Signup():
    if request.method == "GET":
        return render_template('Signup.html')
    else:
        username = request.form['username']
        userid = request.form['userid']
        userpw = request.form['userpw']
        adb.insert_user(userid, username, userpw)
        return '<b>{}</b>님 회원가입 되었습니다.'.format(username)

#검색페이지
#@app.route('/search')
#def search():
#    if 'username' in session

if __name__ == '__main__':
    app.run()