from .task import Task
import os
import platform
import re
from termcolor import colored


class TodoList:
    def __init__(self):
        self._tasks: list[Task] = []
        self._menu_options = [
            {
                "call_input": ["1", "a"],
                "name": "Adicionar nova tarefa",
                "method": self._handle_add_task,
                "is_enabled": lambda s: True,
            },
            {
                "call_input": ["2", "m"],
                "name": "Marcar tarefa como concluída",
                "method": self._handle_mark_task_completed,
                "is_enabled": lambda s: bool(s._tasks),
            },
            {
                "call_input": ["3", "r"],
                "name": "Remover tarefa",
                "method": self._handle_remove_task,
                "is_enabled": lambda s: bool(s._tasks),
            },
            {
                "call_input": ["4", "s"],
                "name": "Sair",
                "method": self._handle_exit,
                "is_enabled": lambda s: True,
            },
        ]

    def _display_menu(self):
        print(" {:=^40} ".format("MENU"))
        for i, option in enumerate(self._menu_options):
            text = f"{i + 1} - {option['name']}"
            if not option["is_enabled"](self):
                text = colored(f"{text} (indisponível)", "dark_grey")
            print(text)

    def _handle_menu_input(self):
        user_input = input("Selecione a opção desejada: ")

        for option in self._menu_options:
            if user_input in option["call_input"]:
                if not option["is_enabled"](self):
                    return
                option["method"]()
                return

        raise ValueError(f"A opção '{user_input}' não é válida.")

    def _handle_add_task(self):
        description = input("Digite a descrição da tarefa: ")
        self._add_task(Task(description))

    def _add_task(self, task: Task):
        self._tasks.append(task)

    def _multiple_tasks_input(self) -> list[int]:
        task_numbers_str = input(
            "Digite os números das tarefas separados por espaço: "
        ).strip()
        task_numbers_str = re.sub(r"\s+", " ", task_numbers_str).split(" ")
        last_valid_tasks_index = len(self._tasks) - 1
        task_indexes = []

        for i in task_numbers_str:
            try:
                index = int(i) - 1
                if index < 0 or index > last_valid_tasks_index:
                    raise IndexError(f"A tarefa {i} está fora do intervalo válido.")
                if index in task_indexes:
                    print("A tarefa {i} já foi especificada; ignorando duplicata.")
                    continue
                task_indexes.append(index)
            except ValueError:
                raise ValueError(f"'{i}' Não é um número válido")
        task_indexes.sort(reverse=True)

        return task_indexes

    def _handle_mark_task_completed(self):
        indexes = self._multiple_tasks_input()
        for i in indexes:
            self._mark_task_completed(self._tasks[i])

    def _mark_task_completed(self, task: Task):
        task.is_completed = True

    def _handle_remove_task(self):
        task_indexes = self._multiple_tasks_input()
        confirmation_input = input(
            "Tem certeza que deseja excluir as tarefas especificadas? (S/N): "
        ).lower()

        if confirmation_input == "n" or confirmation_input == "":
            return
        elif confirmation_input != "s":
            raise ValueError("Opção inválida.")

        for i in task_indexes:
            self._remove_task(i)

    def _remove_task(self, task_index: int):
        self._tasks.pop(task_index)

    def _handle_exit(self):
        exit()

    def _get_tasks(self) -> list[Task]:
        return self._tasks

    def _list_tasks(self):
        if not self._tasks:
            return

        print(" {:=^40} ".format("TAREFAS"))
        for i, task in enumerate(self._tasks):
            task_completion_symbol = "[X]" if task.is_completed else "[ ]"
            print(f"{task_completion_symbol} {i + 1} - {task.description}")

    def _clear_console(self):
        if platform.system() == "Windows":
            os.system("cls")
        else:
            os.system("clear")

    def run(self):
        while True:
            self._clear_console()
            self._display_menu()
            self._list_tasks()
            self._handle_menu_input()
