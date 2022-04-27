from urllib import response
from src.lib.utils import temp_file

from src.webserver import create_app

from src.domain.canva import CanvasRepository


def test_server_should_save_canvas():
    database = temp_file()
    canvas_repository = CanvasRepository(database)
    app = create_app(repositories={"canvas": canvas_repository})

    client = app.test_client()

    canva = {
        "id": "canva-1",
        "name": "canva-test",
        "width": 2,
        "height": 1,
        "pixels": [
            "yellow",
            "white",
            "white",
            "white",
            "white",
            "white",
            "white",
            "white",
            "white",
            "white",
            "white",
            "white",
            "#b34747",
            "#793434",
            "white",
            "white",
            "white",
            "white",
            "white",
            "white",
            "white",
            "white",
            "white",
        ],
    }
    canvas_repository.save(canva)

    response = client.post("api/canvas/sprite-1", json=canva)
    assert response.status_code == 200

    response_get = client.get("api/canva/canva-1")

    assert response_get.json == {
        "id": "canva-1",
        "name": "canva-test",
        "width": 2,
        "height": 1,
        "pixels": [
            "yellow",
            "white",
            "white",
            "white",
            "white",
            "white",
            "white",
            "white",
            "white",
            "white",
            "white",
            "white",
            "#b34747",
            "#793434",
            "white",
            "white",
            "white",
            "white",
            "white",
            "white",
            "white",
            "white",
            "white",
        ],
    }
