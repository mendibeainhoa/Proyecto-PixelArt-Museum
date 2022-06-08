import sqlite3
import json

import sqlite3


class User:
    def __init__(self, id, name, email, password):
        self.id = id
        self.name = name
        self.email = email
        self.password = password

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "password": self.password,
        }


class UserRepository:
    def __init__(self, database_path):
        self.database_path = database_path
        self.init_tables()

    def create_conn(self):
        conn = sqlite3.connect(self.database_path)
        conn.row_factory = sqlite3.Row
        return conn

    def init_tables(self):
        sql = """
           CREATE TABLE if not exists users (
                id varchar primary key,
                name varchar,
                email varchar,
                password varchar
            )
        """
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()

    def get_all(self):
        sql = """SELECT * FROM users"""
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql)

        data = cursor.fetchall()

        users = [User(**item) for item in data]
        return users

    def get_by_name(self, name):
        sql = """SELECT * FROM users WHERE name=:name"""
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql, {"name": name})

        data = cursor.fetchone()

        if data is None:
            return None

        user = User(**data)
        return user

    def save(self, user):
        sql = """insert into users (id, name, email, password) values (
            :id, :name, :email, :password
        ) """
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(
            sql,
            {
                "id": user.id,
                "name": user.name,
                "email": user.email,
                "password": user.password,
            },
        )
        conn.commit()
