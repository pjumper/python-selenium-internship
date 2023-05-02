from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from app.application import Application
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.service import service
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

def browser_init(context, test_name):
    """
    :param context: Behave context
    :param test_name: scenario.name
    """

    # ########### GOOGLE CHROME ###########################
    #options = ChromeOptions()
    #options.add_argument("--headless")
    #options.add_argument("--window-size=1920,1080")
    #options.add_argument("--start-maximized")
    #context.driver = webdriver.Chrome(executable_path='chromedriver', options=options)
    # #####################################################

    ############## FIREFOX ################################
    #options = FirefoxOptions()
    #options.headless = True
    #context.driver = webdriver.Firefox(executable_path='geckodriver', options=options)
    #######################################################
    #context.driver = webdriver.Chrome('service=service')
    #context.driver = webdriver.Firefox(service=service)

    #context.driver = webdriver.Safari()
    #context.driver = webdriver.Firefox()

    ##HEADLESS MODE ##
    # options = webdriver.ChromeOptions()
    # options.add_argument('--headless')
    # context.driver = webdriver.Chrome(
    #     chrome_options=options,
    #     service=service
    # )

    ### for browserstack ###
    desired_cap = {
        'browser': 'Chrome',
        'os_version': '11',
        'os': 'Windows',
        'name': test_name
    }
    bs_user = 'chriscrayton_YJMgRK'
    bs_key = 'g3UKWUehpdP2scReX7WL'
    url = f'http://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'
    context.driver = webdriver.Remote(url, desired_capabilities=desired_cap)

    context.driver.maximize_window()
    context.driver.implicitly_wait(5)
    context.driver.wait = WebDriverWait(context.driver, 10)
    context.app = Application(driver=context.driver)

def before_scenario(context, scenario):
    #print('\nStarted scenario: ', scenario.name)
    browser_init(context, scenario.name)


def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)


def after_scenario(context, feature):
    context.driver.delete_all_cookies()
    context.driver.quit()


