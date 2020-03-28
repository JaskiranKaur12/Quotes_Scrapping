from bs4 import BeautifulSoup

from locators.quote_locators import QuoteLocators
from locators.quotes_page_locators import QuotesPageLocators
from parsers.quote import QuoteParser

class QuotesPage:
    def __init__(self,page):
        self.soup=BeautifulSoup(page,'html.parser')

    @property
    def quotes(self):
        locator=QuotesPageLocators.QUOTE
        all_quotes=self.soup.select(locator)
        return [QuoteParser(e) for e in all_quotes]
