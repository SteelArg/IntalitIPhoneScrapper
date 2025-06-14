from flask_restful import Resource

from app.api.api_db import db


class StoreDataRequest(Resource):
    def get(self, store):
        catalog = db.get_all_products(store)

        if catalog is None:
            return None, 404

        return catalog.to_dict(), 200
