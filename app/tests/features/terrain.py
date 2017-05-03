import os
from lettuce import before, world, after
from selenium import webdriver


@before.all
def open_shop():
    open_drivers()

@after.all
def close_shop(total):
    print "Total %d of %d scenarios passed!" % (total.scenarios_passed, total.scenarios_ran)
    close_drivers()

def open_drivers():
    world.driver = webdriver.Chrome('/path/to/chromedriver')
    world.driver.set_page_load_timeout(3)
    world.driver.implicitly_wait(3)
    world.driver.maximize_window()


def close_drivers():
    if world.driver:
        world.driver.quit()