from django.test import LiveServerTestCase
from selenium import webdriver



class PlayerFormTest(LiveServerTestCase):

    def test_upload_branch_form(self):
        browser = webdriver.Chrome()
        browser.get('http://127.0.0.1:8000/admin_login/login/')
        input_1 = browser.find_element_by_id("id_username")
        input_1.send_keys("admin")
        input_2 = browser.find_element_by_id("id_password")
        input_2.send_keys("12345678")
        button_admin_login = browser.find_element_by_id("admin_login").click()
        button_branch = browser.find_element_by_id("branch").click()
        branch_upload = browser.find_element_by_id("upload_branch").click()
        input_3 = browser.find_element_by_id("id_name")
        input_3.send_keys("Китай")
        input_4 = browser.find_element_by_id("id_description")
        input_4.send_keys("С 20 мая в нашем кинотеатре появиться новый кинозал. Ждем вас в гости!")
        button_new = browser.find_element_by_id("branch_mpei").click()




