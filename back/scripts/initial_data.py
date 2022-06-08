import sys

sys.path.insert(0, "")
from src.domain.canva import CanvasRepository, Canva
from src.domain.user import UserRepository, User

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
        "#b34747",
        "#793434",
        "#b34747",
        "#793434",
        "#b34747",
        "#793434",
        "#b34747",
        "#793434",
        "#b34747",
        "#793434",
    ],
)
canva_two = Canva(
    id="canva-2",
    name="canva-test-2",
    width=8,
    height=4,
    pixels=[
        "blue",
        "white",
        "red",
        "yellow",
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
        "#b34747",
        "#793434",
        "#b34747",
        "#793434",
        "#b34747",
        "#793434",
        "#b34747",
        "#793434",
        "#b34747",
        "#793434",
    ],
)
canvas_repository = CanvasRepository(database_path)
canvas_repository.save(canva)
canvas_repository.save(canva_two)


user_one = User(id="user-ainhoa", name="ainhoa", password="aguacate")
user_two = User(id="user-gabriel", name="an3xo", password="petin")
user_repository = UserRepository(database_path)
user_repository.save(user_one)
user_repository.save(user_two)
print("Base de datos inicializada en " + database_path)
