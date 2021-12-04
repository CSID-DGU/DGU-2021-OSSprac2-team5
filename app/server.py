from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def main():
   return render_template('main.html')

@app.route('/detail', methods = ['POST', 'GET'])
def detail():
   if request.method == 'POST':
      result = dict()
      result['Name'] = request.form.get('Name')
      result['Major'] = request.form.get('Major')
      result['Year'] = request.form.get('Year')
      result['Desire_metod'] = request.form.get('Desire_metod')
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
      result['Year'] = request.form.get('Year')
      result['Desire_metod'] = request.form.get('Desire_metod')
      result['Vaccine'] = request.form.get('Vaccine')
      result['Reason'] = request.form.get('Reason')
      return render_template("submit.html",result = result, uname=uname, uyear=uyear, umajor=umajor)

if __name__ == '__main__':
   app.run(host="0.0.0.0", debug=True, port=80)
