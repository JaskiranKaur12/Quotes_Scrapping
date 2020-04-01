from selenium import webdriver

from pages.quotes_pages import QuotesPage, InvalidTagForAuthorError

try:
    author=input("Enter the author name: ")
    tag= input("Enter the tag name")

    chrome=webdriver.Chrome(executable_path="C:\\Users\\Jaski\\eclipse-workspace\\Seleniumpractice\\src\\drivers\\chromedriver.exe")
    chrome.get('http://quotes.toscrape.com/search.aspx')
    page=QuotesPage(chrome)

    print(page.search_for_quotes(author, tag))
except InvalidTagForAuthorError as e:
    print(e)
except Exception as e:
    print(e)
    print("An Invalid error occurred...Please try again.")


# author=input(" Enter the author name: ")
# page.select_author(author)
#
# tags=page.get_available_tags()
# print("Select one of these tags:[{}]".format(" | ".join(tags)))
# selected_tag=input("Enter your tag")
#
# page.select_tag(selected_tag)
# page.search_button.click()


