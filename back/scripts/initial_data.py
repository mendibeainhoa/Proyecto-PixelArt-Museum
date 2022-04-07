import sys

sys.path.insert(0, "")
from domain.canva import CanvasRepositories, Canva, Pixels

database_path = "data/database.db"

color_1 = Pixels(
    red=1,
    green=1,
    blue=1,
)
color_2 = Pixels(
    red=1,
    green=2,
    blue=3,
)
canva = Canva(
    id="canva-1", name="canva-test", width=2, height=1, pixels=[color_1, color_2]
)

canvas_repository = CanvasRepositories(database_path)
canvas_repository.save(canva)
print("Base de datos inicializada en " + database_path)
