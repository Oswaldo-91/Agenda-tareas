# Lista para almacenar las tareas
tareas = []

# Función para agregar una tarea
def agregar_tarea():
    tarea = input("Ingrese la tarea: ")
    tareas.append({'tarea': tarea, 'completada': False})
    print(f"Tarea '{tarea}' agregada.")

# Función para ver las tareas
def ver_tareas():
    if len(tareas) == 0:
        print("No hay tareas pendientes.")
    else:
        for i, tarea in enumerate(tareas):
            estado = "Completada" if tarea['completada'] else "Pendiente"
            print(f"{i + 1}. {tarea['tarea']} - {estado}")

# Función para marcar una tarea como completada
def completar_tarea():
    ver_tareas()
    try:
        tarea_id = int(input("Ingrese el número de la tarea que completó: ")) - 1
        if tarea_id >= 0 and tarea_id < len(tareas):
            tareas[tarea_id]['completada'] = True
            print(f"Tarea '{tareas[tarea_id]['tarea']}' completada.")
        else:
            print("Tarea no encontrada.")
    except ValueError:
        print("Por favor, ingrese un número válido.")

# Función principal que ejecuta el menú
if __name__ == "__main__":
    while True:
        print("\n--- Agenda de Tareas ---")
        print("1. Ver tareas")
        print("2. Agregar tarea")
        print("3. Completar tarea")
        print("4. Salir")
        opcion = input("Seleccione una opción (1-4): ")

        if opcion == '1':
            ver_tareas()
        elif opcion == '2':
            agregar_tarea()
        elif opcion == '3':
            completar_tarea()
        elif opcion == '4':
            print("Gracias por usar la Agenda de Tareas. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intente nuevamente.")
