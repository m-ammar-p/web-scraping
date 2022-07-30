from bs4 import BeautifulSoup
import requests

def find_price():
    html_text = requests.get("https://farmacie.md/ro/cosmetica/ingrijire-picioare//?sort-filters=title").text

    soup = BeautifulSoup(html_text, 'html.parser')

    products = soup.find_all('div', class_ = 'product__item__inner')

    for product in products:

        try:
            company_name = product.find('div', class_ = 'product__item__title').text
            price = product.find('div', class_ = 'product__item__price__current').text

            print(company_name)
            print(price)
        except Exception as e:
            print(e)






if __name__ == '__main__':
    find_price()