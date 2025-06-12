from storage_manager.json_storage_manager import JSONStorageManager
from storage_manager.mysql_storage_manager import MySQLStorageManager
from todo_list.todo_list import TodoList


storage_manager = MySQLStorageManager()
todo_list = TodoList(storage_manager)
todo_list.run()
