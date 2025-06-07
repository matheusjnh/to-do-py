import os
import platform


def show_menu():
    print(
        "To-do List Py\n\n"
        "=== MENU ===\n"
        "\033[1m1\033[0m - \033[1mA\033[0mdicionar tarefa\n"
        "\033[1m2\033[0m - \033[1mM\033[0marcar como concluída\n"
        "\033[1m3\033[0m - \033[1mR\033[0memover tarefa\n"
        "\033[1m4\033[0m - \033[1mS\033[0mair"
    )


def list_tasks():
    if not tasks:
        return

    print("\n=== TAREFAS ATUAIS ===")

    for i in range(len(tasks)):
        task = tasks[i]
        task_completion_symbol = "[X]" if task["is_completed"] else "[ ]"
        print(f"{task_completion_symbol} {i + 1} - {task['description']} ")


def clear_console():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")


tasks = []

while True:
    clear_console()
    show_menu()
    list_tasks()

    option = input("\nSelecione a opção: ").lower()

    if option == "1" or option == "a":
        task_description = input("Descrição da tarefa: ")
        tasks.append({"description": task_description, "is_completed": False})

    elif option == "2" or option == "m":
        task_index = int(input("Selecione a tarefa: ")) - 1
        tasks[task_index]["is_completed"] = True

    elif option == "3" or option == "r":
        task_index = int(input("Qual tarefa você quer remover?: ")) - 1
        tasks.pop(task_index)

    elif option == "4" or option == "s":
        break
