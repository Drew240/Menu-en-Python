def agregar_nombre(nombre):
    try:
        with open("nombres.txt", "a") as archivo:
            archivo.write(nombre + "\n")
        print("Nombre agregado correctamente.")
    except IOError:
        print("Error al escribir en el archivo.")

def mostrar_nombres():
    try:
        with open("nombres.txt", "r") as archivo:
            nombres = archivo.readlines()
            if nombres:
                for i, nombre in enumerate(nombres):
                    print(f"Línea {i+1}: {nombre.strip()}")
            else:
                print("No hay nombres guardados.")
    except IOError:
        print("Error al leer el archivo.")

def buscar_nombre(nombre_a_buscar):
    try:
        with open("nombres.txt", "r") as archivo:
            for i, linea in enumerate(archivo):
                if nombre_a_buscar in linea:
                    print(f"El nombre '{nombre_a_buscar}' se encuentra en la línea {i+1}")
                    return
            print(f"El nombre '{nombre_a_buscar}' no se encontró.")
    except IOError:
        print("Error al buscar el nombre.")

def menu():
    while True:
        print("\nMenú:")
        print("1. Agregar nombre")
        print("2. Mostrar nombres")
        print("3. Buscar un nombre")
        print("4. Salir")

        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            nombre = input("Ingrese el nombre: ")
            agregar_nombre(nombre)
        elif opcion == "2":
            mostrar_nombres()
        elif opcion == "3":
            nombre_a_buscar = input("Ingrese el nombre a buscar: ")
            buscar_nombre(nombre_a_buscar)
        elif opcion == "4":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida.")

menu()