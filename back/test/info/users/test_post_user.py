from src.lib.utils import temp_file

from src.webserver import create_app

from src.domain.user import UserRepository, User


def test_should_return_new_user():
    user_repository = UserRepository(temp_file())
    app = create_app(repositories={"users": user_repository})
    client = app.test_client()

    body = {
        "id": "user-gabri",
        "name": "an3xo",
        "email": "petin@example.es",
        "password": "petin",
    }

    response_post = client.post(
        "/api/users", json=body, headers={"Authorization": "user-gabri"}
    )

    assert response_post.status_code == 200

    response_get = client.get(
        "/api/users", json=body, headers={"Authorization": "user-gabri"}
    )

    user = response_get.json
    assert user[0]["id"] == "user-gabri"
    assert user[0]["name"] == "an3xo"
    assert user[0]["email"] == "petin@example.es"
    assert user[0]["password"] == "petin"
