import time
import pytest
from appium import webdriver
from appium.options.common.base import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(scope="module")
def appium_driver():
    options = AppiumOptions()
    options.load_capabilities({
            "platformName": "Android",
            "deviceName": "adb-RZ8R21SMYNN-i8os4l._adb-tls-connect._tcp",
            # Add other desired capabilities as needed
        })
    # Add other desired capabilities as needed

    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", options=options)
    yield driver
    driver.quit()

@pytest.mark.usefixtures("appium_driver")
class TestAppiumAutomation:
    @staticmethod
    def test_click_docile_delivery_element(appium_driver):
        el = WebDriverWait(appium_driver, 20).until(
            EC.element_to_be_clickable((
                AppiumBy.XPATH, '//android.widget.TextView[@content-desc="DeliveryAgentApp1502"]'
        ))
        )
        el.click()

    @staticmethod
    def test_pressNo(appium_driver):
        el = WebDriverWait(appium_driver, 20).until(
            EC.element_to_be_clickable((
                AppiumBy.XPATH, '//android.view.ViewGroup[@resource-id="noBtn"]'
            ))
        )
        el.click()
        el = WebDriverWait(appium_driver, 20).until(
            EC.element_to_be_clickable((
                AppiumBy.XPATH, '//android.widget.TextView[@text="Okay"]'
            ))
        )
        el.click()

    @staticmethod
    def test_pressyes(appium_driver):
        el = WebDriverWait(appium_driver, 20).until(
            EC.element_to_be_clickable((
                AppiumBy.XPATH, '//android.widget.TextView[@text="Yes"]'
            ))
        )
        el.click()

    @staticmethod
    def test_mobile_number(appium_driver):
        ele = WebDriverWait(appium_driver,20).until(
            EC.presence_of_element_located((
                AppiumBy.XPATH , '//android.widget.EditText[@text="Enter your mobile number"]'
            ))
        )

        ele.send_keys('8374076596')

        ele_next_button = WebDriverWait(appium_driver, 20).until(
            EC.element_to_be_clickable((
                AppiumBy.XPATH, '//android.view.ViewGroup[@resource-id="btnMobileLogIn"]'
            ))
        )
        ele_next_button.click()

        time.sleep(40)#otp button sleep for 40 sec

        otp_next_button = WebDriverWait(appium_driver, 20).until(
            EC.element_to_be_clickable((
                AppiumBy.XPATH, '//android.widget.TextView[@text="Next"]'
            ))
        )
        otp_next_button.click()

        otp_verification_ok_button = WebDriverWait(appium_driver, 20).until(
            EC.element_to_be_clickable((
                AppiumBy.XPATH, '//android.widget.TextView[@text="OK"]'
            ))
        )
        otp_verification_ok_button.click()
################################################ notification button  ##############################################################################################################
    # notification_button.click()
    # notification_back_button = WebDriverWait(appium_driver, 20).until(
    #     EC.element_to_be_clickable((
    #         AppiumBy.XPATH, '//android.widget.ImageView'
    #     ))
    # )
    # notification_back_button.click()
    @staticmethod
    def test_notification_button(appium_driver):
        notification_button = WebDriverWait(appium_driver, 20).until(
            EC.element_to_be_clickable((
                AppiumBy.XPATH, '//android.view.ViewGroup[@resource-id="dashNotiffBtn"]/android.widget.ImageView'
            ))
        )
        notification_button.click()
        notification_back_button = WebDriverWait(appium_driver, 20).until(
            EC.element_to_be_clickable((
                AppiumBy.XPATH, '//android.widget.ImageView'
            ))
        )
        notification_back_button.click()

    def test_notification_clear_button(self,appium_driver):
        notification_clear_button = WebDriverWait(appium_driver, 20).until(
            EC.element_to_be_clickable((
                AppiumBy.XPATH, '//android.widget.TextView[@text="Clear"]'
            ))
        )
        notification_clear_button.click()
        clear_button_no = WebDriverWait(appium_driver, 20).until(
            EC.element_to_be_clickable((
                AppiumBy.XPATH, '//android.widget.TextView[@text="No"]'
            ))
        )
        clear_button_no.click()

    def test_clear_notification_yes(self,appium_driver):
        notification_clear_button = WebDriverWait(appium_driver, 20).until(
            EC.element_to_be_clickable((
                AppiumBy.XPATH, '//android.widget.TextView[@text="Clear"]'
            ))
        )
        notification_clear_button.click()

        clear_yes_button = WebDriverWait(appium_driver, 20).until(
            EC.element_to_be_clickable((
                AppiumBy.XPATH, '//android.widget.TextView[@text="Yes"]'
            ))
        )
        clear_yes_button.click()
        allclear_ok_button = WebDriverWait(appium_driver, 20).until(
            EC.element_to_be_clickable((
                AppiumBy.XPATH, '//android.widget.TextView[@text="OK"]'
            ))
        )
        allclear_ok_button.click()

    def test_notification_back_button(self,appium_driver):
        notification_back_button = WebDriverWait(appium_driver, 20).until(
            EC.element_to_be_clickable((
                AppiumBy.XPATH, '//android.widget.ImageView'
            ))
        )
        notification_back_button.click()

