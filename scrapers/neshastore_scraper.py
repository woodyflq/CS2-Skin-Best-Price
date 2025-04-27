from bs4 import BeautifulSoup
import requests

def coletar_skins_neshastore():
    # URL do site a ser feito scraping
    url = "https://neshastore.com"

    # Requisição da página
    response = requests.get(url)

    # Analisa o conteúdo HTML
    soup = BeautifulSoup(response.text, 'html.parser')

    # Encontre todos os cartões de item
    items = soup.find_all('div', class_='card')

    skins = []

    # Para cada item encontrado, colete os dados relevantes
    for item in items:
        # Nome da skin
        name = item.find('span', class_='mb-0 d-inline-block text-muted text-truncate undefined')
        if name:
            name = name.text.strip()
        else:
            name = None

        # Preço atual
        price = item.find('p', class_='font-weight-normal h2')
        if price:
            price = price.text.strip()
        else:
            price = None

        # Preço original (se houver)
        old_price = item.find('p', class_='text-danger font-weight-lighter h3')
        if old_price:
            old_price = old_price.text.strip()
        else:
            old_price = None

        # Link do item
        link = item.find('a', href=True)
        if link:
            link = link['href']
        else:
            link = None

        # Imagem da skin
        image_tag = item.find('img', class_='ng-tns-c16-51 ng-lazyloaded')
        if image_tag:
            image = image_tag['src']
        else:
            image = None  # Ou algum valor padrão caso a imagem não seja encontrada

        # Desconto
        discount = item.find('span', class_='font-weight-bold h2')
        if discount:
            discount = discount.text.strip()
        else:
            discount = None

        # Fase
        phase = item.find('span', class_='phase')
        if phase:
            phase = phase.text.strip()
        else:
            phase = None

        # Adiciona a skin no dicionário
        skins.append({
            'name': name,
            'price': price,
            'old_price': old_price,
            'link': link,
            'image': image,
            'discount': discount,
            'phase': phase
        })
    return(skins)
