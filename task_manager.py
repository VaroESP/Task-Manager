import json
import os

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
    print("\nTarea añadida.")

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
        print("No hay tareas para mostar.")
        return
    
    print(f"Tareas ({status_filter}):\n")
    for idx, task in enumerate(filtered):
        status = "Realizada" if task["completed"] else "Pendiente"
        print(f"{idx + 1}. {status} - {task['description']}")

# Completa una tarea
def complete_task(index):
    tasks = load_tasks()
    if 0 <= index < len(tasks):
        if tasks[index]["completed"] == True:
            print("\nLa tarea ya está completada.")
        else:
            tasks[index]["completed"] = True
            print("\nTarea completada.")
        save_tasks(tasks)
        
    else:
        print("\nÍndice inválido.")

# Elimina una tarea
def delete_task(index):
    tasks = load_tasks()
    if 0 <= index < len(tasks):
        removed = tasks.pop(index)
        save_tasks(tasks)
        print(f"\nTarea eliminada: {removed['description']}")
    else:
        print("\nÍndice inválido.")

# Limpia la pantalla
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

# Crea una pausa hasta presionar 'Enter'
def pause():
    input("\nPulse ENTER para volver al menú...")

# Muestra el menú principal
def show_menu():
    print("Gestor de tareas")
    print("\n1. Añadir tarea")
    print("\n2. Listar todas las tareas")
    print("\n3. Completar tarea")
    print("\n4. Eliminar tarea")
    print("\n5. Filtrar tareas")
    print("\n6. Salir\n")

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
        filter_tasks("todas")
        idx = int(input("\nNúmero de la tarea a completar: ")) - 1
        complete_task(idx)
        pause()
        
    elif choice == "4":
        filter_tasks("todas")
        idx = int(input("\nNúmero de la tarea a eliminar: ")) - 1
        delete_task(idx)
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
            print("Opción inválida.")
        pause()
       
    elif choice == "6":
        print("Saliendo...")
        break

    else:
        print("Opción no válida.")
        pause()