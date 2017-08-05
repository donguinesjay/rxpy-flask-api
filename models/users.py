from db import db

class UserModel(db.Model):
	__tablename__ = 'users'

	_id = db.Column('id', db.Integer, primary_key=True)
	username = db.Column(db.String(45))
	password = db.Column(db.String(45))

	def __init__(self, *args, **kwargs):
		for name, value in kwargs.items():
			setattr(self, name, value)

	def json(self):
		return{
			'id':self._id,
			'username':self.username
			}