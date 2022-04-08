import requests
from bs4 import BeautifulSoup as soup


# scrape data from the F1 website
def WebScrape(calendar, category):

    website = "https://www.formula1.com/en/results.html/{}/{}.html".format(calendar, category)
    rec = requests.get(website)
    site_html = rec.text
    scrape = soup(site_html, 'html.parser')
    table = soup.select(scrape, "tbody>tr")

    return table