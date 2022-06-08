from src.lib.utils import temp_file

from src.webserver import create_app

from src.domain.user import UserRepository, User


def setup():
    user_repository = UserRepository(temp_file())
    app = create_app(repositories={"users": user_repository})
    client = app.test_client()

    ainhoa = User(
        id="user-ainhoa",
        name="Ainhoa",
        email="petin@example.es",
        password="aguacate",
    )
    user_repository.save(ainhoa)

    return client


def test_should_validate_login():
    client = setup()

    body = {"name": "Ainhoa", "password": "aguacate"}
    response = client.post("/auth/login", json=body)

    assert response.status_code == 200
    response_get = client.get("/api/users")

    users = response_get.json
    assert users[0]["name"] == "Ainhoa"
    assert users[0]["password"] == "aguacate"


def test_should_fail_if_invalid_password():
    client = setup()

    body = {"name": "Ainhoa", "password": "carne"}
    response = client.post("/auth/login", json=body)

    assert response.status_code == 401


def test_should_fail_if_user_not_exists():
    client = setup()

    body = {"name": "not-exists", "password": "aguacate"}
    response = client.post("/auth/login", json=body)

    assert response.status_code == 401
