import pytest
import time


def pytest_html_report_title(report):
    ''' modifying the title of html report'''
    report.title = "NASA APIs - Asteroids."

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

    # print('passed amount:', len(terminalreporter.stats['passed']))
    # print('failed amount:', len(terminalreporter.stats['failed']))
    # print('xfailed amount:', len(terminalreporter.stats['xfailed']))
    # print('skipped amount:', len(terminalreporter.stats['skipped']))

    # print('terminalreporter:',terminalreporter.stats)
            
    print('Status:', resume)

    duration = time.time() - terminalreporter._sessionstarttime
    print('duration:', duration, 'seconds')

# def pytest_sessionfinish(session, exitstatus):
#     terminalreporter = session.config.pluginmanager.get_plugin('terminalreporter')
#     print('sessionfinish - passed amount:', len(terminalreporter.stats['passed']))
#     print('sessionfinish - failed amount:', len(terminalreporter.stats['failed']))
#     print('sessionfinish - xfailed amount:', len(terminalreporter.stats['xfailed']))
#     print('sessionfinish - skipped amount:', len(terminalreporter.stats['skipped']))

