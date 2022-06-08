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

    response = client.post(
        "/api/users", json=body, headers={"Authorization": "user-gabri"}
    )

    assert response.status_code == 200
