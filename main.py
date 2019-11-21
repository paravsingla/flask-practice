from flask import Flask
from config import DevConfig
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from models import *

app  = Flask(__name__)
app.config.from_object(DevConfig)
db = SQLAlchemy(app)
migrate = Migrate(app, db)



@app.route('/')
def home():
	return 'Hello World!'

if __name__ == '__main__':
	app.run()