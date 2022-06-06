import sqlite3
import json


class Canva:
    def __init__(self, id, name, width, height, pixels):
        self.id = id
        self.name = name
        self.width = width
        self.height = height
        self.pixels = pixels

        # if pixels is not None:
        #     self.pixels = pixels
        # else:
        #     self.pixels = []

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "width": self.width,
            "height": self.height,
            "pixels": self.pixels,
        }


class CanvasRepository:
    def __init__(self, database_path):
        self.database_path = database_path
        self.init_tables()

    def create_conn(self):
        conn = sqlite3.connect(self.database_path)
        conn.row_factory = sqlite3.Row
        return conn

    def init_tables(self):

        sql = """
        CREATE TABLE if not exists canva(
            "id" VARCHAR PRIMARY KEY,
            "name" VARCHAR,
            "width" INTERGER,
            "height" INTERGER,
            "pixels" VARCHAR)"""
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()

    def get_all_canva(self):
        sql = """SELECT * FROM canva"""
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql)

        data = cursor.fetchall()

        canvas = []
        for item in data:
            canva = Canva(
                id=item["id"],
                name=item["name"],
                width=item["width"],
                height=item["height"],
                pixels=json.loads(item["pixels"]),
            )
            canvas.append(canva)

        return canvas

    def get_canva_by_id(self, id):
        sql = """SELECT * FROM canva WHERE id=:id"""
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql, {"id": id})
        print(id)
        data = cursor.fetchone()

        canva = Canva(
            id=data["id"],
            name=data["name"],
            width=data["width"],
            height=data["height"],
            pixels=json.loads(data["pixels"]),
        )

        return canva

    def save(self, canva):
        print(canva.to_dict())
        sql = """INSERT OR REPLACE INTO canva(id, name, width, height, pixels) values
        (:id, :name, :width, :height, :pixels)"""
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(
            sql,
            {
                "id": canva.id,
                "name": canva.name,
                "width": canva.width,
                "height": canva.height,
                "pixels": json.dumps(canva.pixels),
            },
        )

        conn.commit()
