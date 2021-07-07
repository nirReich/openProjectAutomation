import pytest
from test_ui_tests_part.ui_utils import create_rand_project_name, open_and_name_add_new_project, \
    check_advanced_settings, set_advanced_settings_and_save_project, check_test_name_top_dropdown, load_json_file, \
    sign_in_to_open_project, enter_project_work_pack_page, get_new_task_header_text, \
    get_work_pack_table_elements, open_new_task_dropdown, fill_desc_and_subject_and_create_task, \
    wait_until_task_add_to_table, get_last_work_pack_subject_and_type_from_list

json = load_json_file()
user_name_for_test = json["ui"]["test_user_name"]
password_for_test = json["ui"]["test_password"]
proj_description = json["ui"]["project_description"]
project_status = json["ui"]["project_status"]
tested_project_name = json["ui"]["tested_project_name"]
task_subject = json["ui"]["task_subject"]
task_description = json["ui"]["task_description"]


# -----------------------
@pytest.mark.project_sanity
def test_advanced_settings_dropdown():
    proj_name = create_rand_project_name()
    open_and_name_add_new_project(user_name_for_test, password_for_test, proj_name)
    term = check_advanced_settings()
    assert term, f"advanced settings content displayed: {term}"


@pytest.mark.project_sanity
def test_project_created():
    proj_name = create_rand_project_name()
    open_and_name_add_new_project(user_name_for_test, password_for_test, proj_name)
    set_advanced_settings_and_save_project(proj_description, project_status)
    title = check_test_name_top_dropdown(proj_name)
    assert title == proj_name, f"crated project name test fail. current project name:{proj_name}"


@pytest.mark.work_pack_sanity
def test_new_task_header():
    sign_in_to_open_project(user_name_for_test, password_for_test)
    enter_project_work_pack_page(tested_project_name)
    header_title = get_new_task_header_text()
    print("header title: ", header_title)
    assert header_title == "New TASK", f"title test failed!, current header title {header_title}"


@pytest.mark.work_pack_sanity
def test_task_add_to_table():
    sign_in_to_open_project(user_name_for_test, password_for_test)
    enter_project_work_pack_page(tested_project_name)
    rows_in_table_before = len(get_work_pack_table_elements())
    open_new_task_dropdown()
    fill_desc_and_subject_and_create_task(task_subject, task_description)
    wp_tr_after = wait_until_task_add_to_table(rows_in_table_before)
    print(f"table rows before: {rows_in_table_before}, table rows after: {wp_tr_after}")
    assert wp_tr_after == rows_in_table_before + 1, f"number of rows test failed!, rows before: {rows_in_table_before}, rows after:{wp_tr_after}"


@pytest.mark.work_pack_sanity
def test_new_task_subject_and_type():
    sign_in_to_open_project(user_name_for_test, password_for_test)
    enter_project_work_pack_page(tested_project_name)
    rows_in_table_before = len(get_work_pack_table_elements())
    open_new_task_dropdown()
    fill_desc_and_subject_and_create_task(task_subject, task_description)
    wait_until_task_add_to_table(rows_in_table_before)
    table_elements = get_work_pack_table_elements()
    task_tr_tuple = get_last_work_pack_subject_and_type_from_list(table_elements, task_subject)
    assert task_tr_tuple[0] == task_subject and task_tr_tuple[
        1] == "task", f"type and subject test failed!, current type: {task_tr_tuple[1]} and subject:{task_tr_tuple[0]}!"
