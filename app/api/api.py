from flask import Flask
from flask_restful import Api

from app.api.resources.store_data_request import  StoreDataRequest
from app.api.resources.product_data_request import ProductDataRequest

from app.database import Database
from app.configuration import get_db_path

app = Flask(__name__)
api = Api(app)

db = Database(get_db_path())

api.add_resource(ProductDataRequest, "/data/product/<string:store>/<string:name>", "/data/product/<string:store>")
api.add_resource(StoreDataRequest, "/data/store/<string:store>")


def run_flask():
    app.run(port=5050, debug=True)

