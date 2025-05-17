import flask
from flask import Flask
from flask_restful import Api, Resource

from app.database import Database
from app.configuration import get_db_path

from app.model.product import Product

app = Flask(__name__)
api = Api(app)

db = Database(get_db_path())


class ProductDataRequest(Resource):
    def get(self, store: str, name: str):
        product = db.get_product(store, name)
        if product is None:
            return None, 404
        return eval(product.to_json()), 200

    def post(self, store: str):
        args = flask.request.form
        args = dict(args)
        args["store"] = store

        product = Product.from_json(args)
        product.validate()

        db.insert_product(product)

        return eval(product.to_json()), 200

    def put(self, store: str):
        args = flask.request.form
        args = dict(args)
        args["store"] = store

        product = Product.from_json(args)
        product.validate()

        db.update_product(product)

        return eval(product.to_json()), 200

    def delete(self, store: str):
        args = flask.request.form

        db.delete_product(store, args["name"])

        return {}, 200


class StoreDataRequest(Resource):
    def get(self, store):
        catalog = db.get_all_products(store)

        if catalog is None:
            return None, 404

        return eval(catalog.to_json()), 200


api.add_resource(ProductDataRequest, "/data/product/<string:store>/<string:name>", "/data/product/<string:store>")
api.add_resource(StoreDataRequest, "/data/store/<string:store>")


def run_flask():
    app.run(port=5050, debug=True)

