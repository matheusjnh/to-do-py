from abc import ABC, abstractmethod

from todo_list.task import Task


class StorageManagerBase(ABC):
    @abstractmethod
    def load(self) -> list[Task]:
        pass

    @abstractmethod
    def save(self, tasks: list[Task]) -> bool:
        pass