##############################################################################################################################################
    @staticmethod
    def test_account(appium_driver):
        account_button = WebDriverWait(appium_driver, 20).until(
            EC.element_to_be_clickable((
                AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.ImageView'
            ))
        )
        account_button.click()
#####################################################################################################
    @staticmethod
    def test_dutystatus_on(appium_driver):
        dutystatus_on_button = WebDriverWait(appium_driver, 20).until(
            EC.element_to_be_clickable((
                AppiumBy.XPATH, '//android.widget.TextView[@text="OFF"]'
            ))
        )
        dutystatus_on_button.click()
    def test_dutystatus_off(self,appium_driver):
        dutystatus_off_button = WebDriverWait(appium_driver, 20).until(
            EC.element_to_be_clickable((
                AppiumBy.XPATH, '//android.widget.TextView[@text="ON"]'
            ))
        )
        dutystatus_off_button.click()
##################################################################################################
    def test_Profile_picture(self,appium_driver):
        profile_button = WebDriverWait(appium_driver, 20).until(
            EC.element_to_be_clickable((
                AppiumBy.XPATH, '//android.view.ViewGroup[@resource-id="dashProfileBtn"]/android.widget.ImageView'
            ))
        )
        profile_button.click()
        camera_button = WebDriverWait(appium_driver, 20).until(
            EC.element_to_be_clickable((
                AppiumBy.XPATH, '//android.view.ViewGroup[@resource-id="modalClose1"]/android.widget.ImageView'
            ))
        )
        camera_button.click()

####################################################################################################
    @staticmethod
    def test_logout_button(appium_driver):
        logout_button = WebDriverWait(appium_driver, 20).until(
            EC.element_to_be_clickable((
                AppiumBy.XPATH, '//android.widget.TextView[@text="Logout"]'
            ))
        )
        logout_button.click()
        logoutyes_button = WebDriverWait(appium_driver, 20).until(
            EC.element_to_be_clickable((
                AppiumBy.XPATH, '//android.widget.TextView[@text="Yes"]'
            ))
        )
        logoutyes_button.click()
##################### ###############################################################################################################
    def test_logout_button_forno(self, appium_driver):
            logout_button = WebDriverWait(appium_driver, 20).until(
                EC.element_to_be_clickable((
                    AppiumBy.XPATH, '//android.widget.TextView[@text="Logout"]'
                ))
            )
            logout_button.click()
            logoutno_button = WebDriverWait(appium_driver, 20).until(
                EC.element_to_be_clickable((
                    AppiumBy.XPATH, '//android.widget.TextView[@text="No"]'
                ))
            )
            logoutno_button.click()

    @staticmethod
    def test_performance_button(appium_driver):
        performance_button = WebDriverWait(appium_driver, 20).until(
            EC.element_to_be_clickable((
                AppiumBy.XPATH, '//android.widget.Button[@content-desc="Performance, tab, 3 of 3"]/android.view.ViewGroup/android.widget.ImageView'
            ))
        )

        performance_button.click()



    def test_dropdown_alldata_button(self, appium_driver):
        dropdown_button = WebDriverWait(appium_driver, 20).until(
            EC.element_to_be_clickable((
                AppiumBy.XPATH,
                '//android.view.ViewGroup[@resource-id="selectBtn"]/android.widget.ImageView'
            ))
        )

        dropdown_button.click()
        alldata_button = WebDriverWait(appium_driver, 20).until(
            EC.element_to_be_clickable((
                AppiumBy.XPATH, '//android.widget.TextView[@text="All data"]'
            ))
        )
        alldata_button.click()
