from pathlib import Path
from typing import Any
import json

from storage_manager.storage_manager_base import StorageManagerBase
from todo_list.task import Task


class JSONStorageManager(StorageManagerBase):
    def __init__(self):
        super().__init__()

        # Just a temporary way to specify the file path
        self._filePath = Path(
            r"C:\Users\TheuJnh\Desktop\dev\python\to-do-list\tasks.json"
        )
        print(self._filePath)

    def load(self) -> list[Task]:
        try:
            with open(self._filePath, "r") as f:
                data = json.load(f)
                return [self._deserialize_task(d) for d in data]
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def save(self, tasks: list[Task]) -> bool:
        data = [self._serialize_task(task) for task in tasks]
        with open(self._filePath, "w") as f:
            json.dump(data, f, indent=4)
        return True

    def _serialize_task(self, task: Task) -> dict[str, Any]:
        return {"description": task.description, "is_completed": task.is_completed}

    def _deserialize_task(self, data: dict) -> Task:
        return Task(data["description"], data["is_completed"])
