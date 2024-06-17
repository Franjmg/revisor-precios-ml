import src.scraper.scraper as scraper
import src.alerts.alerts as alerts


def menu():
    while True:
        print("1. Ver productos")
        print("2. Comparar precios")
        print("3. Salir")
        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            scraper.guardar_productos_json(scraper.get_productos(), "backend/productos.json")
            print(scraper.leer_productos_json("backend/productos.json"))

        elif opcion == "2":
            cambios = alerts.comparar_productos()
            print(cambios)
            if cambios:
                alerts.enviar_cambios_email(cambios)
            else:
                print("No se encontraron cambios.")
        
        elif opcion == "3":
            break
    
menu()