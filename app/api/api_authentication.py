from app.configuration import admin_password

from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash

auth = HTTPBasicAuth()

users = {
    "Admin": generate_password_hash(admin_password)
}


@auth.verify_password
def verify_password(user, password):
    if user in users and check_password_hash(users.get(user), password):
        return user
