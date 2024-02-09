import time

import pytest
import request
import inspect
from appium import webdriver
from appium.options.common.base import AppiumOptions
from pages import main
from selenium.common.exceptions import TimeoutException
import allure
from openpyxl import Workbook, load_workbook
# Load the existing Excel workbook
wb = load_workbook(r"C:\Users\admin\PycharmProjects\Appium\test_results.xlsx")
ws = wb.active
# Define a fixture to save the workbook after the tests have run
@pytest.fixture(scope="session")
def excel_results(request):
    def fin():
        wb.save("test_results.xlsx")
        wb.close()

    request.addfinalizer(fin)
# Define a fixture to open the appium driver
# @pytest.fixture(scope="module")
# def appium_driver():
#     options = AppiumOptions()
#     options.load_capabilities({
#     "platformName": "Android",
#     "deviceName": "RZ8R21SMYNN",
#     })
#     driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", options=options)
#     yield driver
#     driver.quit()

@pytest.fixture(scope="module")
def appium_driver():
    options = AppiumOptions()
    options.load_capabilities({
        "platformName": "Android",
        "deviceName": "RZ8R21SMYNN",
        # Add other desired capabilities as needed
    })
    # Add other desired capabilities as needed

    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", options=options)
    yield driver
    # driver.quit()


@pytest.mark.usefixtures("appium_driver","excel_results")
class Testorderpage:
    @staticmethod
    def test_openapp_tc_01(appium_driver,excel_results):
        try:
            main.TestAppiumAutomation.test_click_docile_delivery_element(appium_driver)
            time.sleep(7)
            screenshot_name = f"test_openapp_tc_01.png"
            # allure.attach(appium_driver.get_screenshot_as_png(), name="Screenshot",
            #               attachment_type=allure.attachment_type.PNG)
            appium_driver.save_screenshot(screenshot_name)

            assert True  # Example assertion
            result = "Pass"
            function_name = inspect.stack()[0][3]
            test_id = function_name.split("_")[-1]
            screenshot_hyperlink = f'=HYPERLINK("{screenshot_name}", "Screenshot")'
            ws.append(
                [f"TC-{test_id}", function_name, result, screenshot_hyperlink, "None", "None", "open the docile app",
                 "As Expected", "APK", "None"])
            wb.save("test_results.xlsx")
            wb.save("test_results.xlsx")
        except TimeoutException:
            result = "Fail"
            screenshot_name = f"test_openapp_tc_01.png"
            # allure.attach(appium_driver.get_screenshot_as_png(), name="Screenshot",
            #               attachment_type=allure.attachment_type.PNG)
            appium_driver.save_screenshot(screenshot_name)
            function_name = inspect.stack()[0][3]
            test_id = function_name.split("_")[-1]
            screenshot_hyperlink = f'=HYPERLINK("{screenshot_name}", "Screenshot")'
            ws.append([f"TC-{test_id}", function_name, result, screenshot_hyperlink, "High", "Try using ID or Xpath",
                       "open docile App", "Not opening", "APK", "it's not clicking the app icon"])
            wb.save("test_results.xlsx")
###############################################################################################################################
    def test_yestologin_tc_02(self,appium_driver):
        try:
            main.TestAppiumAutomation.test_pressyes(self,appium_driver)
            time.sleep(7)
            screenshot_name = f"test_openapp_tc_02.png"
            # allure.attach(appium_driver.get_screenshot_as_png(), name="Screenshot",
            #               attachment_type=allure.attachment_type.PNG)
            appium_driver.save_screenshot(screenshot_name)

            assert True  # Example assertion
            result = "Pass"
            function_name = inspect.stack()[0][3]
            test_id = function_name.split("_")[-1]
            screenshot_hyperlink = f'=HYPERLINK("{screenshot_name}", "Screenshot")'
            ws.append(
                [f"TC-{test_id}", function_name, result, screenshot_hyperlink, "None", "None", "YES to login",
                 "As Expected", "APK", "None"])
            wb.save("test_results.xlsx")

        except TimeoutException:
            result = "Fail"
            screenshot_name = f"test_openapp_tc_02.png"
            # allure.attach(appium_driver.get_screenshot_as_png(), name="Screenshot",
            #               attachment_type=allure.attachment_type.PNG)
            appium_driver.save_screenshot(screenshot_name)
            function_name = inspect.stack()[0][3]
            test_id = function_name.split("_")[-1]
            screenshot_hyperlink = f'=HYPERLINK("{screenshot_name}", "Screenshot")'
            ws.append([f"TC-{test_id}", function_name, result, screenshot_hyperlink])
            wb.save("test_results.xlsx")

            function_name = inspect.stack()[0][3]
            test_id = function_name.split("_")[-1]
            ws.append([f"TC-{test_id}", function_name, result, screenshot_hyperlink, "High", "Try using ID or Xpath",
                       "YES to login", "Not opening", "APK", "it's not clicking the app icon"])
