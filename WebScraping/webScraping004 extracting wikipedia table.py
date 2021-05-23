import requests
from bs4 import BeautifulSoup
import csv

website = requests.get('https://pt.wikipedia.org/wiki/Lista_de_pa%C3%ADses_por_popula%C3%A7%C3%A3o')
soup = BeautifulSoup(website.text, 'html.parser')
csv_data = [['rank', 'name', 'population', 'date', 'source']]

first_element = soup.select_one('.wikitable')
table_rows = first_element.select('tr')[1:]
for row in table_rows:
    table_data = row.select('td')
    rank = table_data[0].text.strip()
    name = table_data[1].text.strip()
    population = table_data[2].text.strip()
    date = table_data[3].text.strip()
    source = table_data[4].text.strip()
    csv_data.append([rank, name, population, date, source])

with open('countries_population.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerows(csv_data)
