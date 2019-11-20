from flask import Flask
from config import DevConfig
from flask_sqlalchemy import SQLAlchemy

app  = Flask(__name__)
app.config.from_object(DevConfig)
db = SQLAlchemy(app)

class User(db.Model):
	id = db.Column(db.Integer(), primary_key = True)
	username = db.Column(db.String(255))
	password = db.Column(db.String(255))

	def __init__(self, username):
		self.username = username

@app.route('/')
def home():
	return 'Hello World!'

if __name__ == '__main__':
	app.run()