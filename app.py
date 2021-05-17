from flask import Flask, render_template
app = Flask(__name__)

#기본
@app.route('/')
def Main():
    return '메인'

#게임페이지
@app.route('/Game')
def Game():
    return render_template("Game.html")

#노래페이지
@app.route('/Music')
def Music():
    return '''
    <html>
    <body>

    <h2>노래방</h2>
    <img src="https://t1.daumcdn.net/cfile/blog/2074D51049CC2D353D" alt="Live pangpang">

    </body>
    </html>
    '''

if __name__ == '__main__':
    app.run()