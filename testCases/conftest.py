import os
from datetime import datetime
from pathlib import Path

import pytest
from selenium import webdriver


import pytest
from selenium import webdriver
from selenium.webdriver import FirefoxOptions

@pytest.fixture()
def driver(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome()
        print("Launching Chrome browser.........")
    elif browser == 'firefox':
        firefox_options = FirefoxOptions()
        firefox_options.binary_location = '/opt/firefox/firefox'
        firefox_options.add_argument('--headless')

        driver = webdriver.Firefox(options=firefox_options)
        driver.implicitly_wait(30)
        # driver = webdriver.Firefox()
        print("Launching Firefox browser.........")
    else:
        driver = webdriver.Chrome()  # Default to Chrome if no browser specified
        print("Launching Chrome browser as default.........")
    yield driver
    driver.quit()

def pytest_addoption(parser):  # This will get the value from CLI / hooks
    parser.addoption("--browser", action="store", default="chrome", help="Type in browser name e.g. chrome or firefox")

@pytest.fixture()
def browser(request):  # This will return the Browser value to setup method
    return request.config.getoption("--browser")


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    now = datetime.now()
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "driver":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            test_name = item.nodeid.split("::")[-1]
            # Construct the file_name including the test method name
            file_name = f"{test_name}_Failed_{now.strftime('%H%M%d%m%Y')}.png"
            screenshot_path = str(Path('Screenshots', file_name))

            driver = item.funcargs.get('driver', None)
            if driver:
                capture_screenshot(driver, screenshot_path)
                if screenshot_path:
                    # Construct complete file path
                    screenshot_full_path = os.path.abspath(screenshot_path)

                    # Construct HTML to display the screenshot
                    html = f'<div><a href="file://{screenshot_full_path}" target="_blank"><img src="file://{screenshot_full_path}" alt="Screenshots" style="width:304px;height:228px;" align="right"/></a></div>'

                    extra.append(pytest_html.extras.html(html))

                report.extra = extra


def capture_screenshot(driver, name):
    driver.get_screenshot_as_file(name)

def pytest_html_report_title(report):
    report.title = "InLynk Automation Report"

@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    now = datetime.now()
    report_dir = Path('Reports', now.strftime("%H%M%d%m%Y"))
    report_dir.mkdir(parents=True, exist_ok=True)
    pytest_html = report_dir / f"report_{now.strftime('%H%M%S')}.html"
    config.option.htmlpath = pytest_html
    config.option.self_contained_html = True
