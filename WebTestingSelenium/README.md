web testing with Selenium Webdriver..

more of a OOP way of testing, instead of functional programming

! Important !
Make sure the necessary driver (Chromedriver (for Chrome), GeckoDriver (for Firefox)) is installed on your system PATH. AND make sure the driver version matches your _browser_ version


main reference:
https://testautomationu.applitools.com/selenium-webdriver-python-tutorial

Notes:

- CSS Selectors in Selenium
e.g.
Element: <button class ="django_ok">OK</button>
This button element has a class instead of an id.
We could use a CSS selector to uniquely identify it. CSS selectors work the same in Selenium WebDriver as they do in CSS pages for web front-ends.
Here, we could use “button.django_ok” to select the button element with the “django_ok” class.

thus, its locator would be
(By.CSS_Selector, 'button.django_ok')