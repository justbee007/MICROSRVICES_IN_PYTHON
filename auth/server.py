from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError
import jwt
import datetime
import os

server = Flask(__name__)

# Configure SQLAlchemy
server.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:example@localhost:8081/auth'
server.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(server)

# JWT configuration
jwt_secret = "lolz"


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return f'<User {self.email}>'


@server.route("/login", methods=["POST"])
def login():
    auth = request.authorization
    if not auth:
        return "missing credentials", 401

    # Check db for username and password
    user = User.query.filter_by(email=auth.username, password=auth.password).first()

    if user:
        return create_jwt(user.email, jwt_secret, True), 200
    else:
        return "invalid credentials", 401


@server.route("/validate", methods=["POST"])
def validate():
    encoded_jwt = request.headers.get("Authorization")

    if not encoded_jwt:
        return "missing credentials", 401

    encoded_jwt = encoded_jwt.split(" ")[1]

    try:
        decoded = jwt.decode(encoded_jwt, jwt_secret, algorithms=["HS256"])
    except jwt.ExpiredSignatureError:
        return "token has expired", 401
    except jwt.InvalidTokenError:
        return "not authorized", 403

    return jsonify(decoded), 200


def create_jwt(username, secret, authz):
    return jwt.encode(
        {
            "username": username,
            "exp": datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(days=1),
            "iat": datetime.datetime.utcnow(),
            "admin": authz,
        },
        secret,
        algorithm="HS256",
    )


if __name__ == "__main__":
    # Create database tables if they do not exist
    server.run(host="0.0.0.0", port=5001)