################################################################################################################################################################
    def test_mobile_otp_tc_03(self,appium_driver):
        try:
            main.TestAppiumAutomation.test_mobile_number(self,appium_driver)
            time.sleep(7)
            screenshot_name = f"test_mobileotp_tc_03.png"
            # allure.attach(appium_driver.get_screenshot_as_png(), name="Screenshot",
            #               attachment_type=allure.attachment_type.PNG)
            appium_driver.save_screenshot(screenshot_name)

            assert True  # Example assertion
            result = "Pass"
            function_name = inspect.stack()[0][3]
            test_id = function_name.split("_")[-1]
            screenshot_hyperlink = f'=HYPERLINK("{screenshot_name}", "Screenshot")'
            ws.append(
                [f"TC-{test_id}", function_name, result, screenshot_hyperlink, "None", "None", "Login with mobile no",
                 "As Expected", "APK", "None"])
            wb.save("test_results.xlsx")


        except TimeoutException:

            result = "Fail"

            screenshot_name = f"test_mobileotp_tc_03.png"

            # allure.attach(appium_driver.get_screenshot_as_png(), name="Screenshot",
            #
            #               attachment_type=allure.attachment_type.PNG)

            appium_driver.save_screenshot(screenshot_name)

            function_name = inspect.stack()[0][3]

            test_id = function_name.split("_")[-1]

            screenshot_hyperlink = f'=HYPERLINK("{screenshot_name}", "Screenshot")'

            ws.append([f"TC-{test_id}", function_name, result, screenshot_hyperlink])

            wb.save("test_results.xlsx")

            function_name = inspect.stack()[0][3]

            test_id = function_name.split("_")[-1]

            ws.append([f"TC-{test_id}", function_name, result, screenshot_hyperlink, "High", "Try using ID or Xpath",
                       "Login with mobile no", "Not opening", "APK", "it's not clicking the app icon"])
############################################################################ 3 ###########################################
    def test_notification_button_tc_04(self,appium_driver):
        try:
            main.TestAppiumAutomation.test_notification_button(self,appium_driver)
            time.sleep(7)
            screenshot_name = f"test_notification_tc_04.png"
            # allure.attach(appium_driver.get_screenshot_as_png(), name="Screenshot",
            #               attachment_type=allure.attachment_type.PNG)
            appium_driver.save_screenshot(screenshot_name)

            assert True  # Example assertion
            result = "Pass"
            function_name = inspect.stack()[0][3]
            test_id = function_name.split("_")[-1]
            screenshot_hyperlink = f'=HYPERLINK("{screenshot_name}", "Screenshot")'
            ws.append(
                [f"TC-{test_id}", function_name, result, screenshot_hyperlink, "None", "None", "Click on notification",
                 "As Expected", "APK", "None"])
            wb.save("test_results.xlsx")
        except TimeoutException:
            result = "Fail"
            screenshot_name = f"test_notfication_tc_04.png"
            # allure.attach(appium_driver.get_screenshot_as_png(), name="Screenshot",
            #               attachment_type=allure.attachment_type.PNG)
            appium_driver.save_screenshot(screenshot_name)
            function_name = inspect.stack()[0][3]
            test_id = function_name.split("_")[-1]
            screenshot_hyperlink = f'=HYPERLINK("{screenshot_name}", "Screenshot")'
            ws.append([f"TC-{test_id}", function_name, result, screenshot_hyperlink])
            wb.save("test_results.xlsx")
            function_name = inspect.stack()[0][3]
            test_id = function_name.split("_")[-1]
            ws.append([f"TC-{test_id}", function_name, result, screenshot_hyperlink, "High", "Try using ID or Xpath",
                       "Click on notification ", "Not opening", "APK", "it's not clicking the app icon"])
################################################################################################################################
    def testorder_details_ongoing_tc_05(self,appium_driver):
        try:
            main.TestAppiumAutomation. test_dropdown_myorders_ongoing(self,appium_driver)
            time.sleep(7)
            screenshot_name = f"test_notification_tc_04.png"
            appium_driver.save_screenshot(screenshot_name)

            assert True  # Example assertion
            result = "Pass"
            function_name = inspect.stack()[0][3]
            test_id = function_name.split("_")[-1]
            screenshot_hyperlink = f'=HYPERLINK("{screenshot_name}", "Screenshot")'
            ws.append([f"TC-{test_id}", function_name, result, screenshot_hyperlink])
            wb.save("test_results.xlsx")
        except AssertionError:
            result = "Fail"
        function_name = inspect.stack()[0][3]
        test_id = function_name.split("_")[-1]
        ws.append([f"TC-{test_id}", function_name, result])

    def test_orderdetails_button_ongoing_tc_06(self,appium_driver):
        try:
            main.TestAppiumAutomation.test_orderdetails_button(self,appium_driver)
            assert True
            result = "Pass"
        except TimeoutException:
            print("TimeoutException: Element not found within the specified timeout")
            result = "Fail"
        function_name = inspect.stack()[0][3]
        test_id = function_name.split("_")[-1]
        ws.append([f"TC-{test_id}", function_name, result])
