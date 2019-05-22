import requests
import time
import random
import sys
from bs4 import BeautifulSoup

#### Indeed Job Board Parser ####

# User enters their information and assigns it as variables
position = input("What positions are you looking for? \n")
location  = input("In which area? \n")
print()

# Reformats data into URL's syntax
URL = "https://www.indeed.com/jobs?q=" + position.replace(" ", "+") +"&l=" + location.replace(" ", "+")
print("Here is the Link to your search term: \n" + URL)
print()

# Utilizes BeautifulSoup Library to Parse Indeed.com
r = requests.get(URL)
soup = BeautifulSoup(r.content, 'html5lib')

# Intializer used just to let the datas load.
companyName = []
loadingAgain = False
overkill = 0
counter = 5

### MAXIMUM LIMIT: 18 ###
companyName = soup.find_all('span', attrs={"class": "company"}, limit=18)
positionName = soup.find_all('div', attrs={"class": "title"}, limit=18)
linkName = soup.find_all('a', attrs={"class": "jobtitle"}, href=True, limit=18)

# If program is unable to parse any data from the website, program will exit.
if companyName == []:
    print("Please run this program again in a few seconds!")
    sys.exit()

# Data sets
company_result = []
position_result = []
link_result = []


for tag in companyName:
    company_result.append(tag.get_text())

for tag in positionName:
    position_result.append(tag.get_text())

for tag in linkName:
    link_result.append(tag['href'])

for i in range(len(company_result)):
    print()
    print("Company " + str(i + 1) + ":")
    print("---------------------------------------------------------------------------")
    print(company_result[i].strip())
    print()
    print(position_result[i].strip())
    print()
    print("https://www.indeed.com" + link_result[i])
    print()
    print("===========================================================================")

## Prints company name, position and link in a list.
# print("Company:")
# print(company_result)
# print("==================================================================================================================")
# print("Position:")
# print(position_result)
# print("==================================================================================================================")
# print("Link:")
# print(link_result)




