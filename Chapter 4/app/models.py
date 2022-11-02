from datetime import datetime
from app import db

#Represents users
class User(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	username = db.Column(db.String(64), index = True, unique = True)
	email = db.Column(db.String(120), index = True, unique = True)
	password_hash = db.Column(db.String(128))
	posts = db.relationship('Post', backref = 'author', lazy = 'dynamic')

	#Tells Python how to print objects of this class
	def __repr__(self):
		return f'<User {self.username}>'

#Represent blog posts written by users
class Post(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	body = db.Column(db.String(140))
	timestamp = db.Column(db.DateTime, index = True, default = datetime.utcnow)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

	def __repr__(self):
		return f'<Post {self.body}>'