import re
import requests
from bs4 import BeautifulSoup


URL = "http://catalog.rpi.edu/content.php?catoid=24&navoid=587"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

#get rid of all &nbsp; characters in the html
soup.prettify(formatter=lambda s: s.replace(u'\xa0', ' '))

#Header style:
#<span style="mso-fareast-font-family:&quot;Times New Roman&quot;">School of Architecture</span>

# iterate through all the <tr> blocks using find_all('tr')
	# 
	# if text is empty then we don't append
result = soup.find_all('td', attrs={'colspan':'4', 'style':'height:16.8pt; width:458pt'})
print(result[0].text)
result = soup.find_all('td', attrs={'colspan':'4', 'style':'height:16.05pt; width:458pt'})
for i in result:
	print(i.text)

# <td colspan="4" style="height:16.8pt; width:458pt">