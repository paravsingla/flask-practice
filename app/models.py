import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import UserMixin

class User(UserMixin, db.Model):
	id = db.Column(db.Integer(), primary_key = True)
	username = db.Column(db.String(255), nullable=False, unique=True)
	password = db.Column(db.String(255))
	posts = db.relationship('Post', backref='user', lazy='dynamic')

	@property
	def pwd(self):
		raise AttributeError('pwd is not a readable attribute')

	@pwd.setter
	def pwd(self, pwd):
		self.password = generate_password_hash(pwd)
	

	def __init__(self, username):
		self.username = username

	def __repr__(self):
		return "<User '{}'>".format(self.username)

	def verify_password(self, password):
		return check_password_hash(self.password, password)


tags = db.Table('post_tags',
	db.Column('post_id', db.Integer(), db.ForeignKey('post.id')),
	db.Column('tag_id', db.Integer(), db.ForeignKey('tag.id'))
	)


class Post(db.Model):
	id = db.Column(db.Integer(), primary_key=True)
	title = db.Column(db.String(255), nullable=False)
	text = db.Column(db.Text())
	publish_date = db.Column(db.DateTime(), default=datetime.datetime.now)
	user_id = db.Column(db.Integer(), db.ForeignKey('user.id'))
	comments = db.relationship('Comment', backref='post', lazy='dynamic')
	tags = db.relationship('Tag', secondary=tags, backref=db.backref('posts', lazy='dynamic'))

	def __init__(self, title):
		self.title = title

	def __repr__(self):
		return "<Post '{}'>".format(self.title)

class Comment(db.Model):
	id = db.Column(db.Integer(), primary_key=True)
	name = db.Column(db.String(255), nullable=False)
	text = db.Column(db.Text())
	date = db.Column(db.DateTime(), default=datetime.datetime.now)
	post_id = db.Column(db.Integer(), db.ForeignKey('post.id'))

	def __repr__(self):
		return "<Comment '{}'>".format(self.text[:15])

class Tag(db.Model):
	id = db.Column(db.Integer(), primary_key = True)
	title = db.Column(db.String(255), nullable=True, unique=True)

	def __init__(self, title):
		self.title = title

	def __repr__(self):
		return "<Tag '{}'>".format(self.title)