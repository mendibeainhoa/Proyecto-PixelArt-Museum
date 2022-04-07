from crypt import methods
from flask import Flask, request
from flask_cors import CORS


from src.lib.utils import object_to_json
from src.domain.canva import Canva


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

    @app.route("/api/canva", methods=["GET"])
    def canva_get():
        canva = repositories["canva"].get_canva()
        return object_to_json(canva)

    @app.route("/api/canva", methods=["POST"])
    def canva_post():
        body = request.json
        canva = Canva(**body)
        repositories["sprites"].save(canva)

        return ""

    return app
