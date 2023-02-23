# lxml = remplace html.parser car plus rapide
from bs4 import BeautifulSoup
import pandas as pd
import requests
import lxml
from MusicItem import MusicItem

baseUrl = 'https://www.music3000.fr'
uri = "/34-guitare-electro-acoustique?page="
finalUrl = baseUrl + uri
pageNb = 51


# Parse la page et récupérer le code HTML
def swoup(url):
    response = requests.get(url)
    return BeautifulSoup(response.text, 'lxml')


# Récupération des liens en fonction de la range de la page donnée et de l'url de base
def get_links():
    urls = []
    for page in range(pageNb):
        urls.append(finalUrl + str(page))
    return urls


# Récupérer chaque lien par carte dans la liste cards
def get_links_from_cards(cards):
    links = []
    for card in cards:
        card_href = card.find("div", class_="img_block col-xs-5 col-sm-5 col-md-4").find("a")['href']
        links.append(card_href)
    return links


# Récupérer le lien de l'img
def get_img(soup):
    img_href = soup.find("img", class_="js-qv-product-cover")["src"]
    return img_href


# Récupérer la marque
def get_brand(soup):
    brand = soup.find("img", class_="brand-picture-desc")["src"]
    return brand


# Récupérer le modèle
def get_model(soup):
    model = soup.find("h1", class_="h1 namne_details").text
    return model


# Récupérer le prix
def get_price(soup):
    price = soup.find("span", class_="price").text
    return price


# Récupérer le description
def get_description(soup):
    description = soup.find("div", class_="product-desc").text
    return description


# Récupérer les infos de chaque page
def get_info_by_page(link):
    soup = swoup(link)
    img = get_img(soup)
    brand = get_brand(soup)
    model = get_model(soup)
    price = get_price(soup).replace(" ", "")
    description = get_description(soup).replace('\n', ' ').strip()

    return MusicItem(img, brand, model, price, description)


# Formater les données
def format_music(music_items):
    music_data = []
    for instrument in music_items:
        if instrument:
            instrument_dict = {
                'Image Link': instrument.get_img(),
                'Brand Image Link': instrument.get_brand(),
                'Model': instrument.get_model(),
                'Price': instrument.get_price(),
                'Description': instrument.get_description()
            }
            music_data.append(instrument_dict)

    return music_data


# Lancer le programme principal
def main():
    music_items = []
    urls = get_links()
    links = []
    for page in urls:
        soup = swoup(page)
        cards = soup.findAll("div", class_="item-product col-xs-12")
        links.extend(get_links_from_cards(cards))

    for link in links:
        music_items.append(get_info_by_page(link))

    music_items = format_music(music_items)
    data_frame = pd.DataFrame(music_items)
    # data_frame = csvUtils.sanitiseDupes(data_frame, 'Model')
    data_frame.to_csv("music_data.csv")


main()
