import requests
from bs4 import BeautifulSoup

#### LinkedIn Software Engineering Intern Job Board Parser ####

URL = "https://www.linkedin.com/jobs/search/?distance=25&keywords=software%20engineering%20intern"
r = requests.get(URL)
soup = BeautifulSoup(r.content, 'html5lib')

table = soup.find('article', attrs = {'id': 'JobResults'})

final = []

companyName = soup.find_all('a', attrs={"class": "job-result-card__subtitle-item"}, limit=10)

results = []

for tag in companyName:
    results.append(tag.get_text())

print(results)

