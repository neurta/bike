from flask import Flask,request,render_template

app=Flask(__name__)

@app.route('/')
def hello():
	return render_template('main.html')

@app.route('/fire',methods=['POST'])
def start():
	print(request.form.getlist('source'))
	return 'hello'

if __name__ == '__main__':
    app.run(debug=True)
