import requests
from bs4 import BeautifulSoup

def scrape_amazon(link):
    response = requests.get(link)
    soup = BeautifulSoup(response.text, 'html.parser')
    fruits = soup.find_all('a', {'class': 'a-link-normal s-no-outline'})
    vegetables = soup.find_all('a', {'class': 'a-link-normal s-no-outline'})

    fruits_details = []
    vegetables_details = []

    for fruit in fruits:
        name = fruit.find('span', {'class': 'a-size-mini'}).text
        price = fruit.find('span', {'class': 'a-offscreen'}).text
        fruits_details.append({'name': name, 'price': price})

    for vegetable in vegetables:
        name = vegetable.find('span', {'class': 'a-size-mini'}).text
        price = vegetable.find('span', {'class': 'a-offscreen'}).text
        vegetables_details.append({'name': name, 'price': price})

    return fruits_details, vegetables_details

if __name__ == '__main__':
    link = input('Enter the Amazon link: ')
    fruits_details, vegetables_details = scrape_amazon(link)
    print('Fruits details:')
    for detail in fruits_details:
        print(f'Name: {detail["name"]}, Price: {detail["price"]}')
    print('\nVegetables details:')
    for detail in vegetables_details:
        print(f'Name: {detail["name"]}, Price: {detail["price"]}')