#####################################################################################
    def test_dropdown_monthly_button(self, appium_driver):
        dropdown_button = WebDriverWait(appium_driver, 20).until(
            EC.element_to_be_clickable((
                AppiumBy.XPATH,
                '//android.view.ViewGroup[@resource-id="selectBtn"]/android.widget.ImageView'
            ))
        )

        dropdown_button.click()
        monthly_button = WebDriverWait(appium_driver, 20).until(
            EC.element_to_be_clickable((
                AppiumBy.XPATH, '//android.widget.TextView[@text="Monthly"]'
            ))
        )
        monthly_button.click()
 ##########################################################################################
    def test_dropdown_weekly_button(self, appium_driver):
        dropdown_button = WebDriverWait(appium_driver, 20).until(
            EC.element_to_be_clickable((
                AppiumBy.XPATH,
                '//android.view.ViewGroup[@resource-id="selectBtn"]/android.widget.ImageView'
            ))
        )

        dropdown_button.click()
        weekly_button = WebDriverWait(appium_driver, 20).until(
            EC.element_to_be_clickable((
                AppiumBy.XPATH, '//android.widget.TextView[@text="Weekly"]'
            ))
        )
        weekly_button.click()
  #########################################################################################################
    @staticmethod
    def test_myorders( appium_driver):
        myorders_button = WebDriverWait(appium_driver, 20).until(
            EC.element_to_be_clickable((
                AppiumBy.XPATH, '//android.widget.Button[@content-desc="Dashboard, tab, 1 of 3"]/android.view.ViewGroup/android.widget.ImageView'
            ))
        )
        myorders_button.click()
####################################################################################
    def test_dropdown_myorders_ongoing(self,appium_driver):
        dropdown_orders = WebDriverWait(appium_driver, 20).until(
            EC.element_to_be_clickable((
                AppiumBy.XPATH,
                '//android.view.ViewGroup[@resource-id="dropdownTest"]'
            ))
        )
        dropdown_orders.click()
        ongoing_button = WebDriverWait(appium_driver, 20).until(
            EC.element_to_be_clickable((
                AppiumBy.XPATH, '//android.widget.TextView[@text="Ongoing"]'
            ))
        )
        ongoing_button.click()
########################################## zoom in zoom out  #################################################################
    def test_orderdetails_button(self, appium_driver):
        orderdetails_button = WebDriverWait(appium_driver, 20).until(
            EC.element_to_be_clickable((
                AppiumBy.XPATH,
                '(//android.widget.TextView[@text="Order Details"])[1]'
            ))
        )
        orderdetails_button.click()
        locatemap_button = WebDriverWait(appium_driver, 20).until(
            EC.element_to_be_clickable((
                AppiumBy.XPATH,
                '(//android.widget.TextView[@text="Locate on map"])[1]'
            ))
        )
        locatemap_button.click()
        zoomin_button = WebDriverWait(appium_driver, 20).until(
            EC.element_to_be_clickable((
                AppiumBy.XPATH,
                '//android.widget.ImageView[@content-desc="Zoom in"]'
            ))
        )
        zoomin_button.click()
        zoomout_button = WebDriverWait(appium_driver, 20).until(
            EC.element_to_be_clickable((
                AppiumBy.XPATH,
                '//android.widget.ImageView[@content-desc="Zoom out"]'
            ))
        )
        zoomout_button.click()
        back_button = WebDriverWait(appium_driver, 20).until(
            EC.element_to_be_clickable((
                AppiumBy.XPATH,
                '//android.view.ViewGroup[@resource-id="button-back"]/android.widget.ImageView'
            ))
        )
        back_button.click()
        backtohomepage_button = WebDriverWait(appium_driver, 20).until(
            EC.element_to_be_clickable((
                AppiumBy.XPATH,
                '//android.view.ViewGroup[@resource-id="backBtn"]'
            ))
        )
        backtohomepage_button.click()
############################################ zoom in zoom out2 ##########################################
    def test_orderdetails_button_second(self, appium_driver):
        orderdetails_button = WebDriverWait(appium_driver, 20).until(
            EC.element_to_be_clickable((
                AppiumBy.XPATH,
                '(//android.widget.TextView[@text="Order Details"])[2]'
            ))
        )
        orderdetails_button.click()
        locatemap_button = WebDriverWait(appium_driver, 20).until(
            EC.element_to_be_clickable((
                AppiumBy.XPATH,
                '(//android.widget.TextView[@text="Locate on map"])[2]'
            ))
        )
        locatemap_button.click()
        zoomin_button = WebDriverWait(appium_driver, 20).until(
            EC.element_to_be_clickable((
                AppiumBy.XPATH,
                '//android.widget.ImageView[@content-desc="Zoom in"]'
            ))
        )
        zoomin_button.click()
        zoomout_button = WebDriverWait(appium_driver, 20).until(
            EC.element_to_be_clickable((
                AppiumBy.XPATH,
                '//android.widget.ImageView[@content-desc="Zoom out"]'
            ))
        )
        zoomout_button.click()
        back_button = WebDriverWait(appium_driver, 20).until(
            EC.element_to_be_clickable((
                AppiumBy.XPATH,
                '//android.view.ViewGroup[@resource-id="button-back"]/android.widget.ImageView'
            ))
        )
        back_button.click()
        backtohomepage_button = WebDriverWait(appium_driver, 20).until(
            EC.element_to_be_clickable((
                AppiumBy.XPATH,
                '//android.view.ViewGroup[@resource-id="backBtn"]'
            ))
        )
        backtohomepage_button.click()