####################################################################################################################
    def test_payment_button_click_tc_05(self,appium_driver):
        try:
            main.TestAppiumAutomation. test_payments(self,appium_driver)
            time.sleep(7)
            screenshot_name = f"test_payment_tc_07.png"
            appium_driver.save_screenshot(screenshot_name)

            assert True  # Example assertion
            result = "Pass"
            function_name = inspect.stack()[0][3]
            test_id = function_name.split("_")[-1]
            screenshot_hyperlink = f'=HYPERLINK("{screenshot_name}", "Screenshot")'
            ws.append(
                [f"TC-{test_id}", function_name, result, screenshot_hyperlink, "None", "None", "payment button click",
                 "As Expected", "APK", "None"])
            wb.save("test_results.xlsx")
        except TimeoutException:
            result = "Fail"
            screenshot_name = f"test_payment_tc_07.png"
            appium_driver.save_screenshot(screenshot_name)
            function_name = inspect.stack()[0][3]
            test_id = function_name.split("_")[-1]
            screenshot_hyperlink = f'=HYPERLINK("{screenshot_name}", "Screenshot")'
            ws.append([f"TC-{test_id}", function_name, result, screenshot_hyperlink])
            wb.save("test_results.xlsx")
            function_name = inspect.stack()[0][3]
            test_id = function_name.split("_")[-1]
            ws.append([f"TC-{test_id}", function_name, result, screenshot_hyperlink, "High", "Try using ID or Xpath",
                       "payment button click", "Not opening", "APK", "it's not clicking the app icon"])
###############################################################################################################################
    def test_performance_button_click_tc_06(self,appium_driver):
        try:
            main.TestAppiumAutomation. test_performance_button(self,appium_driver)
            time.sleep(7)
            screenshot_name = f"test_performance_tc_08.png"
            appium_driver.save_screenshot(screenshot_name)

            assert True  # Example assertion
            result = "Pass"
            function_name = inspect.stack()[0][3]
            test_id = function_name.split("_")[-1]
            screenshot_hyperlink = f'=HYPERLINK("{screenshot_name}", "Screenshot")'
            ws.append(
                [f"TC-{test_id}", function_name, result, screenshot_hyperlink, "None", "None", "performance button click",
                 "As Expected", "APK", "None"])
            wb.save("test_results.xlsx")
        except TimeoutException:
            result = "Fail"
            screenshot_name = f"test_performance_tc_08.png"
            appium_driver.save_screenshot(screenshot_name)
            function_name = inspect.stack()[0][3]
            test_id = function_name.split("_")[-1]
            screenshot_hyperlink = f'=HYPERLINK("{screenshot_name}", "Screenshot")'
            ws.append([f"TC-{test_id}", function_name, result, screenshot_hyperlink])
            wb.save("test_results.xlsx")
            function_name = inspect.stack()[0][3]
            test_id = function_name.split("_")[-1]
            ws.append([f"TC-{test_id}", function_name, result, screenshot_hyperlink, "High", "Try using ID or Xpath",
                       "performance button click", "Not opening", "APK", "it's not clicking the app icon"])
##################################################################################################################
    def test_account_button_click_tc_07(self,appium_driver):
        try:
            main.TestAppiumAutomation.test_account(self,appium_driver)
            time.sleep(7)
            screenshot_name = f"test_account_tc_09.png"
            appium_driver.save_screenshot(screenshot_name)

            assert True  # Example assertion
            result = "Pass"
            function_name = inspect.stack()[0][3]
            test_id = function_name.split("_")[-1]
            screenshot_hyperlink = f'=HYPERLINK("{screenshot_name}", "Screenshot")'
            ws.append(
                [f"TC-{test_id}", function_name, result, screenshot_hyperlink, "None", "None",
                 "Account button click",
                 "As Expected", "APK", "None"])
            wb.save("test_results.xlsx")
        except TimeoutException:
            result = "Fail"
            screenshot_name = f"test_account_tc_09.png"
            appium_driver.save_screenshot(screenshot_name)
            function_name = inspect.stack()[0][3]
            test_id = function_name.split("_")[-1]
            screenshot_hyperlink = f'=HYPERLINK("{screenshot_name}", "Screenshot")'
            ws.append([f"TC-{test_id}", function_name, result, screenshot_hyperlink])
            wb.save("test_results.xlsx")
            function_name = inspect.stack()[0][3]
            test_id = function_name.split("_")[-1]
            ws.append([f"TC-{test_id}", function_name, result, screenshot_hyperlink, "High", "Try using ID or Xpath",
                       "Account button click", "Not opening", "APK", "it's not clicking the app icon"])
