from src.lib.utils import temp_file

from src.webserver import create_app

from src.domain.canva import CanvasRepository, Canva


def test_should_delete_canvas():
    database = temp_file()
    canvas_repository = CanvasRepository(database)
    app = create_app(repositories={"canva": canvas_repository})
    client = app.test_client()

    canva_one = Canva(
        id="canva-1",
        name="canva-test",
        width=2,
        height=5,
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
        ],
    )
    canva_two = Canva(
        id="canva-2",
        name="canva-test-2",
        width=2,
        height=3,
        user_id="user-ainhoa",
        pixels=["yellow", "red", "red", "blue", "white", "white"],
    )
    canvas_repository.save(canva_one)
    canvas_repository.save(canva_two)

    # ACT (when)

    body = {
        "id": "canva-1",
        "name": "canva-test",
        "width": 2,
        "height": 5,
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
        ],
    }

    response_delete = client.delete(
        "/api/load_canva/canva-1", json=body, headers={"Authorization": "user-ainhoa"}
    )
    assert response_delete.status_code == 200

    # ASSERT (then)
    response = client.get("/api/load_canva", headers={"Authorization": "user-ainhoa"})
    assert response.json == [
        {
            "id": "canva-2",
            "name": "canva-test-2",
            "width": 2,
            "height": 3,
            "user_id": "user-ainhoa",
            "pixels": [
                "yellow",
                "red",
                "red",
                "blue",
                "white",
                "white",
            ],
        }
    ]
