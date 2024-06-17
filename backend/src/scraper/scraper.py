
import requests
from bs4 import BeautifulSoup
import json


url = "https://listado.mercadolibre.com.ar/notebooks#D[A:notebooks]"
response = requests.get(url)

def get_productos():
    productos_list = []  # Lista para almacenar datos de productos

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        productos = soup.find_all('li', class_="ui-search-layout__item shops__layout-item ui-search-layout__stack")
        
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

def leer_productos_json(ruta_archivo):
    try:
        with open(ruta_archivo, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return []  # Retorna una lista vacía si el archivo no existe
    
def guardar_productos_json(productos, ruta_archivo):
    with open(ruta_archivo, 'w', encoding='utf-8') as f:
        json.dump(productos, f, ensure_ascii=False, indent=4)