from main import app, db, migrate
from models import User, Post, Tag, Comment

@app.shell_context_processor
def make_shell_context():
	return dict(app=app, db=db, User=User, Post=Post, Tag=Tag, Comment=Comment, migrate=migrate)