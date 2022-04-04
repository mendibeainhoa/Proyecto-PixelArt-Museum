from src.lib.utils import temp_file
from src.webserver import create_app
from src.domain.sprites import SpritesRepository, Sprites


def test_should_return_sprites_in_database():
    database = temp_file
    sprites_repository = SpritesRepository(database)
    app = create_app(repositories={"sprites": sprites_repository})
    client = app.test_client()

    sprites_repository.save(
        Sprites(
            id="sprite-1",
            x_position=1,
            y_position=1,
            red=1,
            green=1,
            blue=1,
            alpha=0.10,
        )
    )

    response = client.get("/api/sprites")
    assert response.json == [
        {
            "id": "sprite-1",
            "x_position": 1,
            "y_position": 1,
            "red": 1,
            "green": 1,
            "blue": 1,
            "alpha": 0.10,
        },
        {
            "id": "sprite-2",
            "x_position": 1,
            "y_position": 2,
            "red": 1,
            "green": 1,
            "blue": 1,
            "alpha": 0.10,
        },
    ]
