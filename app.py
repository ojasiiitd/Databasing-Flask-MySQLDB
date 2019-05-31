from flask import Flask , render_template , flash , redirect , url_for , request
from flask_mysqldb import MySQL
from wtforms import Form , StringField , TextAreaField , validators

app = Flask(__name__)

# Setting up MariaDB
app.config["MYSQL_HOST"] = 'localhost'
app.config["MYSQL_USER"] = 'root'
app.config["MYSQL_PASSWORD"] = ''
app.config["MYSQL_DB"] = 'prac'
app.config["MYSQL_CURSORCLASS"] = 'DictCursor'
# Initialising MariaDB
mysql = MySQL(app)

@app.route('/')
def homepage():
	return render_template('information.html')

class suggestions(Form) :
	name = StringField("Name" , validators = [
		validators.input_required(),
		validators.Length(min=1 , max=40)
		])
	email = StringField("Email-ID" , validators = [
		validators.input_required(),
		validators.Length(min=5 , max=50)
		])
	sugg = TextAreaField("Your Suggestion" , validators = [
		validators.input_required(),
		validators.Length(min=1 , max=500)
		])

@app.route('/survey' , methods = ["GET" , "POST"])
def survey():
	form = suggestions(request.form)
	if request.method == "POST" and form.validate() :
		name = form.name.data
		email = form.email.data
		sugg = form.sugg.data
		
		# Create Cursor
		cur = mysql.connection.cursor()

		# Execute query
		cur.execute("insert into info values(NULL , %s , %s , %s)" , (name , email , sugg))

		# Commit to DB
		mysql.connection.commit()
		cur.close()

		flash("Your suggestion has been recorded. Thank you for your time." , "success")
		return redirect(url_for("survey"))

	return render_template('survey.html' , form = form)

if __name__ == '__main__':
	app.secret_key = "thisisthebestsecretkeyever"
	app.run()