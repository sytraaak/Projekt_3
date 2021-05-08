import sys
import bs4
import requests
import csv
#"https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=8&xnumnuts=5203"
def down(URL):
    STAZENI = requests.get(URL)
    SOUP = bs4.BeautifulSoup(STAZENI.text, 'html.parser')
    return SOUP

def odkazy(SOUP):
    SEZNAM_ODKAZU = []
    for link in SOUP.select("td.cislo a"):
        SEZNAM_ODKAZU.append("https://volby.cz/pls/ps2017nss/"+link["href"])
    return SEZNAM_ODKAZU

def cisla(SOUP):
    CISLA = []
    for cislo_ok in SOUP.select("td.cislo a"):
        CISLA.append(cislo_ok.get_text())
    return CISLA

def strany(SOUP, modifier):
    STRANY = []
    for strana in SOUP.select(f"div.t2_470 table tr td:nth-of-type({modifier})"):
        STRANY.append(strana.get_text())
    return STRANY

def nazvy(SOUP):
    NAZEV = []
    vsechny = SOUP.find_all("td", "cislo")
    for hledani in vsechny:
        NAZEV.append(hledani.find_next_sibling("td").get_text())
    return NAZEV

def scrapper(SEZNAM_ODKAZU):
    print("Spouštím stahování dat")
    header = ["Číslo obce", "Název obce", "Voliči v seznamu", "Vydané obálky", "Platné hlasy"]
    vysledky = []
    ind = 0
    for obec in SEZNAM_ODKAZU:
        udaje = []
        soup = down(webovka)
        nazev, cislo = nazvy(soup), cisla(soup)
        udaje.append(cislo[ind])
        udaje.append(nazev[ind])
        ind += 1
        SOUP_OBEC = down(obec)
        for i, element in enumerate(SOUP_OBEC.find_all("td", class_="cislo")):
            if i in (3,4,7):
                udaje.append(str(element.get_text()).replace(u'\xa0', u' '))
            elif i == 8:
                break
        for pocet_hlasu in strany(SOUP_OBEC, 3):
            udaje.append(pocet_hlasu)
        vysledky.append(udaje)
    SOUP_OBEC = down(obec)
    for strana in strany(SOUP_OBEC, 2):
        header.append(strana+" (počet hlasů)")
    vystup = (vysledky, header)
    return vystup

def zapis(vysledky):
    with open(f"{nazev}.csv", mode="w", newline="", encoding="utf-8") as soubor:
        zapisovac = csv.writer(soubor)
        zapisovac.writerow(vysledky[1])
        zapisovac.writerows(vysledky[0])

if __name__ == "__main__":
    try:
        webovka = sys.argv[1]
        nazev = sys.argv[2]
        vysledky = scrapper(odkazy(down(webovka)))
        print("Ukládám do souboru")
        zapis(vysledky)
        print(f"Dokončeno - soubor {sys.argv[2]}.csv")
    except:
        print("Nezadali jste správně argumenty")





