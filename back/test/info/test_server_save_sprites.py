from urllib import response
from src.lib.utils import temp_file

from src.webserver import create_app

from src.domain.sprites import SpritesRepository, Sprites


def test_server_should_save_sprites():
    database = temp_file()
    sprites_repository = SpritesRepository(database)
    app = create_app(repositories={"sprites": sprites_repository})

    client = app.test_client()

    sprites = [
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
    sprites_repository.save(sprites)
    response = client.post("api/sprites", json=sprites)
    assert response.status_code == 200

    response_get = client.get("api/sprites")
    assert response_get.json == [
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
