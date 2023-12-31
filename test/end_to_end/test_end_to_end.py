from os.path import join, dirname
from pytest_csv_params.decorator import csv_params

from src.pages.login_page import LoginPage
from src.pages.dashboard_page import DashboardPage
from src.pages.pim_page import PimPage
from src.pages.my_info_page import MyinfoPage

@csv_params(
    data_file="data_login_admin_valid.csv",
    base_dir=join(dirname(__file__), "../assets"),
    data_casts={
        "username": str,
        "password": str
    },
)
@csv_params(
    data_file="data_employees_informations.csv",
    base_dir=join(dirname(__file__), "../assets"),
    data_casts={
        "id_employee": str,
        "first_name": str,
        "last_name": str,
        "username_employee": str,
        "password_employee": str
    },
)
def test_end_to_end_ok(username: str, password: str, id_employee: str, first_name: str, last_name: str, username_employee: str, password_employee: str, login_page: LoginPage, dashboard_page: DashboardPage, pim_page: PimPage, my_info_page: MyinfoPage) -> None:
    '''
        Test end to end successful .
    '''
    assert login_page.verify_page_title()
    assert login_page.verify_page_url()

    login_page.login(username, password)

    assert dashboard_page.verify_page()

    dashboard_page.go_to_pim_page()

    assert pim_page.verify_page()

    pim_page.click_button_add_employee()

    assert pim_page.verify_existence_of_add_employee_text()

    pim_page.fill_form_employee(True)

    assert pim_page.verify_existence_personal_details_button()

    dashboard_page.go_to_pim_page()

    assert pim_page.verify_page()

    employee_details = pim_page.search_employee_by_id()

    assert pim_page.verify_existence_of_one_employee(employee_details)

    pim_page.update_id_employee()

    assert my_info_page.verify_toaster_success()
    
    dashboard_page.go_to_pim_page()

    assert pim_page.verify_page()

    employee_details = pim_page.search_employee_by_id()

    assert pim_page.verify_existence_of_one_employee(employee_details)
    
    dashboard_page.logout()

    assert login_page.verify_existence_of_login_text()

    assert login_page.verify_page_title()
    assert login_page.verify_page_url()

    login_page.login(username_employee, password_employee)

    assert dashboard_page.verify_page()

    my_info_page.go_to_my_info()

    assert pim_page.verify_existence_personal_details_button()

    my_info_page.go_to_personal_details()

    assert my_info_page.verify_header_form_personal_details()
    
    my_info_page.insert_marital_status_and_gender_into_personal_details()
    
    assert my_info_page.verify_toaster_success()

    my_info_page.insert_blood_type_into_personal_details()
    
    assert my_info_page.verify_toaster_success()

    my_info_page.go_to_contact_details()

    assert my_info_page.verify_header_form_contact_details()

    my_info_page.insert_into_contact_details()

    assert my_info_page.verify_toaster_success()

    dashboard_page.logout()

    assert login_page.verify_existence_of_login_text()