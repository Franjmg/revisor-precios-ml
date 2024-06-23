import src.scraper.scraper as scraper
import src.alerts.alerts as alerts


def menu():
    while True:

        print("\nMenú:")
        producto = scraper.obtener_nombre_producto("backend/nameproducto.json")
        print(f"El producto almacenado es {producto}")
        print("0. Actualizar productos")
        print("1. Ver productos")
        print("2. Comparar precios")
        print("3. Salir")
        opcion = input("Ingrese una opción: ")

        
        

        if opcion == "0":
            print("Ingrese nuevo producto:")
            productonuevo = input()
            scraper.guardar_nombre_producto(productonuevo, "backend/nameproducto.json")
            scraper.guardar_productos_json(scraper.get_productos_final(productonuevo), "backend/productos.json")
            print(scraper.leer_productos_json("backend/productos.json"))
            print("Productos actualizados.")

        elif opcion == "1":
            print(scraper.leer_productos_json("backend/productos.json"))

        elif opcion == "2":
            cambios = alerts.comparar_productos(producto)
            print(cambios)
            if cambios:
                alerts.enviar_cambios_email(cambios)
            else:
                print("No se encontraron cambios.")
        
        elif opcion == "3":
            break
    
menu()