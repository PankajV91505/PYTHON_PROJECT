# import requests

# response = requests.get('https://en.wikipedia.org/wiki/Web_scraping')
# print(response.status_code)

# import requests
# from bs4 import BeautifulSoup

# response = requests.get(
#     url="https://en.wikipedia.org/wiki/Web_scraping",
# )
# soup = BeautifulSoup(response.content, 'html.parser')

# title = soup.find(id="firstHeading")
# print(title.string)




# import requests
# from bs4 import BeautifulSoup
# import random

# response = requests.get(
#     url="https://en.wikipedia.org/wiki/Web_scraping",
# )
# soup = BeautifulSoup(response.content, 'html.parser')

# title = soup.find(id="firstHeading")
# print(title.content)

# # Get all the links
# allLinks = soup.find(id="bodyContent").find_all("a")
# random.shuffle(allLinks)
# linkToScrape = 0

# for link in allLinks:
#     # We are only interested in other wiki articles
#     if link['href'].find("/wiki/") == -1: 
#         continue

#     # Use this link to scrape
#     linkToScrape = link
#     break

# print(linkToScrape)


import requests
from bs4 import BeautifulSoup
import random

def scrapeWikiArticle(url):
    response = requests.get(
        url=url,
    )

    soup = BeautifulSoup(response.content, 'html.parser')

    title = soup.find(id="firstHeading")
    print(title.text)

    allLinks = soup.find(id="bodyContent").find_all("a")
    random.shuffle(allLinks)
    linkToScrape = 0

    for link in allLinks:
        # We are only interested in other wiki articles
        if link['href'].find("/wiki/") == -1: 
            continue

        # Use this link to scrape
        linkToScrape = link
        break

    scrapeWikiArticle("https://en.wikipedia.org" + linkToScrape['href'])

scrapeWikiArticle("https://en.wikipedia.org/wiki/Web_scraping")


