from todo_list import TodoList
from storage_manager import JSONStorageManager

storage_manager = JSONStorageManager()
todo_list = TodoList(storage_manager)
todo_list.run()
