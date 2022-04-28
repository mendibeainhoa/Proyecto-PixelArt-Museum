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

    @app.route("/api/canva/<id>", methods=["GET"])
    def canva_get_by_id(id):
        print(repositories)
        canva = repositories["canva"].get_canva_by_id(id)
        return object_to_json(canva)

    @app.route("/api/canvas/<id>", methods=["POST"])
    def canva_post(id):
        body = request.json
        canva = Canva(**body)
        repositories["canva"].save(canva)

        return "", 200

    return app
