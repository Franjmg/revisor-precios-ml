
import requests
from bs4 import BeautifulSoup
import json


def url_dinamica(producto):
    url = f"https://listado.mercadolibre.com.ar/{producto}#D[A:{producto}]"
    response = requests.get(url)
    return response


def get_productos(producto, itemclass):
    response = url_dinamica(producto)
    productos_list = []  # Lista para almacenar datos de productos

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        productos = soup.find_all('li', class_=itemclass)
        
        for i, producto in enumerate(productos):
            if i < 15:  # Limita a los primeros 15 productos
                
                titulo = producto.find('h2', class_="ui-search-item__title").text.strip()
                precio = producto.find('span', class_="andes-money-amount__fraction").text.strip()
                imagen = producto.find('img', class_="ui-search-result-image__element")['data-src']
                
                # Agrega el producto a la lista
                productos_list.append({"titulo": titulo, "precio": precio, "imagen": imagen})
            else:
                break  # Sale del bucle después de 10 productos
    else:
        print("Error al cargar la web, codigo", response.status_code)
    return productos_list

def get_productos_final(producto):
    itemclass =  "ui-search-layout__item shops__layout-item ui-search-layout__stack"
    lista = get_productos(producto, itemclass)
    if not lista: 
        lista = get_productos(producto, "ui-search-layout__item")
        return lista
    else:
        return lista

def leer_productos_json(ruta_archivo):
    try:
        with open(ruta_archivo, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return []  # Retorna una lista vacía si el archivo no existe
    
def guardar_productos_json(productos, ruta_archivo):
    with open(ruta_archivo, 'w', encoding='utf-8') as f:
        json.dump(productos, f, ensure_ascii=False, indent=4)

def guardar_nombre_producto(producto, ruta_archivo):
    with open(ruta_archivo, 'w', encoding='utf-8') as f:
        json.dump([{"nombre_producto": producto}], f, ensure_ascii=False)

def obtener_nombre_producto(ruta_archivo):
    with open(ruta_archivo, 'r') as archivo:
        productos = json.load(archivo)
    
    # Asumiendo que quieres la primera palabra del nombre del primer producto
    primer_producto = productos[0]  # Accede al primer producto
    nombre_primer_producto = primer_producto['nombre_producto']  # Accede al nombre
    primera_palabra = nombre_primer_producto.split()[0]  # Extrae la primera palabra
    return primera_palabra