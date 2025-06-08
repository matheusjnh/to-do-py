class Task:
    def __init__(self, description: str):
        self.description = description
        self._is_completed = False

    def get_completion_status(self) -> bool:
        return self._is_completed

    def change_completion_status(self, status: bool):
        self._is_completed = status
