import requests
import time
import random
import sys
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
counter = 5

## While loop algorithm doesn't work :(
# while companyName == []:
#     companyName = soup.find_all('h4', attrs={"class": "result-card__subtitle"}, limit=10)
#     positionName = soup.find_all('a', attrs={"class": "result-card__full-card-link"}, limit=10)
#     linkName = soup.find_all('a', attrs={"class": "result-card__full-card-link"}, href=True, limit=10)

#     print(companyName)

#     if companyName == []:

#         if loadingAgain is False:
#             print("Loading... (Please wait!)")
#             time.sleep(counter)
#             loadingAgain = True

#         else:
#             if overkill < 5:
#                 print("Loading... (Just a bit more!)")
#             else:
#                 print("Loading... (It's getting there!)")

#             if overkill == 10:
#                 print()
#                 print("FAILED: Try run the program again later :(")
#                 break

#             time.sleep(counter)
#         counter += random.randint(1, 5)
#         overkill += 1

### MAXIMUM LIMIT: 25 ###
companyName = soup.find_all('h4', attrs={"class": "result-card__subtitle"}, limit=25)
positionName = soup.find_all('a', attrs={"class": "result-card__full-card-link"}, limit=25)
linkName = soup.find_all('a', attrs={"class": "result-card__full-card-link"}, href=True, limit=25)

if companyName == []:
    print("URL Request Overload: Please run this program again in a few seconds!")
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




