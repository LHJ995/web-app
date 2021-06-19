from flask import Flask, render_template, request, session, redirect
import MyDB

app = Flask(__name__)

#세션처리를 위한 키
app.secret_key = b'aaa!1234/'

#로그인/회원가입 이동 페이지
@app.route('/')
def Main():
    return render_template('main.html')

#로그인 시 들어가지는 페이지
@app.route('/Index')
def Index():
    return render_template('Index.html')

#게임페이지
@app.route('/Game')
def Game():
    return render_template('Game.html')

#테트리스 출처 : https://github.com/sangminem/tetris.git
@app.route('/Tetris')
def Tetris():
    return render_template('tetris.html')

#2048 출처 : https://github.com/yjyoon-dev/vanilla-javascript-game.git
@app.route('/2048')
def Game2048():
    return render_template('2048.html')

#노래페이지
@app.route('/Music')
def Music():
    return render_template('Music.html')

#로그인페이지
@app.route('/Signin', methods=['GET', 'POST'])
def Signin():
    if request.method == "GET":
        return render_template('Signin.html')
    if request.form['userid'] == "" or request.form['userpw'] == "":
        return '''<script>alert('아이디 혹은 비밀번호를 입력해주시길 바랍니다.'); location.href='/Signin'</script>'''
    else:
        userid = request.form['userid']
        userpw = request.form['userpw']
        adb.get_user(userid, userpw)
        ret = adb.get_user(userid, userpw)
        if ret != None:
            print(ret[1])
            session['username'] = ret[1]
            return '''<script>alert('로그인 되었습니다.'); location.href='/Index'</script>'''
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
    if request.form['userid'] == "" or request.form['userpw'] == "":
        return '''<script>alert('아이디 혹은 비밀번호를 입력해주시길 바랍니다.'); location.href='/Signup'</script>'''
    else:
        username = request.form['username']
        userid = request.form['userid']
        userpw = request.form['userpw']
        adb.insert_user(userid, username, userpw)
        return '''<script>alert('{}님 회원가입 되었습니다.'); location.href='/Signin'</script>'''.format(username)

#if __name__ == '__main__':
#    app.run()