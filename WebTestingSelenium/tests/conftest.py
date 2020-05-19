"""
This module contains shared fixtures.
"""

import json
import pytest
import selenium.webdriver


@pytest.fixture

 def config(scope = 'session'):
 	'''The reason I've changed the scope is because I want to run this fixture only one time before the entire
 	test suite. We don't need to repeatedly read in the same config file over and over again for every single test.
 	That's a bit inefficient. And theoretically, if some dangerous party were to come along and change
 	your config file while the test suite runs, it could mess up your whole test suite.So, read it once, be efficient, and be safe.
 	'''

 	# Read the file
 	with open('config.json') as config_file:
    	config = json.load(config_file)
    	# json.load method to parse the textual content into a Python dictionary.

	# Assert values are acceptable
	assert config['browser'] in ['Firefox', 'Chrome', 'Headless Chrome']
	assert isinstance(config['implicit_wait'], int)
	assert config['implicit_wait'] > 0

	#The isinstance() function returns True if the specified object is of the specified type, otherwise False.

	# Return config so it can be used
	return config


@pytest.fixture

def browser(config):
	# Initialize the WebDriver instance
	if config['browser'] == 'Firefox':
		b = selenium.webdriver.Firefox()

	elif config['browser'] == 'Chrome':
		b = selenium.webdriver.Chrome()

	elif config['browser'] == 'Headless Chrome':
		opts = selenium.webdriver.ChromeOptions()
		opts.add_argument('headless')
		b = selenium.webdriver.Chrome(options=opts)

	else:
		raise Exception(f'Browser "{config["browser"]}" is not supported')
		# raise Exception('Broswer {} is not supported).format(config['browser'])')

	# Make its calls wait for elements to appear
	b.implicitly_wait(config['implicit_wait'])

	# Return the WebDriver instance for the setup
	yield b
	# We still yield the browser instance and we still quit at the end of a test.

	# Quit the WebDriver instance for the cleanup
	b.quit()