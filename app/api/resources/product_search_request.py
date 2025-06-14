import flask

from flask_restful import Resource

from app.configuration import stores

from app.model.product_search_result import ProductSearchResult

from app.api.api_db import db


class ProductSearchRequest(Resource):
    def get(self):
        args = flask.request.form
        search_keywords = eval(args["keywords"])

        searched_products = []

        for store in stores:
            catalog = db.get_all_products(store)
            for product in catalog.products:
                fits_search = True

                for keyword in search_keywords:
                    if keyword not in product.name:
                        fits_search = False

                if fits_search:
                    searched_products.append(product)

        search_result = ProductSearchResult(search_keywords, searched_products)

        return search_result.to_json(), 200
