import pytest
import time

from selenium import webdriver  
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager  
  

## Setup Chrome Driver 
@pytest.fixture()  
def chrome_browser():

    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--ignore-certificate-errors")
    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])

    driver = webdriver.Chrome(options=chrome_options)  
  
    # Use this line instead of the prev if you wish to download the ChromeDriver binary on the fly  
    # driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))  
      
    driver.implicitly_wait(10)  
    # Yield the WebDriver instance  
    yield driver  
    # Close the WebDriver instance  
    driver.quit()


## Parameters from command line
def pytest_addoption(parser):
    parser.addoption("--name", action="store", default="default name")

## Report Customization - Title
def pytest_html_report_title(report):
    ''' modifying the title of html report'''
    report.title = "NASA APIs - Asteroids."

## Report Customization - html - Prefix, Summary, Oostfix
def pytest_html_results_summary(prefix, summary, postfix):
    prefix.extend([r"""<button onclick="myFunction()">Click Object-Prefix</button>

    <p id="demo"></p>

    <script>
    function myFunction() {
    document.getElementById("demo").innerHTML = "Hello World - prefix";
    }
    </script>
    """])

    summary.extend([r"""<button onclick="myFunction2()">Click Object-summary</button>

    <p id="demo2"></p>

    <script>
    function myFunction2() {
    document.getElementById("demo2").innerHTML = "Hello World - summary";
    }
    </script>
    """])

    postfix.extend([r"""<button onclick="myFunction3()">Click Object-postfix</button>

    <p id="demo3"></p>

    <script>
    function myFunction3() {
    document.getElementById("demo3").innerHTML = "Hello World - postfix";
    }
    </script>
    """])


## Report Data Summary
def pytest_terminal_summary(terminalreporter, exitstatus, config):

    resume = {
        'passed' : 0,
        'failed' : 0,
        'xfailed' : 0,
        'skipped' : 0
    }

    for key in terminalreporter.stats:
        if len(key)>0:
            resume[key] = len(terminalreporter.stats[key])
            # print("Status:", key, '->', len(terminalreporter.stats[key]))

    # print('terminalreporter:',terminalreporter.stats)
            
    print('Status:', resume)

    duration = time.time() - terminalreporter._sessionstarttime
    print('duration:', duration, 'seconds')


