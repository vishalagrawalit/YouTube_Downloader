import requests
from bs4 import BeautifulSoup
from prettytable import PrettyTable

url = "https://www.you" + "magic" + "tube.com/watch?v=SAcpESN_Fk4"

page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")
data = soup.find('div', class_="sv-download-links")
data = data.find_all('a')

columns = ["S.No", "Quality"]
table = PrettyTable(columns)

links = []
text = []

for i in range(len(data)):
    links.append(data[i]['href'])
    text.append(data[i].contents[0])

for i in range(len(text)):
    table.add_row([i+1, text[i]])
    
print(table)
