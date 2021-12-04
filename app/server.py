from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def main():
   return render_template('main.html')

@app.route('/login')
def login():
   return render_template('login.html')

@app.route('/sign up')
def sign():
   return render_template('sign up.html')

@app.route('/application form')
def apllication():
   return render_template('application form.html')

@app.route('/detail', methods = ['POST', 'GET'])
def detail():
   if request.method == 'POST':
      result = dict()
      result['Name'] = request.form.get('Name')
      result['Major'] = request.form.get('Major')
      result['Grade'] = request.form.get('Grade')
      result['Desire_method'] = request.form.get('Desire_method')
      result['Vaccine'] = request.form.get('Vaccine')
      result['Reason'] = request.form.get('Reason')
      return render_template("detail.html",result = result)

@app.route('/submit', methods = ['POST', 'GET'])
def submit():
   uname = request.form.get('uname')
   umajor = request.form.get('umajor')
   ugrade = request.form.get('ugrade')
   if request.method == 'POST':
      result = dict()
      result['Name'] = request.form.get('Name')
      result['Major'] = request.form.get('Major')
      result['Grade'] = request.form.get('Grade')
      result['Desire_method'] = request.form.get('Desire_method')
      result['Vaccine'] = request.form.get('Vaccine')
      result['Reason'] = request.form.get('Reason')
      return render_template("submit.html",result = result, uname=uname, Grade=Grade, umajor=umajor)

if __name__ == '__main__':
   app.run(host="0.0.0.0", debug=True, port=80)
