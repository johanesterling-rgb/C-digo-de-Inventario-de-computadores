def agregar_equipo(inventario):
    # Pedir los datos al usuario
    print("\n--- REGISTRAR EQUIPO ---")
    serial = input("Serial/ID: ")
    marca = input("Marca: ")
    modelo = input("Modelo: ")
    procesador = input("Procesador: ")
    ram = input("Memoria RAM (GB): ")
    disco = input("Capacidad Disco (GB): ")

    # Crear un diccionario con la información
    nuevo_pc = {
        "serial": serial,
        "marca": marca,
        "modelo": modelo,
        "procesador": procesador,
        "ram": ram,
        "disco": disco,
        "estado": "Disponible"
    }

    # Guardar el diccionario en la lista general
    inventario.append(nuevo_pc)
    print("Equipo guardado correctamente.")


def listar_equipos(inventario):
    # Recorrer la lista y mostrar cada equipo
    print("\n--- LISTA DE INVENTARIO ---")
    if len(inventario) == 0:
        print("No hay equipos registrados.")
        return

    for equipo in inventario:
        print(f"ID: {equipo['serial']} | {equipo['marca']} {equipo['modelo']}")
        print(f"RAM: {equipo['ram']}GB | Disco: {equipo['disco']}GB | Estado: {equipo['estado']}")
        print("-" * 30)


def cambiar_estado(inventario):
    # Buscar un equipo por su serial para cambiar su estado
    id_buscar = input("Ingrese el serial del equipo: ")

    for equipo in inventario:
        if equipo["serial"] == id_buscar:
            print("1. Disponible / 2. Asignado / 3. Mantenimiento")
            op = input("Seleccione el nuevo estado: ")

            if op == "1":
                equipo["estado"] = "Disponible"
            elif op == "2":
                equipo["estado"] = "Asignado"
            elif op == "3":
                equipo["estado"] = "Mantenimiento"

            print("Estado actualizado con éxito.")
            return

    print("Error: No se encontró un equipo con ese serial.")


def main():
    # Lista principal que actuará como base de datos
    inventario_computadores = []

    while True:
        # Menú principal de navegación
        print("\nSISTEMA DE INVENTARIO")
        print("1. Agregar computador")
        print("2. Listar inventario")
        print("3. Cambiar estado de equipo")
        print("4. Salir")

        opcion = input("Elija una opción: ")

        if opcion == "1":
            agregar_equipo(inventario_computadores)
        elif opcion == "2":
            listar_equipos(inventario_computadores)
        elif opcion == "3":
            cambiar_estado(inventario_computadores)
        elif opcion == "4":
            print("Cerrando sistema...")
            break
        else:
            print("Opción no válida.")


# Iniciar el programa
if __name__ == "__main__":
    main()
