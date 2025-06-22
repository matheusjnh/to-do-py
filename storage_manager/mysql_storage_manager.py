import mysql.connector

from storage_manager.storage_manager_base import StorageManagerBase
from todo_list.task import Task


class MySQLStorageManager(StorageManagerBase):
    def __init__(self, host: str, user: str, passwd: str, database: str):
        super().__init__()

        self._db = mysql.connector.connect(
            host=host, user=user, passwd=passwd, database=database
        )

    def load(self) -> list[Task]:
        cursor = self._db.cursor()
        try:
            cursor.execute("SELECT description, is_completed FROM tasks")
            return [
                Task(description, is_completed) for description, is_completed in cursor
            ]
        except mysql.connector.Error as e:
            print(f"Erro ao carregar tarefas: {e}")
        finally:
            cursor.close()

    def save(self, tasks: list[Task]) -> bool:
        cursor = self._db.cursor()
        try:
            cursor.execute("TRUNCATE TABLE tasks;")
            cursor.executemany(
                "INSERT INTO tasks (description, is_completed) VALUES (%s, %s)",
                [(t.description, int(t.is_completed)) for t in tasks],
            )
            self._db.commit()
            return True
        except mysql.connector.Error as e:
            print(f"Erro ao salvar tarefas: {e}")
        finally:
            cursor.close()
