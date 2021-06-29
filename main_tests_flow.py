import random
import string
import time


from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://www.openproject.org/")
driver.maximize_window()

driver.find_element_by_xpath("/html/body/div[2]/div/nav/div[2]/div[2]/ul/li[3]/a").click()
driver.find_element_by_id("signin-input").send_keys("nirreichfinalproject")
WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="signin"]/input')))
driver.find_element_by_xpath('//*[@id="signin"]/input').click()
WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.ID, "username")))
driver.find_element_by_id("username").send_keys("reich.nir@gmail.com")
driver.find_element_by_id("password").send_keys("nir7281161")
WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="login-form"]/form/input[4]')))
driver.find_element_by_xpath('//*[@id="login-form"]/form/input[4]').click()
WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.CLASS_NAME, 'op-quick-add-menu--icon')))
driver.find_element_by_class_name("op-quick-add-menu--icon").click()
WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.ID, 'quick-add-menu')))
li_locator = driver.find_element_by_xpath('//*[@data-name="new_project"]')
li_locator.find_element_by_xpath('//*[@title="New project"]').click()
WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="formly_3_textInput_name_0"]')))
rand_str_numbers = str(random.randint(0, 9)) + str(random.randint(0, 9))
rand_str_letters = random.choice(string.ascii_lowercase) + random.choice(string.ascii_uppercase)
rand_special_att = random.choice(['/', '#', '@', '%']) + random.choice(['/', '#', '@', '$', '%'])
project_rand_name = (rand_str_numbers + ' ' + rand_str_letters + ' ' + rand_special_att)
driver.find_element_by_xpath('//*[@id="formly_3_textInput_name_0"]').send_keys(project_rand_name)
driver.find_element_by_xpath("//*[contains(text(), ' Advanced settings ')]").click()
WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.TAG_NAME, 'op-dynamic-field-group-wrapper')))
flippable_data_field = driver.find_element_by_tag_name('op-dynamic-field-group-wrapper')
description_title = flippable_data_field.find_element_by_xpath("//*[contains(text(), ' Description ')]")
status_title = flippable_data_field.find_element_by_xpath("//*[contains(text(), 'Status description')]")
if description_title and status_title != None:
    print("data content OK!")
else:
    print("no data found")
text_filed_XPATH = '//*[@id="formly_9_formattableInput_statusExplanation_5"]/div/op-ckeditor/div/div[2]/div/p'
WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.XPATH, text_filed_XPATH)))
text_filed_p = driver.find_element_by_xpath(text_filed_XPATH)
text_filed_p.send_keys("this is a test text for project: ", project_rand_name)
submit_div = driver.find_element_by_class_name('op-form--submit')
submit_div.find_element_by_xpath("//button[contains(text(), 'Save')]").click()
time.sleep(5)
current_url = driver.current_url
split_url = current_url.split('/')
proj_identifier = split_url[4]
expected_identifier = proj_identifier.replace(' ', '-').replace('/', '-').replace('#', '-').replace('@', '-').replace(
    '$', '-').replace('%', '-')
print(expected_identifier)


# WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.CLASS_NAME, "max-width")))
