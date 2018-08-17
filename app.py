# hello_flask.py
# 웹 서버를 띄우는 코드
from flask import Flask

app = Flask(__name__)

# http:/IP주소:5000/   # 브라우저가 우리 서버를 요청하면
# '/' : root
@app.route("/")   # 어떤 URL이 들어왔을때의 처리
def hello_world():
    return 'Hello World'

# http://IP주소:5000/abc   # 브라우저가 우리 서버를 요청하면
# '/' : root
@app.route("/abc")   # 어떤 URL이 들어왔을때의 처리
def hello_world():
    return 'Hello abc'

if __name__ == '__main__' :
    app.run('0.0.0.0')   # # 0.0.0.0 이라고 해줘야 외부에서 접속 가능

