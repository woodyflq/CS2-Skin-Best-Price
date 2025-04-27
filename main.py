from scrapers.neshastore_scraper import coletar_skins_neshastore
from scrapers.csmoney_scraper import coletar_skins_csmoney
from scrapers.dashskins_scraper import coletar_skins_dashskins
import csv

def salvar_skins_csv(skins, caminho_csv='skins_data.csv'):
    with open(caminho_csv, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=skins[0].keys())
        writer.writeheader()
        writer.writerows(skins)

def main():
    print("Iniciando coleta de skins...")

    # Coleta as skins do Neshastore
    skins_neshastore = coletar_skins_neshastore()
    for skin in skins_neshastore:
        skin['site'] = 'Neshastore'

    # Coleta as skins do CS Money
    skins_csmoney = coletar_skins_csmoney()
    for skin in skins_csmoney:
        skin['site'] = 'CS.Money'

    # Coleta as skins da DashSkins
    skins_dashskins = coletar_skins_dashskins()
    for skin in skins_dashskins:
        skin['site'] = 'DashSkins'

    # Junta todas as skins
    todas_skins = skins_neshastore + skins_csmoney

    # Exibe no console
    print(f"Total de skins coletadas: {len(todas_skins)}")
    for skin in todas_skins:
        print(skin)

    # Salva em CSV
    if todas_skins:
        salvar_skins_csv(todas_skins)
        print(f"Skins salvas em 'skins_data.csv'")
    else:
        print("Nenhuma skin coletada.")

if __name__ == "__main__":
    main()
