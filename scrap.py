import requests
from bs4 import BeautifulSoup

URL = "https://in.indeed.com/jobs?q=java+js&l=mumbai"
PAGE = requests.get(URL)

soup = BeautifulSoup(PAGE.content, 'html.parser')

results = soup.find(id="resultsBodyContent")

jobs_elems = results.find_all('div',class_="jobsearch-SerpJobCard")

for jobs_elem in jobs_elems:
    # print(jobs_elem)

    title = jobs_elem.find('h2',class_="title")

    title_elem = title.find('a')['title']
    company_elem = jobs_elem.find('span', class_="company")

    if None in(title_elem,company_elem):
        continue

    print(title_elem,'==>',company_elem.text.strip())
    print()
    print()
