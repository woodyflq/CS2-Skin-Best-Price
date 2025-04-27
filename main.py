from scrapers.neshastore_scraper import coletar_skins_neshastore
from scrapers.csmoney_scraper import coletar_skins_csmoney
# No futuro, importar também buff163_scraper, csfloat_scraper

def main():
    print("Iniciando coleta de skins...")

    # Coleta as skins do Neshastore
    skins_neshastore = coletar_skins_neshastore()
    print(f"Skins coletadas do Neshastore: {skins_neshastore}")

    # Coleta as skins do CS Money
    skins_csmoney = coletar_skins_csmoney()
    print(f"Skins coletadas do CS Money: {skins_csmoney}")

    # Aqui futuramente vamos:
    # - Juntar as skins dos outros sites
    # - Contar as mais frequentes
    # - Buscar preços
    # - Comparar preços
    # - Salvar resultados

if __name__ == "__main__":
    main()
