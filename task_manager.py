import json
import os

#Archivo dónde guardaremos las tareas
TASKS_FILE = "tasks.json"

def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []
    return []

def save_tasks(tasks):
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f, indent=4)
        
def add_task(description):
    tasks = load_tasks()
    tasks.append({"description": description, "completed": False})
    save_tasks(tasks)
    print("Tarea añadida.")
    
def list_tasks():
    filter_tasks("todas")
    
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
    
    print(f"\nTareas {status_filter}:")
    for idx, task in enumerate(filtered):
        status = "Realizada" if task["completed"] else "Pendiente"
        print(f"{idx + 1}. {status} - {task['description']}")

def complete_task(index):
    tasks = load_tasks()
    if 0 <= index < len(tasks):
        tasks[index]["completed"] = True
        save_tasks(tasks)
        print("Tarea completada.")
    else:
        print("Índice inválido.")
        
def delete_task(index):
    tasks = load_tasks()
    if 0 <= index < len(tasks):
        removed = tasks.pop(index)
        save_tasks(tasks)
        print(f"Tarea eliminada: {removed['description']}")
    else:
        print("Índice inválido.")

def show_menu():
    print("\nGestor de tareas")
    print("\n1. Añadir tarea")
    print("\n2. Listar todas las tareas")
    print("\n3. Completar tarea")
    print("\n4. Eliminar tarea")
    print("\n5. Filtrar tareas")
    print("\n6. Salir")
    
while True:
    show_menu()
    choice = input("Elige una opción: ")
    
    if choice == "1":
        desc = input("Descripción de la tarea: ")
        add_task(desc)
        
    elif choice == "2":
        list_tasks()
        
    elif choice == "3":
        idx = int(input("Número de la tarea a completar: ")) - 1
        complete_task(idx)
        
    elif choice == "4":
        idx = int(input("Número de la tarea a eliminar: ")) - 1
        delete_task(idx)
        
    elif choice == "5":
        print("\nFiltrar por:")        
        print("1. Pendientes")        
        print("2. Completadas")        
        print("3. Todas")
        filter = input("Elige una opción: ")
        
        if filter == "1":
            filter_tasks("pendientes")
        elif filter == "2":
            filter_tasks("completadas")
        elif filter == "3":
            filter_tasks("todas")
        else:
            print("Opción inválida.") 
       
    elif choice == "6":
        print("Saliendo...")
        break

    else:
        print("Opción no válida.")