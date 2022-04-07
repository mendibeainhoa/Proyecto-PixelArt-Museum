from src.lib.utils import temp_file
from src.webserver import create_app
from src.domain.canva import CanvasRepository, Pixels, Canva


def test_should_return_sprites_in_front():
    database = temp_file()
    canvas_repository = CanvasRepository(database)
    app = create_app(repositories={"canvas": canvas_repository})
    client = app.test_client()

    color_1 = Pixels(
        red=1,
        green=1,
        blue=1,
    )
    color_2 = Pixels(
        red=1,
        green=2,
        blue=3,
    )
    canva = Canva(
        id="canva-1", name="canva-test", width=2, height=1, pixels=[color_1, color_2]
    )

    canvas_repository.save(canva)

    response = client.get("/api/canva/canva-1")
    assert response.json == {
        "id": "canva-1",
        "name": "canva-test",
        "width": 2,
        "height": 1,
        "pixels": [
            {
                "red": 1,
                "green": 1,
                "blue": 1,
            },
            {
                "red": 1,
                "green": 2,
                "blue": 3,
            },
        ],
    }
