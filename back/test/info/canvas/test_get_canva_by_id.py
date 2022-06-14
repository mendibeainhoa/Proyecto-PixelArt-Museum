from src.lib.utils import temp_file
from src.webserver import create_app
from src.domain.canva import CanvasRepository, Canva


def test_should_return_sprites_in_front():
    database = temp_file()
    canvas_repository = CanvasRepository(database)
    app = create_app(repositories={"canva": canvas_repository})
    client = app.test_client()

    canva = Canva(
        id="canva-1",
        name="canva-test",
        width=8,
        height=4,
        user_id="user-ainhoa",
        pixels=[
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
    )

    canvas_repository.save(canva)

    response = client.get(
        "/api/canva/canva-1", headers={"Authorization": "user-ainhoa"}
    )
    assert response.json == {
        "id": "canva-1",
        "name": "canva-test",
        "width": 8,
        "height": 4,
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
