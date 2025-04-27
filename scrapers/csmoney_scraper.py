import requests
from bs4 import BeautifulSoup

def coletar_skins_csmoney():
    url = "https://cs.money/pt/market/buy/"

    # Enviando uma requisição GET para obter o conteúdo da página
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Encontrando os elementos de skins com a classe "csm_9e4b7045"
    skins = soup.find_all('div', class_='csm_9e4b7045')

    # Lista para armazenar os dados das skins
    skins_data = []

    # Iterando pelos elementos encontrados para extrair as informações
    for skin in skins:
        skin_info = {}

        # Nome da skin
        name = skin.find('span', class_='csm_1f2324e6')
        if name:
            skin_info['name'] = name.text.strip()
        else:
            skin_info['name'] = None

        # Preço da skin
        price = skin.find('div', class_='csm_541445e7')
        if price:
            skin_info['price'] = price.text.strip()
        else:
            skin_info['price'] = None

        # Imagem da skin
        image = skin.find('img')
        if image and 'src' in image.attrs:
            skin_info['image'] = image.attrs['src']
        else:
            skin_info['image'] = None

        # Adiciona as informações coletadas à lista de skins
        skins_data.append(skin_info)

    # Exibindo os resultados
    for skin in skins_data:
        print(f"Nome: {skin['name']}, Preço: {skin['price']}, Imagem: {skin['image']}")

    return skins_data