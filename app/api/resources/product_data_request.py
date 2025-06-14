import flask

from flask_restful import Resource

from app.api.api_authentication import auth

from app.model.product import Product

from app.api.api import db


class ProductDataRequest(Resource):
    def get(self, store: str, name: str):
        product = db.get_product(store, name)
        if product is None:
            return None, 404
        return eval(product.to_json()), 200

    @auth.login_required
    def post(self, store: str):
        args = flask.request.form
        args = dict(args)
        args["store"] = store

        product = Product.from_dict(args)
        product.validate()

        db.insert_product(product)

        return eval(product.to_json()), 200

    @auth.login_required
    def put(self, store: str):
        args = flask.request.form
        args = dict(args)
        args["store"] = store

        product = Product.from_dict(args)
        product.validate()

        db.update_product(product)

        return eval(product.to_json()), 200

    @auth.login_required
    def delete(self, store: str):
        args = flask.request.form

        db.delete_product(store, args["name"])

        return {}, 200
