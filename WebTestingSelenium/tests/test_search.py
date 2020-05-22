"""
These tests cover DuckDuckGo searches.
"""

from pages.result import DuckDuckGoResultPage
from pages.search import DuckDuckGoSearchPage
# from selenium.web.driver.support.ui import WebDriverWait
# from selenium.web.driver.support import expected_conditions as EC
# NOTE: Using explict waits would imply that we should rid of all implicit waits, and make 'em all explicit. see config.json

def test_basic_duckduckgo_search(browser):

	search_page = DuckDuckGoSearchPage(browser)
	result_page = DuckDuckGoResultPage(browser)

	Phrase = 'Popolin'

    # Given the DuckDuckGo home page is displayed
    search_page.load()

    # When the user searches for "panda"
    search_page.search(Phrase)

    # And the search result query is "panda"
    assert Phrase == result_page.search_input_value()

    # And the search result links pertain to "panda"
    titles = result_page.result_link_titles()
    matches = [t for t in titles if Phrase.lower() in t.lower]
    assert len(matches) >0 

    # Then the search result title contains "panda"
    # changed the order, bc. of race condition on Firefox - title loading a bit late
    # WebDriverWait(driver, 10).until(EC.title_contains(Phrase))
    # explicit wait case
    assert Phrase == result_page.title()