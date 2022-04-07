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
        }
    ]
    sprites_repository.save(sprites)

    response = client.post("api/sprites/sprite-1", json=sprites)
    assert response.status_code == 200

    response_get = client.get("api/sprites/sprite-1")
    sprites_list = response_get.json
    assert len(sprites_list) == 49
    assert sprites_list[0]["id"] == "sprite-1"
    assert sprites_list[0]["x_position"] == 1
    assert sprites_list[0]["y_position"] == 1
    assert sprites_list[0]["red"] == 1
    assert sprites_list[0]["green"] == 1
    assert sprites_list[0]["blue"] == 1
    assert sprites_list[0]["alpha"] == 0.10

    # assert response_get.json == [
    #     {
    #         "id": "sprite-1",
    #         "x_position": 1,
    #         "y_position": 1,
    #         "red": 1,
    #         "green": 1,
    #         "blue": 1,
    #         "alpha": 0.10,
    #     }
    # ]
