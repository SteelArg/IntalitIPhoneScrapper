from flask import Flask
from flask_restful import Api

from app.api.api_resources import ProductDataRequest, StoreDataRequest

app = Flask(__name__)
api = Api(app)

api.add_resource(ProductDataRequest, "/data/product/<string:store>/<string:name>", "/data/product/<string:store>")
api.add_resource(StoreDataRequest, "/data/store/<string:store>")


def run_flask():
    app.run(port=5050, debug=True)

