import requests
from bs4 import BeautifulSoup

def coletar_skins_dashskins():
    url = "https://dashskins.com.br/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Encontrar todos os listings de itens
    items = soup.find_all('div', class_='listing')

    skins = []

    for item in items:
        # Nome da skin
        name_tag = item.find('div', class_='title is-size-7 has-text-white-bis item-name')
        name = name_tag.text.strip() if name_tag else None

        # Preço com desconto
        price_tag = item.find('div', class_='title is-size-6 has-text-white-bis has-text-centered')
        price = None
        if price_tag:
            price_inner = price_tag.find('div')
            price = price_inner.text.strip() if price_inner else None

        # Preço original
        original_price_tag = item.find('div', class_='subtitle is-size-7 has-text-centered')
        original_price = None
        if original_price_tag:
            original_price_inner = original_price_tag.find('span')
            original_price = original_price_inner.text.strip() if original_price_inner else None

        # Link do produto
        link_tag = item.find_parent('a', href=True)
        link = f"https://dashskins.com.br{link_tag['href']}" if link_tag else None

        # Imagem do produto
        image_tag = item.find('img', class_='image')
        image = image_tag['src'] if image_tag else None

        # Desconto
        discount_tag = item.find('div', class_='tag is-green')
        discount = None
        if discount_tag:
            discount_span = discount_tag.find('span')
            discount = discount_span.text.strip() if discount_span else None

        # Monta o dicionário
        skins.append({
            'name': name,
            'price': price,
            'original_price': original_price,
            'link': link,
            'image': image,
            'discount': discount
        })

    return skins

# Teste rápido
if __name__ == "__main__":
    skins = coletar_skins_dashskins()
    for skin in skins:
        print(skin)
