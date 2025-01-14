from ninja import NinjaAPI
from shortener.api import shortener_router

api = NinjaAPI()
api.add_router('', shortener_router)