# web testing with Selenium Webdriver..

more of a OOP way of testing, instead of functional programming

! **Important** !
Make sure the necessary driver (Chromedriver (for Chrome), GeckoDriver (for Firefox)) is installed on your system PATH. AND make sure the driver version matches your _browser_ version

main reference here at [TAU] (https://testautomationu.applitools.com/selenium-webdriver-python-tutorial)

Notes:

- CSS Selectors in Selenium
e.g.
Element: <button class ="django_ok">OK</button>
This button element has a class instead of an id.
We could use a CSS selector to uniquely identify it. CSS selectors work the same in Selenium WebDriver as they do in CSS pages for web front-ends.
Here, we could use “button.django_ok” to select the button element with the “django_ok” class. Thus, its locator would be
(By.CSS_Selector, 'button.django_ok')

## Parallel Testing

Need to install pytest-xdist first, good thing you can both control multiple test threads on a single machine AND distribute with multiple machines.

`pipenv install pytest-xdist`

### Make sure
- tests are independent of one another
- tests should be able to run irrespective of their order
- no collisions, i.e. no access to shared data etc.
### would be cool if...
- better use smart waits over hard.sleeps
- Optimize navigation using direct URLs
- Call APIs instead of using screen interactions to populate test data

### to run the tests w/parallel testing
`pipenv run python -m pytest -n 3`

where: -n lets you run tests in parallel, and after -n, you give the number of threads you would like to run in parallel, e.g. 3
PS: A good way is to use number of parametrized tests as the number of threads, if not **too** many...

## how about parallel testing on several machines?
There is a cool service: Selenium Grid is a free, open source tool from the Selenium Project for running remote WebDriver sessions.

A grid has one hub that receives all requests, as well as multiple nodes with different browsers operating systems and versions. Automation can request a session with specific criteria from the hub and the hub will allocate an available session from one of its nodes.

**Selenium grid enables not only parallel testing but also multi config testing.** e.g. For example, tests running from a Windows machine could request sessions for Safari on a macOS machine.

2 ways to implement it:
- choose to set up your own instance and manage the infrastructure yourself.
- OR, pay for it as a service.
