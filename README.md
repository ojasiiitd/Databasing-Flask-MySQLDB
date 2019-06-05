# Trying-out-Flask

A basic **flask application which implements a simple database** using MariaDB `(mysql  Ver 15.1 Distrib 10.1.37-MariaDB, for debian-linux-gnu (x86_64) using readline 5.2)`.

A simple website using [Bulma](https://bulma.io/ "Bulma Website") has been used for styling *(no external CSS used !)*. A survey form has been made, in which entries will be submitted, and simultaneously stored in a MariaDB database.

**MariaDB is a newer version of MySQL** and uses same commands as MySQL.


## Instructions to Setup :

* Fork this repo.
* Use `git clone https://github.com/<your-github-username>/Databasing-Flask-MySQLDB.git` to clone this repo into your system

* ### Python :
	* Install pip3 on your system by `sudo apt-get install python3-pip` if not already installed.
	* Create a virtual environment by the name of **venv**. Information in setting up virtualenv can be found [here](https://docs.python-guide.org/dev/virtualenvs/ "Pipenv & Virtual Environments").
	* Enter your virtualenv by `source venv/bin/activate`
	* Do a `pip install -r requirements.txt` to install the required packages.

* ### MySQL :
	* To install latest version of *MySQL* (MariaDB)
		* Do a `sudo apt-get install mysql-server`
		* Next do `sudo apt-get install default-libmysqlclient-dev`
	* Now, to enter MariaDB, use `mysql -u root -p`.
	* You need to reste the password. For that use :
		```mysql
		sudo mysql -u root
		use mysql;
		update user set plugin='' where User='root';
		flush privileges;
		exit;
		```
	* You will now be able to use MySQL normally through the command line.
	* Create a new database named **prac** using **`CREATE DATABASE prac;`**
	* Now use this databse by a `USE prac;`
	* Then make a table called info by
		```mysql
		CREATE TABLE info (
		time_added TIMESTAMP DEFAULT NOW() , 
		name VARCHAR(30) , email VARCHAR(50) , 
		suggestion VARCHAR(500));
		```
	* Some basic MySQL commands can be found [here](https://www.digitalocean.com/community/tutorials/a-basic-mysql-tutorial "A Basic MySQL Tutorial")

## Working :

* Open command line and enter your virtualenv venv.
* Use `python app.py` and go to `localhost:5000` to show the webpage.
* Take a Survey and click Submit.
* Take a look at the contents of your database by a `SELECT * FROM info;` and the entered data will be present.
