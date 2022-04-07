import sys

sys.path.insert(0, "")
from src.domain.sprites import SpritesRepository, Sprites

database_path = "data/database.db"

color_1 = Sprites(
    id="sprite-1", x_position=1, y_position=1, red=1, green=1, blue=1, alpha=0.10
)

sprites_repository = SpritesRepository(database_path)
sprites_repository.save(color_1)
print("Base de datos inicializada en " + database_path)
