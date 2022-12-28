import sqlite3
from typing import Optional, Iterable

import aiosqlite


class ConnectionsFactory:
    """ This class creates connection to the db and returns it. """
    def __init__(self, db_path: str):
        self.path = db_path
        self.conn = None

    async def create(self) -> sqlite3.Connection:
        self.conn = await aiosqlite.connect(self.path)
        return self.conn

    async def __aenter__(self) -> sqlite3.Connection:
        await self.create()
        return self.conn

    async def __aexit__(self, exc_type, exc_val, exc_tb) -> None:
        await self.conn.close()


class DatabaseController:
    """ Class with the all methods to working with db. """
    def __init__(self, connection):
        self._conn = connection

    async def create_db(self) -> None:
        await self._conn.execute("""CREATE TABLE IF NOT EXISTS users(
        user_id INTEGER,
        username TEXT
        )""")

    async def add_user(self, user_id: int, username: str) -> None:
        async with self._conn.cursor() as cursor:
            await cursor.execute("INSERT INTO users VALUES (?, ?)", (user_id, username))

    async def get_user_by_id(self, user_id: int) -> Optional[sqlite3.Row]:
        async with self._conn.cursor() as cursor:
            await cursor.execute("SELECT * FROM users WHERE user_id=?", (user_id,))
            res = await cursor.fetchone()
        return res[0] if res else None

    async def get_all_users(self) -> Optional[Iterable[sqlite3.Row]]:
        async with self._conn.cursor() as cursor:
            await cursor.execute("SELECT * FROM users")
            res = await cursor.fetchall()
        return res

    async def commit(self) -> None:
        await self._conn.commit()

    async def disconnect(self) -> None:
        await self._conn.close()
