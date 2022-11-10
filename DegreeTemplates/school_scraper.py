import re
import requests
import json
from bs4 import BeautifulSoup

# site being scraped for schools and majors
URL = "http://catalog.rpi.edu/content.php?catoid=24&navoid=587"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")

# get rid of all '&nbsp;' characters in the html (no clue if this actually worked)
soup.prettify(formatter=lambda s: s.replace(u'\xa0', ' '))

# create list of <tr> blocks
table = soup.find_all("table", attrs={'border':'0'})[0]
blocks = table.find_all('tr')

#instantiate variable used for json dump
schools = []
current_school = ''

# iterate through all <tr> blocks which contain school-major information
for block in blocks:
	# find the intended information from scraper
	school = block.find('td', attrs = {'colspan':'4'})
	major = block.find('td', attrs = {'style':'height:16.05pt; width:266pt'})
	degrees = block.find('td', attrs = {'style': 'width:169pt'})
	
	# when find() runs into school block formatting
	if school:

		# populate json variable
		if re.sub(r'[0-9]', '', school.strong.span.text).strip() == "Information Technologyand Web Science":
			new_school = {}
			new_school['School Name'] = ["Information Technology and Web Science"]
			new_school['Majors'] = []
			schools.append(new_school)
			continue
		
		new_school = {}
		new_school['School Name'] = [re.sub(r'[0-9]', '', school.strong.span.text).strip()]
		new_school['Majors'] = []
		schools.append(new_school) 
	
	# when find() runs into major block formatting
	elif major:

		major_p = major.find_all('p')
		degrees_p = degrees.find_all('p')
		
		# case where the structure is a <p> block dividing multiple majors
		if major_p:
			for i in range(len(major_p)):
				if(degrees_p[i].text.find('B.') != -1): # change find string for other degrees
					schools[-1]['Majors'].append(major_p[i].text)
			continue
		
		# standard major output
		if degrees.text.find('B.') != -1: # change find string for other degrees
			schools[-1]['Majors'].append(major.text)
			# print(major.text.strip())

# dump scraped information into json file
with open("schools.json", "w") as write_file:
	json.dump(schools, write_file, sort_keys=False, indent=2, ensure_ascii=False)