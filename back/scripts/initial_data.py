import sys

sys.path.insert(0, "")
from src.domain.canva import CanvasRepository, Canva

database_path = "data/database.db"


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
canvas_repository = CanvasRepository(database_path)
canvas_repository.save(canva)
print("Base de datos inicializada en " + database_path)
