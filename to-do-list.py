from pathlib import Path
from storage_manager.json_storage_manager import JSONStorageManager
from storage_manager.mysql_storage_manager import MySQLStorageManager
from todo_list.todo_list import TodoList
from dotenv import load_dotenv
import os

load_dotenv()

# MYSQL STORAGE MANAGER
mysql_storage_manager = MySQLStorageManager(
    host=os.getenv("HOST"),
    user=os.getenv("USER"),
    passwd=os.getenv("PASSWD"),
    database=os.getenv("DATABASE"),
)

# JSON STORAGE MANAGER
json_storage_manager = JSONStorageManager(Path(os.getenv("JSON_FILE_PATH")))

todo_list = TodoList(json_storage_manager)
todo_list.run()