################################################################################################################
    def test_dutystatus_button_click_tc_08(self,appium_driver):
        try:
            main.TestAppiumAutomation.test_dutystatus_on(self,appium_driver)
            time.sleep(7)
            screenshot_name = f"test_statuson_tc_09.png"
            appium_driver.save_screenshot(screenshot_name)

            assert True  # Example assertion
            result = "Pass"
            function_name = inspect.stack()[0][3]
            test_id = function_name.split("_")[-1]
            screenshot_hyperlink = f'=HYPERLINK("{screenshot_name}", "Screenshot")'
            ws.append(
                [f"TC-{test_id}", function_name, result, screenshot_hyperlink, "None", "None",
                 "Duty status on and off",
                 "As Expected", "APK", "None"])
            wb.save("test_results.xlsx")
        except TimeoutException:
            result = "Fail"
            screenshot_name = f"test_statuson_tc_09.png"
            appium_driver.save_screenshot(screenshot_name)
            function_name = inspect.stack()[0][3]
            test_id = function_name.split("_")[-1]
            screenshot_hyperlink = f'=HYPERLINK("{screenshot_name}", "Screenshot")'
            ws.append([f"TC-{test_id}", function_name, result, screenshot_hyperlink])
            wb.save("test_results.xlsx")
            function_name = inspect.stack()[0][3]
            test_id = function_name.split("_")[-1]
            ws.append([f"TC-{test_id}", function_name, result, screenshot_hyperlink, "High", "Try using ID or Xpath",
                       "Duty status on and off", "Not opening", "APK", "it's not clicking the app icon"])

########################################################################################################
    def test_ordercompleted_button_click_tc_09(self, appium_driver):
        try:
            main.TestAppiumAutomation.test_dropdown_myorders_completed(self, appium_driver)
            time.sleep(7)
            screenshot_name = f"test_completed_tc_09.png"
            appium_driver.save_screenshot(screenshot_name)
            assert True  # Example assertion
            result = "Pass"
            function_name = inspect.stack()[0][3]
            test_id = function_name.split("_")[-1]
            screenshot_hyperlink = f'=HYPERLINK("{screenshot_name}", "Screenshot")'
            ws.append([f"TC-{test_id}", function_name, result, screenshot_hyperlink])
            wb.save("test_results.xlsx")
        except TimeoutException:
            result = "Fail"
            screenshot_name = f"test_completed_tc_09.png"
            appium_driver.save_screenshot(screenshot_name)
            function_name = inspect.stack()[0][3]
            test_id = function_name.split("_")[-1]
            screenshot_hyperlink = f'=HYPERLINK("{screenshot_name}", "Screenshot")'
            ws.append([f"TC-{test_id}", function_name, result, screenshot_hyperlink])
            wb.save("test_results.xlsx")
            function_name = inspect.stack()[0][3]
            test_id = function_name.split("_")[-1]
            if __name__ == '__main__':
                ws.append([f"TC-{test_id}", function_name, result])
    ########################################################################################################
    def test_orderdetailscompleted_button_click_tc_10(self, appium_driver):
        try:
            main.TestAppiumAutomation.test_orderdetails_button_completed(self, appium_driver)
            time.sleep(7)
            screenshot_name = f"test_completed_tc_10.png"
            appium_driver.save_screenshot(screenshot_name)
            assert True  # Example assertion
            result = "Pass"
            function_name = inspect.stack()[0][3]
            test_id = function_name.split("_")[-1]
            screenshot_hyperlink = f'=HYPERLINK("{screenshot_name}", "Screenshot")'
            ws.append([f"TC-{test_id}", function_name, result, screenshot_hyperlink])
            wb.save("test_results.xlsx")
        except TimeoutException:
            result = "Fail"
            screenshot_name = f"test_completed_tc_10.png"
            appium_driver.save_screenshot(screenshot_name)
            function_name = inspect.stack()[0][3]
            test_id = function_name.split("_")[-1]
            screenshot_hyperlink = f'=HYPERLINK("{screenshot_name}", "Screenshot")'
            ws.append([f"TC-{test_id}", function_name, result, screenshot_hyperlink])
            wb.save("test_results.xlsx")
            function_name = inspect.stack()[0][3]
            test_id = function_name.split("_")[-1]
            ws.append([f"TC-{test_id}", function_name, result])

    #################################################################################################################
    def test_logout_button_click(self,appium_driver):
        main.TestAppiumAutomation.test_logout_button(self,appium_driver)