#########################################################################################################
    @staticmethod
    def test_dropdown_myorders_completed(appium_driver):
        dropdown_orders = WebDriverWait(appium_driver, 20).until(
            EC.element_to_be_clickable((
                AppiumBy.XPATH,
                '//android.view.ViewGroup[@resource-id="dropdownTest"]'
            ))
        )
        dropdown_orders.click()

        completed_button = WebDriverWait(appium_driver, 20).until(
            EC.element_to_be_clickable((
                AppiumBy.XPATH, '//android.widget.TextView[@text="Completed"]'
            ))
        )
        completed_button.click()
        # order_completed_button = WebDriverWait(appium_driver, 20).until(
        #     EC.element_to_be_clickable((
        #         AppiumBy.XPATH,
        #         '//android.widget.TextView[@text="Order Details"]'
        #     ))
        # )
        # order_completed_button.click()
#################################################################################################################
    def test_orderdetails_button_completed(self, appium_driver):
        order_completed_button = WebDriverWait(appium_driver, 20).until(
            EC.element_to_be_clickable((
                AppiumBy.XPATH,
                '//android.widget.TextView[@text="Order Details"]'
            ))
        )
        order_completed_button.click()
        # order_completed_ok_button = WebDriverWait(appium_driver, 20).until(
        #     EC.element_to_be_clickable((
        #         AppiumBy.XPATH,
        #         '//android.widget.TextView[@text="Okay"]'
        #     ))
        # )
        # order_completed_ok_button.click()

###################################################################################################################
    @staticmethod
    def test_payments(appium_driver):
        payment_button = WebDriverWait(appium_driver, 20).until(
            EC.element_to_be_clickable((
                AppiumBy.XPATH, '//android.widget.Button[@content-desc="Payments, tab, 2 of 3"]/android.widget.ImageView'
            ))
        )
        payment_button.click()
##################################################################################################################
    def test_startride(self, appium_driver):
        startride_button = WebDriverWait(appium_driver, 20).until(
            EC.element_to_be_clickable((
                AppiumBy.XPATH,
                '//android.widget.TextView[@text="Start Ride"]'
            ))
        )
        startride_button.click()
        clickok_button = WebDriverWait(appium_driver, 20).until(
            EC.element_to_be_clickable((
                AppiumBy.XPATH,
                '//android.widget.TextView[@text="OK"]'
            ))
        )
        clickok_button.click()
        time.sleep(30)
        startride_button = WebDriverWait(appium_driver, 20).until(
            EC.element_to_be_clickable((
                AppiumBy.XPATH,
                '//android.widget.TextView[@text="Start Ride"]'
            ))
        )
        startride_button.click()

        deliverycomplete_button = WebDriverWait(appium_driver, 20).until(
            EC.element_to_be_clickable((
                AppiumBy.XPATH,
                '//android.view.ViewGroup[@resource-id="DeliveryCompleteBtn"]'
            ))
        )
        deliverycomplete_button.click()
        deliveryok_button = WebDriverWait(appium_driver, 20).until(
            EC.element_to_be_clickable((
                AppiumBy.XPATH,
                '//android.widget.TextView[@text="OK"]'
            ))
        )
        deliveryok_button.click()
        time.sleep(20)
        delivery_checkbox = WebDriverWait(appium_driver, 20).until(
            EC.element_to_be_clickable((
                AppiumBy.XPATH,
                '//android.widget.TextView[@text=""]'
            ))
        )
        delivery_checkbox.click()
        delivery_complete = WebDriverWait(appium_driver, 20).until(
            EC.element_to_be_clickable((
                AppiumBy.XPATH,
                '//android.view.ViewGroup[@resource-id="DeliveryCompleteBtn2"]'
            ))
        )
        delivery_complete.click()
        delivery_ok_button = WebDriverWait(appium_driver, 20).until(
            EC.element_to_be_clickable((
                AppiumBy.XPATH,
                '//android.widget.TextView[@text="Okay"]'
            ))
        )
        delivery_ok_button.click()