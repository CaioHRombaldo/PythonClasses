import requests
from bs4 import BeautifulSoup

website = requests.get('https://quotes.toscrape.com/')
soup = BeautifulSoup(website.text, 'html.parser')

quote = soup.find(class_='quote')
quote_text = quote.find(class_='text')
quote_author = quote.find(class_='author')

print(quote_text.text)
print(quote_author.text)