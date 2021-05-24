from flask import Flask, render_template
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
@app.route('/Login', methods=['GET','POST'])
def Login():
    if request.method == "GET":
        return '그냥 넘어옴'
    else:
        return '그냥 넘어옴'

#로그인후페이지
@app.route('/Loginac')
def Loginac():
    return '로그인 되었습니다.'

if __name__ == '__main__':
    app.run()