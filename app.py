from flask import Flask, render_template
from flask.globals import request
from test import idpw_ck

app = Flask(__name__)

#기본
@app.route('/')
def Main():
    return render_template('main.html')

#게임페이지
@app.route('/Game')
def Game():
    return render_template('Game.html', image_file="img/MHR.jpg")

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
        id = request.form['id']
        pw = request.form['pw']
        return idpw_ck(id, pw)

#회원가입페이지
@app.route('/Signup', methods=['GET', 'POST'])
def Signup():
    if request.method == "GET":
        return render_template('Signup.html')
    else:
        name = request.form['username']
        return '<b>{}</b>님 회원가입 되었습니다.'.format(name)

if __name__ == '__main__':
    app.run()