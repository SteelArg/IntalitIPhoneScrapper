from flask_restful import Resource

from app.api.api import db


class StoreDataRequest(Resource):
    def get(self, store):
        catalog = db.get_all_products(store)

        if catalog is None:
            return None, 404

        return eval(catalog.to_json()), 200
