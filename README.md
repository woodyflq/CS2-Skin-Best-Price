
# CS2 Skin Best Price Tracker

Projeto em python para coletar e comparar preços de skins de CS2 de múltiplos sites, como **Neshastore** e **CS Money**. O objetivo é reunir os preços e mostrar a melhor opção para o usuário. O programa utiliza **BeautifulSoup** e **Requests** para fazer scraping das páginas.

---

## Funcionalidades

- Coleta de dados de skins de sites como **Neshastore** e **CS Money**.
- Para cada skin, são retornados: **nome**, **preço atual**, **imagem** e **link**.
- Coleta múltiplas skins de diferentes sites e as organiza para futuras comparações de preços.
- A possibilidade de adicionar novos sites de coleta (como **buff163** e **csfloat**) futuramente.

---

## Backend (Python + BeautifulSoup + Requests)

### Pré-requisitos

- [Instale o Python](https://www.python.org/downloads/) caso ainda não tenha instalado.
- Instale as dependências:
  ```bash
  pip install beautifulsoup4 requests
  ```

### Instruções

1. Clone o repositório:
   ```bash
   git clone https://github.com/woodyflq/CS2-Skin-Best-Price.git
   ```

2. Acesse a pasta do projeto:
   ```bash
   cd CS2-Skin-Best-Price
   ```

3. Execute o script de coleta de skins:
   ```bash
   python scraper.py
   ```

> O script fará a coleta e imprimirá as skins no console, com nome, preço e imagem.

---

## Estrutura do Projeto

```
CS2-Skin-Best-Price/
├── scrapers/
│   ├── neshastore_scraper.py
│   ├── csmoney_scraper.py
│   └── buff163_scraper.py (futuro)
├── scraper.py
└── README.md
```

---

## Como usar

1. Execute o script `scraper.py` para coletar as skins dos sites configurados.
2. As informações sobre as skins coletadas serão exibidas no console.
3. No futuro, o sistema permitirá a comparação de preços entre as skins de diferentes sites.

---

## Expansão Futura

- Adicionar novos sites de coleta (ex: **buff163**, **csfloat**).
- Implementar uma interface de comparação de preços.
- Armazenar os dados coletados em um banco de dados ou arquivo para facilitar consultas futuras.
