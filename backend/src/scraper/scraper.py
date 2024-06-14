
import requests
from bs4 import BeautifulSoup
import json

url = "https://listado.mercadolibre.com.ar/notebooks#D[A:notebooks,on]"
response = requests.get(url)

def get_productos():
    productos_list = []  # Lista para almacenar datos de productos

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        productos = soup.find_all('div', class_="andes-card ui-search-result ui-search-result--core andes-card--flat andes-card--padding-16")
        
        for i, producto in enumerate(productos):
            if i < 10:  # Limita a los primeros 10 productos
                titulo = producto.find('h2', class_="ui-search-item__title").text.strip()
                precio = producto.find('span', class_="andes-money-amount__fraction").text.strip()

                image_container = producto.find('div', class_="andes-carousel-snapped__slide andes-carousel-snapped__slide--active")
                image_url = ""
                if image_container:
                    image = image_container.find('img', class_="ui-search-result-image__element")
                    if image and 'src' in image.attrs:
                        image_url = image['src']
                    elif image and 'data-src' in image.attrs:  # Para imágenes que cargan perezosamente
                        image_url = image['data-src']

                # Agrega el producto a la lista
                productos_list.append({"titulo": titulo, "precio": precio, "imagen": image_url})
            else:
                break  # Sale del bucle después de 10 productos

    return productos_list # Devuelve la lista de productos

print(get_productos())