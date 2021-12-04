from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def main():
   return render_template('main.html')

@app.route('/login', methods = ['GET','POST'])
def login():
   error = None
   if request.method == 'POST':
      if request.form['username'] != 'ossp' or request.form['password'] != 'ossp1234': #error 변수에 'Error 메시지 내용'을 대입
         error = 'Incorrect authentication credentials! Please try again. '
      else:
         return render_template('application_form.html')
​
   return render_template("login.html", error = error)

@app.route('/sign_up')
def sign():
   return render_template('sign_up.html')

@app.route('/application_form')
def apllication():
   return render_template('application_form.html')

@app.route('/detail', methods = ['POST', 'GET'])
def detail():
   if request.method == 'POST':
      result = dict()
      result['이름'] = request.form.get('uname')
      result['전공'] = request.form.get('umajor')
      result['학년'] = request.form.get('grade')
      result['희망 수업 방식'] = request.form.get('class')
      result['백신 접종 여부'] = request.form.get('completion')
      result['접종 백신 종류'] = request.form.get('vaccine')
      result['해당 수업방식 선호 이유'] = request.form.get('memo')
      return render_template("detail.html",result = result)

@app.route('/submit', methods = ['POST', 'GET'])
def submit():
   uname = request.form.get('uname')
   umajor = request.form.get('umajor')
   ugrade = request.form.get('ugrade')
   if request.method == 'POST':
      result = dict()
      result['이름'] = request.form.get('uname')
      result['전공'] = request.form.get('umajor')
      result['학년'] = request.form.get('grade')
      result['희망 수업 방식'] = request.form.get('class')
      result['백신 접종 여부'] = request.form.get('completion')
      result['접종 백신 종류'] = request.form.get('vaccine')
      result['해당 수업방식 선호 이유'] = request.form.get('memo')
      return render_template("submit.html",result = result, uname=uname, Grade=grade, umajor=umajor)

if __name__ == '__main__':
   app.run(host="0.0.0.0", debug=True, port=80)
