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