from src.lib.utils import temp_file
from src.webserver import create_app
from src.domain.canva import CanvasRepository, Canva


def test_should_return_all_list_of_sprites_in_front():
    database = temp_file()
    canvas_repository = CanvasRepository(database)
    app = create_app(repositories={"canva": canvas_repository})
    client = app.test_client()

    canva = Canva(
        id="canva-1",
        name="canva-test",
        width=8,
        height=4,
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
    canva_2 = Canva(
        id="canva-2",
        name="canva-test-2",
        width=8,
        height=4,
        pixels=[
            "yellow",
            "red",
            "red",
            "blue",
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
    canvas_repository.save(canva_2)

    response = client.get("/api/load_canva")
    assert response.json == [
        {
            "id": "canva-1",
            "name": "canva-test",
            "width": 8,
            "height": 4,
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
        },
        {
            "id": "canva-2",
            "name": "canva-test-2",
            "width": 8,
            "height": 4,
            "pixels": [
                "yellow",
                "red",
                "red",
                "blue",
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
        },
    ]