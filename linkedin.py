import requests
import time
from bs4 import BeautifulSoup

#### LinkedIn Software Engineering Intern Job Board Parser ####

URL = "https://www.linkedin.com/jobs/search/?distance=25&keywords=software%20engineering%20intern"
r = requests.get(URL)
soup = BeautifulSoup(r.content, 'html5lib')

table = soup.find('article', attrs = {'id': 'JobResults'})

# Intializer used just to let the datas load.
companyName = []
loadingAgain = False
overkill = 0

while companyName == []:
    companyName = soup.find_all('h4', attrs={"class": "result-card__subtitle"}, limit=10)
    positionName = soup.find_all('a', attrs={"class": "result-card__full-card-link"}, limit=10)
    linkName = soup.find_all('a', attrs={"class": "result-card__full-card-link"}, href=True, limit=10)
    if companyName == []:
        if loadingAgain is False:
            print("Loading... (Automatically refreshing for a minute!)")
            loadingAgain = True
        else:
            if overkill == 5:
                print()
                print("Failed: Try run the program again later :(")
                break

            print("Loading... (Automatically refreshing for another minute!)")
        overkill += 1
        time.sleep(60)

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
    print(company_result[i])
    print()
    print(position_result[i])
    print()
    print(link_result[i])
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




