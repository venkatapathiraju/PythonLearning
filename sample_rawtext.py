import urllib
from urllib import request
from bs4 import BeautifulSoup
url = 'https://en.wikipedia.org/wiki/Python_(programming_language)'
html_content = urllib.request.urlopen(url).read()
#print(html_content)
soup = BeautifulSoup(html_content,'html.parser')
n_links = soup.find_all('a')
print(len(n_links))
table = soup.find('table',{'class':'wikitable'})
rows = table.find_all('tr')
rows = rows[1:]
for row in rows:
    tags = row.find_all('td')
    print(tags[0].get_text())