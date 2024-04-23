from gestortareas.gestor_tareas import GestorTareas

def mostrar_menu():
    print("\nMenu:")
    print("1. Agregar tarea")
    print("2. Eliminar tarea")
    print("3. Completar tarea")
    print("4. Ver tareas pendientes")
    print("5. Salir")

def main():
    gestor = GestorTareas()
    while True:
        mostrar_menu()
        opcion = input("Ingrese el número de la opción que desea: ")

        if opcion == "1":
            nombre_tarea = input("Ingrese el nombre de la tarea que desea agregar: ")
            gestor.agregar_tarea(nombre_tarea)
            print("Tarea agregada correctamente.")
        elif opcion == "2":
            nombre_tarea = input("Ingrese el nombre de la tarea que desea eliminar: ")
            gestor.eliminar_tarea(nombre_tarea)
            print("Tarea eliminada correctamente.")
        elif opcion == "3":
            nombre_tarea = input("Ingrese el nombre de la tarea que desea completar: ")
            gestor.completar_tarea(nombre_tarea)
            print("Tarea completada correctamente.")
        elif opcion == "4":
            tareas_pendientes = gestor.ver_tareas_pendientes()
            if tareas_pendientes:
                print("Tareas pendientes:")
                for tarea in tareas_pendientes:
                    print("-", tarea)
            else:
                print("No hay tareas pendientes.")
        elif opcion == "5":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, ingrese un número válido.")

if __name__ == "__main__":
    main()
