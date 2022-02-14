# 기본 Flask 어플리케이션 작성
from flask import Flask  # Flask 임포트

app = Flask(__name__)  # Flask 객체 생성 -> __name__ 입력 -> app이 이름이됨


@app.route('/')  # 생성한 app 객체의 루트를 설정 ('/': 메인페이지)
                 # 설정한 루트에 따라 어떤 함수를 실행시켜야 하는지 결정 => def Hello_flask()
def Hello_flask():
    return 'Hello Flask'

@app.route('/post') 
def post():
    return "<h1>Post<h1>"    

@app.route('/post/<username>') # <변수이름> 지정 가능 
def Username(username):
    return "my name is : " + username

@app.route('/post/<int:post_id>') # <변수이름>에 데이터 타입 설정 가능
def Intname(post_id):
    return "my post_id is : %d " % post_id    

if __name__ == '__main__':  # __name__ => 해당 코드를 실행할 경우 __main__으로 변경됨
    app.run(host='0.0.0.0', debug=True)  # Flask 웹 어플리케이션 실행 메소드 = run()


# host(ex: 0.0.0.0, 127.0.0.1, ...)
# 해당 웹 서비스로 접근을 허용하는 IP 혹은 Domain을 적을 수 있다. 예를 들어(127.0.0.1)를 보내면 웹 서버를 실행시킨 해당 PC 외에는 접속이 불가능하지만, 모든 IP를 뜻하는(0.0.0.0)을 보내면 외부에서도 접속이 가능해지는 셈이다.

# debug(True or False)
# 해당 옵션을 True로 보내주면, 웹 서버가 실행 중에 코드가 변경되어도 해당 작업을 그대로 반영시킨다. 실제로 개발 중에 구현 현황을 실시간으로 확인할 수 있어 엄청 편리하다. 아무 인자도 주지 않을 경우, False 인자로 보내진다.
