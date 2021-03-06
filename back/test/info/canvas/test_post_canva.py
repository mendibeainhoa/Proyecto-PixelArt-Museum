from src.lib.utils import temp_file

from src.webserver import create_app

from src.domain.canva import CanvasRepository


def test_server_should_save_sprites():
    database = temp_file()
    canvas_repository = CanvasRepository(database)
    app = create_app(repositories={"canva": canvas_repository})

    client = app.test_client()

    body = {
        "id": "canva-1",
        "name": "canva-test",
        "width": 2,
        "height": 1,
        "user_id": "user-ainhoa",
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

    response = client.post(
        "api/canvas", json=body, headers={"Authorization": "user-ainhoa"}
    )
    assert response.status_code == 200

    response_get = client.get(
        "api/canva/canva-1", headers={"Authorization": "user-ainhoa"}
    )

    assert response_get.json == {
        "id": "canva-1",
        "name": "canva-test",
        "width": 2,
        "height": 1,
        "user_id": "user-ainhoa",
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
