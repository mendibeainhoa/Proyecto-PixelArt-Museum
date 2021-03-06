import re
from flask import Flask, request
from flask_cors import CORS


from src.lib.utils import object_to_json
from src.domain.canva import Canva
from src.domain.user import User
import json


def create_app(repositories):
    app = Flask(__name__)
    CORS(app)

    @app.route("/", methods=["GET"])
    def hello_world():
        return "...magic!"

    @app.route("/api/load_canva", methods=["GET"])
    def canvas_get():
        user_id = request.headers.get("Authorization")
        all_canvas_of_user = repositories["canva"].get_all_canva(user_id)
        return object_to_json(all_canvas_of_user)

    @app.route("/api/canva/<id>", methods=["GET"])
    def canva_get_by_id(id):
        user_id = request.headers.get("Authorization")
        canva = repositories["canva"].get_canva_by_id(id)

        if user_id == canva.user_id:
            return object_to_json(canva), 200
        else:
            return "", 403

    @app.route("/api/canvas", methods=["POST"])
    def canva_post():
        user_id = request.headers.get("Authorization")
        body = request.json
        canva = Canva(
            id=body["id"],
            name=body["name"],
            width=body["width"],
            height=body["height"],
            user_id=user_id,
            pixels=body["pixels"],
        )
        repositories["canva"].save(canva)

        return "", 200

    @app.route("/auth/login", methods=["POST"])
    def login():
        body = request.json
        user = repositories["users"].get_by_name(body["name"])
        if user is None or body["password"] != user.password:
            return "", 401

        return user.to_dict(), 200

    @app.route("/api/users", methods=["GET"])
    def get_users():
        users = repositories["users"].get_all()
        return object_to_json(users)

    @app.route("/api/load_canva/<id>", methods=["DELETE"])
    def delete_canva(id):
        user_id = request.headers.get("Authorization")
        canva = repositories["canva"].get_canva_by_id(id)

        if user_id == canva.user_id:
            repositories["canva"].delete_canva(id)
            return "", 200
        else:
            return "", 403

    @app.route("/api/users", methods=["POST"])
    def users_post():
        body = request.json
        users = User(**body)
        repositories["users"].save(users)

        return "", 200

    return app
