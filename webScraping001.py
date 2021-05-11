import requests
from bs4 import BeautifulSoup

website = requests.get('https://quotes.toscrape.com/')
# print(website.text)
soup = BeautifulSoup(website.text, 'html.parser')

title = soup.find('title')
print(title.text)

firstLink = soup.find('a')
print(firstLink.text)

firstQuote = soup.find(class_='text')
print(firstQuote.text)

links = soup.findAll('a')
for link in links:
    print(link.text)

quotes = soup.findAll(class_='text')
for quote in quotes:
    print(quote.text)
