# -*- coding: utf-8 -*-
from lettuce import *
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


@step(u'Given I go to "([^"]*)"')
def given_i_go_to(step, url):
    world.driver.get(url)

@step(u'Insert text "([^"]*)" in element "(.*?)"')
def insert_text_in_element(step, text,id):
    element=world.driver.find_element(By.ID,id)
    element.send_keys(text)

@step(u'Check if element "(.*?)" value is "([^"]*)"')
def check_if_value_is(step, id,value):
    element=world.driver.find_element(By.ID,id)

    current_value=element.get_attribute('value')

    assert current_value==value

@step(u'Check if result is "([^"]*)"')
def check_result(step,value):
    elements=world.driver.find_elements(By.ID,'result')

    current_value=""

    for element in elements:
        current_value= current_value+element.text
    
    assert current_value==value

@step(u'Pulse button "(.*?)"')
def pulse_button(step,id):
    button=world.driver.find_element(By.ID,id)

    if button.is_enabled():
        button.click()

'''
Insertar texto

Insertar mas de 100 caracteres

resetear sin texto

resetear con texto

Insertar texto y contar

Insertar texto ,contar y resetar

Insertar texto ,contar, insertar y resetar

Insertar texto ,contar y insertar texto y contar

Insertar texto ,contar y contar
'''