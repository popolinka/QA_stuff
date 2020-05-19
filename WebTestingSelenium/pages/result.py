"""
This module contains DuckDuckGoResultPage,
the page object for the DuckDuckGo search result page.
"""

from selenium.webdriver.common.by import By



class DuckDuckGoResultPage:

    # Locators
    RESULT_LINKS = (By.CSS_SELECTOR, 'a.result__a')
    SEARCH_INPUT = (By.ID, 'search_form_input')

    # initializer
    def __init__(self, browser):
        self.browser = browser


    # Interaction Methods

    def result_link_titles(self):
    links = self.browser.find_elements(*self.RESULT_LINKS)
    titles = [link.text for link in links]
    return titles

    def search_input_value(self):
    '''Now instead of sending keys to this, I want to get the value from it.
    To do that, I'll need to use the get_attribute method and look for the attribute named “value” and
    ultimately, that's the text value that I'll want to return.

    Now you may be wondering, why did we use get_attribute instead of just the text property for the search_input element?
    Whenever you're dealing with text input elements where you can type something in,
    interestingly, the text property of that is going to be the empty string.
    You'll need to use the get_attribute of the value to get the value that the user typed in.
    Be careful, that usually trips up a lot of people.
    '''
    search_input = self.browser.find_element(*self.SEARCH_INPUT)
    value = search_input.get_attribute('value')
    return value

    def title(self):
        return self.browser.title