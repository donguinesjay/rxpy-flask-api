from flask_restful import Resource, reqparse
from services.users_service import UserService, source
from rx import Observable
import json

class ListUsers(Resource):
	def get(self):
		# service = UserService()
		# data = service.call_all()
		# return ObserverService.on_completed()
		# return json.dumps(data)

		service = UserService()
		obs = source
		obs.subscribe(service)

