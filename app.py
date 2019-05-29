from flask import Flask , render_template

app = Flask(__name__)

@app.route('/')
def homepage():
	return render_template('information.html')

@app.route('/survey')
def survey():
	return render_template('survey.html')

if __name__ == '__main__':
	app.run(port = "4000")