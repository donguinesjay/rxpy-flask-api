from models.users import UserModel
from rx import Observable, Observer

'''class UserService:
	obs= None
	data = None
	def __init__(self):
		def callback(s):
			self.data = s
		self.obs = Observable
		self.obs.subscribe(callback)

	def on_next(self):
		users = [a.json() for a in UserModel.query.all()]
		return users
	def on_completed(self):
		return self.data
	def on_error(self):
		pass	

	def call_all(self):
		self.obs.from_(self.on_next())
		self.obs.complete()'''

def push_user_data(observer):
	observer.on_completed

class UserService(Observer):
	users = None
	def on_next(self):
		self.users = [a.json() for a in UserModel.query.all()]

	def on_completed(self):
		return self.users
	def on_error(self):
		return {"message":"Error occured"}

source = Observable.create(push_user_data)

