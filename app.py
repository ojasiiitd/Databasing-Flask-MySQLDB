from flask import Flask , render_template

app = Flask(__name__)

@app.route('/')
def homepage():
	return render_template('index.html')

@app.route('/next')
def next():
	return render_template('next.html')

@app.route('/last')
def last():
	return render_template('last.html')

if __name__ == '__main__':
	app.run(, debug=True)