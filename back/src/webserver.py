from crypt import methods
from flask import Flask, request
from flask_cors import CORS


from src.lib.utils import object_to_json
from src.domain.sprites import Sprites


def create_app(repositories):
    app = Flask(__name__)
    CORS(app)

    @app.route("/", methods=["GET"])
    def hello_world():
        return "...magic!"

    @app.route("/api/info", methods=["GET"])
    def info_get():
        info = repositories["info"].get_info()
        return object_to_json(info)

    @app.route("/api/sprites", methods=["GET"])
    def sprites_get():
        sprites = repositories["sprites"].get_sprites()
        return object_to_json(sprites)

    @app.route("/api/sprites", methods=["POST"])
    def sprites_post():
        body = request.json
        sprites = Sprites(**body)
        repositories["sprites"].save(sprites)

        return ""

    return app
