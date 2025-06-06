tasks = []


def show_menu():
    print(
        "To-do List Py\n\n"
        "=== MENU ===\n"
        "1 - Adicionar tarefa\n"
        "2 - Marcar como concluída\n"
        "3 - Remover tarefa\n"
        "4 - Sair"
    )


def list_tasks():
    if not tasks:
        return

    print("\n=== TAREFAS ATUAIS ===")

    for i in range(len(tasks)):
        task = tasks[i]
        task_completion_symbol = "[X]" if task["is_completed"] else "[ ]"
        print(f"{task_completion_symbol} {i + 1} - {task['description']} ")


while True:
    show_menu()
    list_tasks()

    option = input("\nSelecione a opção: ")

    if option == "1":
        task_description = input("Descrição da tarefa: ")
        tasks.append({"description": task_description, "is_completed": False})

    elif option == "2":
        task_index = int(input("Selecione a tarefa: ")) - 1
        tasks[task_index]["is_completed"] = True

    elif option == "3":
        print("opção 3")

    elif option == "4":
        break
