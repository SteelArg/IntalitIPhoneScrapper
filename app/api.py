import flask
from flask import Flask
from flask_restful import Api, Resource

from database import Database

app = Flask(__name__)
api = Api(app)

db = Database("products.db")


class ProductDataRequest(Resource):
    def get(self, store: str, name: str):
        data = db.get_product(store, name)
        if data is None:
            return None, 404
        return data, 200

    def post(self, store: str):
        args = flask.request.form
        formatted_name = db.insert_product(store, args["name"], float(args["price"]))
        return self.get(store, formatted_name), 200

    def put(self, store: str):
        args = flask.request.form
        db.update_product(store, args["name"], float(args["price"]))
        return self.get(store, args["name"]), 200

    def delete(self, store: str):
        args = flask.request.form
        db.delete_product(store, args["name"])
        return {}, 200


class StoreDataRequest(Resource):
    def get(self, store):
        data = db.get_all_products(store)
        if data is None:
            return None, 404
        return data, 200


api.add_resource(ProductDataRequest, "/data/product/<string:store>/<string:name>", "/data/product/<string:store>")
api.add_resource(StoreDataRequest, "/data/store/<string:store>")


def run_flask():
    app.run(debug=True, port=5002)


if __name__ == "__main__":
    run_flask()
