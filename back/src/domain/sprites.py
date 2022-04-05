import sqlite3
from unittest import result


class Sprites:
    def __init__(self, id, x_position, y_position, red, green, blue, alpha):
        self.id = id
        self.x_position = x_position
        self.y_position = y_position
        self.red = red
        self.green = green
        self.blue = blue
        self.alpha = alpha

    def to_dict(self):
        return {
            "id": self.id,
            "x_position": self.x_position,
            "y_position": self.y_position,
            "red": self.red,
            "green": self.green,
            "blue": self.blue,
            "alpha": self.alpha,
        }


class SpritesRepository:
    def __init__(self, database_path):
        self.database_path = database_path
        self.init_tables()

    def create_conn(self):
        conn = sqlite3.connect(self.database_path)
        conn.row_factory = sqlite3.Row
        return conn

    def init_tables(self):

        sql = """
        CREATE TABLE if not exists sprites(
            "id" VARCHAR,
            "x_position" INTERGER,
            "y_position" INTERGER,
            "red" INTERGER,
            "green" INTERGER,
            "blue" INTERGER,
            "alpha" REAL
        )"""
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()

    def get_sprites(self):
        sql = """select * from sprites"""
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql)

        data = cursor.fetchall()

        result = []
        for item in data:
            sprites = Sprites(**item)
            result.append(sprites)

        return result

    def save(self, sprites):
        sql = """INSERT INTO sprites(id, x_position, y_position, red, green, blue, alpha) values
        (:id, :x_position, :y_position, :red, :green, :blue, :alpha)"""
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(
            sql,
            {
                "id": sprites.id,
                "x_position": sprites.x_position,
                "y_position": sprites.y_position,
                "red": sprites.red,
                "green": sprites.green,
                "blue": sprites.blue,
                "alpha": sprites.alpha,
            },
        )

        conn.commit()
