import requests
from bs4 import BeautifulSoup

url= "https://listado.mercadolibre.com.ar/notebooks#D[A:notebooks,on]"

response = requests.get(url)


def get_productos():
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        productos = soup.find_all('div', class_="andes-card ui-search-result ui-search-result--core andes-card--flat andes-card--padding-16")
    
        for producto in productos:
            titulo = producto.find('h2', class_="ui-search-item__title")
            image = producto.find('img', class_="ui-search-result-image__element")
            precio = producto.find('span', class_="andes-money-amount__fraction")

            if titulo:
                print(titulo.text.strip())
            if image:
                print(image['src'])
            if precio:
                print(precio.text.strip())
    else:
        print("Error al cargar la web, codigo", response.status_code)

get_productos()