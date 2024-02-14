# VERSION 1 - WORKING

from bs4 import BeautifulSoup
import requests

page_to_scrape = requests.get("http://quotes.toscrape.com")
soup = BeautifulSoup(page_to_scrape.content, 'html.parser')
quotes = soup.findAll("span", attrs={"class": "text"})
authors = soup.findAll("small", attrs={"class": "author"})

for quote, author in zip(quotes, authors):
    print(quote.text)
    print(author.text)

# VERSION 2 - WORKING, CATCHES ERRORS

from bs4 import BeautifulSoup
import requests

page_to_scrape = requests.get("http://quotes.toscrape.com")
soup = BeautifulSoup(page_to_scrape.content, 'html.parser')

# Find all quotes
quotes = soup.findAll("span", attrs={"class": "text"})

# Find all authors
authors = soup.findAll("small", attrs={"class": "author"})

# Check if both lists are non-empty before proceeding
if quotes and authors:
    for quote, author in zip(quotes, authors):
        print(quote.text)
        print(author.text)
else:
    print("No quotes or authors found.")