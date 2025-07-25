import json
import os
from colorama import init, Fore, Style

init(autoreset=True) # Reinicia el color en cada línea

msg_info = Fore.MAGENTA
msg_warning = Fore.YELLOW

# Archivo dónde guardaremos las tareas
TASKS_FILE = "tasks.json"

# Carga de los datos del archivo
def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []
    return []

# Guardado de los datos en el archivo
def save_tasks(tasks):
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f, indent=4)

# Se añade una nueva tarea
def add_task(description):
    tasks = load_tasks()
    tasks.append({"description": description, "completed": False})
    save_tasks(tasks)
    print(msg_info + "\nTarea añadida.")

# Hace una búsqueda con filtro
def filter_tasks(status_filter):
    tasks = load_tasks()
    filtered = []
    
    if status_filter == "pendientes":
        filtered = [t for t in tasks if not t["completed"]]  
    elif status_filter == "completadas":
        filtered = [t for t in tasks if t["completed"]]
    else:
        filtered = tasks
    
    if not filtered:
        print("\n" + msg_warning + "No hay tareas para mostar.")
        return False
    
    print("\n" + Fore.CYAN + f"Tareas ({status_filter}):\n")
    for idx, task in enumerate(filtered):
        status = Fore.GREEN + "Realizada" if task["completed"] else Fore.RED + "Pendiente"
        print(Fore.CYAN + f"{idx + 1}. {status}{Fore.WHITE} - {task['description']}")
    
    return True

# Completa una tarea
def complete_task(index):
    tasks = load_tasks()
    if 0 < index <= len(tasks):
        if tasks[index]["completed"] == True:
            print(msg_warning + "\nLa tarea ya está completada.")
        else:
            tasks[index]["completed"] = True
            print(msg_info + "\nTarea completada.")
        save_tasks(tasks)
    else:
        print(msg_warning + "\nÍndice inválido.")

# Elimina una tarea
def delete_task(index):
    tasks = load_tasks()
    if 0 <= index < len(tasks):
        removed = tasks.pop(index)
        save_tasks(tasks)
        print(msg_info + f"\nTarea eliminada: {removed['description']}")
    else:
        print(msg_warning + "\nÍndice inválido.")

# Edita una tarea
def edit_task(index):
    tasks = load_tasks()
    if 0 <= index < len(tasks):
        status = Fore.GREEN + "Realizada" if tasks[index]["completed"] else Fore.RED + "Pendiente"
        print(Fore.CYAN + f"{index + 1}. {status}{Fore.WHITE} - {tasks[index]['description']}")
        print("\n1. Editar estado.")
        print("\n2. Editar descripción.")
       
        choice = int(input("\n Introduce tu elección: "))       
        if choice == 1:
            print("\n" + Fore.GREEN + "1-Realizado" + Fore.WHITE + " | " + Fore.RED + "2-Pendiente")
            estado = int(input("\nNuevo estado (1/2): "))
            if estado == 1:
                tasks[index]["completed"] = True
                print("\n" + msg_info + "Estado actualizado.")
            elif estado == 2:
                tasks[index]["completed"] = False
                print("\n" + msg_info + "Estado actualizado.")
            else:
                print(msg_warning + "\nOpción no válida.")
        elif choice == 2:
            description = input("\nNueva descripción: ")
            tasks[index]["description"] = description
            print("\n" + msg_info + "Descripción actualizada.")
        else:
            print(msg_warning + "\nOpción no válida.")
        save_tasks(tasks)

# Limpia la pantalla
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

# Crea una pausa hasta presionar 'Enter'
def pause():
    input("\nPulse ENTER para volver al menú...")

# Muestra el menú principal
def show_menu():
    print(Style.BRIGHT + Fore.CYAN + "\nGestor de tareas")
    print("\n" + Fore.BLUE + "1." + Fore.WHITE + " Añadir tarea")
    print("\n" + Fore.BLUE + "2." + Fore.WHITE + " Listar todas las tareas")
    print("\n" + Fore.BLUE + "3." + Fore.WHITE + " Completar tarea")
    print("\n" + Fore.BLUE + "4." + Fore.WHITE + " Eliminar tarea")
    print("\n" + Fore.BLUE + "5." + Fore.WHITE + " Filtrar tareas")
    print("\n" + Fore.BLUE + "6." + Fore.WHITE + " Editar tarea")
    print("\n" + Fore.BLUE + "7." + Fore.WHITE + " Salir\n")

# Programa principal
while True:
    clear_screen()
    show_menu()
    choice = input("Elige una opción: ")
    clear_screen()
    
    if choice == "1":
        desc = input("Descripción de la tarea: ")
        add_task(desc)
        pause()
        
    elif choice == "2":
        filter_tasks("todas")
        pause()
        
    elif choice == "3":
        if filter_tasks("todas") == True:
            idx = int(input("\nNúmero de la tarea a completar: "))
            complete_task(idx - 1)
        pause()
        
    elif choice == "4":
        if filter_tasks("todas") == True:
            idx = int(input("\nNúmero de la tarea a eliminar: "))
            delete_task(idx - 1)
        pause()
        
    elif choice == "5":
        print("Filtrar por:\n")
        print("1. Pendientes")
        print("2. Completadas")
        print("3. Todas")
        filter = input("\nElige una opción: ")
        clear_screen()
        
        if filter == "1":
            filter_tasks("pendientes")
        elif filter == "2":
            filter_tasks("completadas")
        elif filter == "3":
            filter_tasks("todas")
        else:
            print(msg_warning + "Opción inválida.")
        pause()
       
    elif choice == "6":
        if filter_tasks("todas") == True:
            idx = int(input("\nNúmero de la tarea a editar: "))
            edit_task(idx - 1)
        pause()

    elif choice == "7":
        print(Style.BRIGHT + Fore.CYAN + "Gracias por usar nuestra aplicación.")
        break

    else:
        print(msg_warning + "Opción no válida.")
        pause()