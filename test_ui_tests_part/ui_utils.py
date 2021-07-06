import json
import time
import random
import string
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("http://localhost:8080/")
driver.maximize_window()


def load_json_file():
    with open("general_variables_ui.json") as json_file:
        json_object = json.load(json_file)
        json_file.close()
        return json_object


def sign_in_to_open_project(user_name, password):
    driver.find_element_by_xpath('//*[@title="Sign in"]').click()
    driver.find_element_by_id("username-pulldown").send_keys(user_name)
    driver.find_element_by_id("password-pulldown").send_keys(password)
    driver.find_element_by_id("login-pulldown").click()


def create_rand_project_name():
    rand_str_numbers = str(random.randint(0, 9)) + str(random.randint(0, 9))
    rand_str_letters = random.choice(string.ascii_lowercase) + random.choice(string.ascii_uppercase)
    rand_special_att = random.choice(['/', '#', '@', '%']) + random.choice(['/', '#', '@', '$', '%'])
    project_rand_name = f"test project {rand_str_numbers} {rand_str_letters} {rand_special_att}"
    return project_rand_name


def open_and_name_add_new_project(user_name, password, project_name):
    sign_in_to_open_project(user_name, password)
    driver.find_element_by_xpath('//*[@title="Open quick add menu"]').click()
    driver.find_element_by_xpath('//*[@title="New project"]').click()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'formly_3_textInput_name_0')))
    driver.find_element_by_id("formly_3_textInput_name_0").send_keys(project_name)


def check_advanced_settings():
    driver.find_element_by_xpath("//*[contains(text(), ' Advanced settings ')]").click()
    flippable_data_field = driver.find_element_by_tag_name('op-dynamic-field-group-wrapper')
    description_title_display = flippable_data_field.find_element_by_xpath(
        "//*[contains(text(), ' Description ')]").is_displayed()
    status_title_display = flippable_data_field.find_element_by_xpath(
        "//*[contains(text(), 'Status description')]").is_displayed()
    print("check_advanced_settings func:\n"
          f"description title displayed:{description_title_display}\n"
          f"status title displayed: {status_title_display}")
    condition = False
    if description_title_display and status_title_display:
        return True
    else:
        return False


def set_advanced_settings_and_save_project(description, status: "None / On track / At risk / Off track" = None):
    driver.find_element_by_xpath("//*[contains(text(), ' Advanced settings ')]").click()
    flippable_data_field = driver.find_element_by_tag_name('op-dynamic-field-group-wrapper')
    description_input = flippable_data_field.find_element_by_class_name("op-uc-p")
    description_input.send_keys(description)
    time.sleep(1)
    if status:
        flippable_data_field.find_element_by_class_name("ng-arrow-wrapper").click()
        status_options = flippable_data_field.find_elements_by_class_name("ng-option")
        for element in status_options:
            if element.find_element_by_xpath(f"//*[contains(text(), '{status}')]"):
                element.click()
                break
    driver.find_element_by_xpath("//*[contains(text(), ' Save ')]").click()


def check_test_name_top_dropdown(name: "project name"):
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, f"//*[contains(text(), '{name}')]")))
    project_top_left_button = driver.find_element_by_id("projects-menu")
    title = project_top_left_button.get_attribute("title")
    return title


def get_element_by_text_from_list_by_tag(tag_name, text):
    elements_list = driver.find_elements_by_tag_name(f"{tag_name}")
    for element in elements_list:
        inner_text = element.get_attribute('text')
        if inner_text == text:
            print(f"project {element.text} found!")
            return element


def wait_until_task_add_to_table(rows_before):
    rows_after = 0
    counter = 0
    while rows_after <= rows_before and counter <= 100:
        time.sleep(0.1)
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.TAG_NAME, 'table')))
        wp_table = driver.find_element_by_tag_name("table")
        wp_tr = wp_table.find_elements_by_tag_name("tr")
        rows_after = len(wp_tr)
        counter += 1
    return rows_after


def enter_project_work_pack_page(project_name):
    driver.find_element_by_id("projects-menu").click()
    project_link = get_element_by_text_from_list_by_tag("a", project_name)
    project_link.click()
    driver.find_element_by_id("main-menu-work-packages").click()


def get_work_pack_table_elements():
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.TAG_NAME, 'table')))
    wp_table = driver.find_element_by_tag_name("table")
    return wp_table.find_elements_by_tag_name("tr")


def open_new_task_dropdown():
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//button[@aria-label='Create new work package']")))
    driver.find_element_by_xpath("//button[@aria-label='Create new work package']").click()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//a[@aria-label='Task']")))
    driver.find_element_by_xpath("//a[@aria-label='Task']").click()


def get_new_task_header_text():
    open_new_task_dropdown()
    WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "work-packages--new-details-header")))
    new_task_header = driver.find_element_by_class_name("work-packages--new-details-header")
    new_title_text = new_task_header.find_element_by_xpath('//*[@title="New"]').text
    task_title_text = new_task_header.find_element_by_xpath('//*[@title="Task"]').text
    header_title = f"{new_title_text} {task_title_text}"
    return header_title


def fill_desc_and_subject_and_create_task(subject, description):
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "wp-new-inline-edit--field-subject")))
    driver.find_element_by_id("wp-new-inline-edit--field-subject").send_keys(subject)
    driver.find_element_by_class_name("op-uc-p").send_keys(description)
    driver.find_element_by_id("work-packages--edit-actions-save").click()


def get_last_work_pack_subject_and_type_from_list(element_list, subject) -> "subject and type tuple":
    last_task_in_table = element_list[len(element_list) - 1]
    subject_td_text = last_task_in_table.find_element_by_xpath(f'//*[@title="{subject}"]').text.lower()
    type_td_text = last_task_in_table.find_element_by_xpath('//*[@title="Task"]').text.lower()
    print(f"new task in table subject: {subject_td_text}, mew task type: {type_td_text}")
    results_tuple = (subject_td_text, type_td_text)
    return results_tuple
