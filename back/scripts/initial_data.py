import sys

sys.path.insert(0, "")
from src.domain.sprites import SpritesRepository, Sprites

database_path = "data/database.db"


sprites_repository = SpritesRepository(database_path)


sprites_repository.save(Sprites(""))
