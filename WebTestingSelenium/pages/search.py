"""
This module contains DuckDuckGoSearchPage,
the page object for the DuckDuckGo search page.
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class DuckDuckGoSearchPage:
	# Link
	URL = 'https://www.duckduckgo.com'

	# Locator
	SEARCH_INPUT = (By.ID, 'search_form_input_homepage')

	# Initializer
	def __init__(self, browser):
    	self.browser = browser
	

	# Interaction Methods
	def load(self):
		browser.get(self.URL)
    # TODO

	def search(self, phrase):
    	search_input = browser.find_element(*self.SEARCH_INPUT)
    	search_input.send_keys(phrase + Keys.return)

    	# Well, the find_element method takes two arguments — the locator type and then the query — 
    	# but SEARCH_INPUT is a tuple
		# This asterisk is a standard Python thing that will expand tuples into positional 
		# arguments that can be passed into methods.

		#I'll also want to add on the Keys.RETURN. That comes from that import we saw before.
		# The return key will essentially commit that search and then proceed to start loading the search results page.
 		