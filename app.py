import requests
from pages.quotes_pages import QuotesPage

page_content=requests.get('http://quotes.toscrape.com').content
page=QuotesPage(page_content)

for e in page.quotes:
    print(e)