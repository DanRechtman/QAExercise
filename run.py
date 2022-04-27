
from __future__ import annotations
from locators import Locators
from data import Data, Results

from selenium.webdriver.common.by import By

from selenium.webdriver.chromium.service import ChromiumService
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from time import sleep


## Sources that helped: https://medium.com/@asheeshmisra29/web-automation-selenium-webdriver-and-python-getting-started-part-3-a9c07143d36d 

class BasePage:
    """Basepage, class where all other pages extend from"""
    def __init__(self,driver:webdriver.Chrome) -> None:
        """__init__

        Args:
            driver (WebDriver): WebDriver
        """
        self.driver = driver
        
        
class MainPage(BasePage):
    
    def click_home(self)->MapPage:
        # self.driver.find_element(*Locators.BTN_FindHome).click()
        WebDriverWait(self.driver,100).until(EC.visibility_of_element_located(Locators.BTN_FindHome)).click()
        return MapPage(driver=self.driver)


class MapPage(BasePage):
    result = Results()

    def click_filter(self)->MapPage:
        WebDriverWait(self.driver,100).until(EC.visibility_of_element_located(Locators.BTN_filter)).click()
        return self
    
    def select_residential(self)->MapPage:
        WebDriverWait(self.driver,100).until(EC.visibility_of_element_located((By.ID,"select2-ddlPropertyTypeRes-container"))).click()
        WebDriverWait(self.driver,100).until(EC.visibility_of_element_located((By.XPATH,"/html/body/span/span/span[2]/ul/li[2]"))).click()
        
        
        
        return self
    def select_townhouse(self)->MapPage:
        WebDriverWait(self.driver,100).until(EC.visibility_of_element_located(Locators.BTN_Dropdown_Building_Type)).click()
        WebDriverWait(self.driver,100).until(EC.visibility_of_element_located(Locators.BTN_Dropdown_Select_Building_Type)).click()
        return self
    def select_bed(self)->MapPage:
        WebDriverWait(self.driver,100).until(EC.visibility_of_element_located(Locators.BTN_Dropdown_Bed_Num)).click()
        WebDriverWait(self.driver,100).until(EC.visibility_of_element_located(Locators.BTN_Dropdown_Select_Bed_Num)).click()
        return self
    def select_bath(self)->MapPage:
        WebDriverWait(self.driver,100).until(EC.visibility_of_element_located(Locators.BTN_Dropdown_Bath_Num)).click()
        WebDriverWait(self.driver,100).until(EC.visibility_of_element_located(Locators.BTN_Dropdown_Select_Bath_Num)).click()
        return self
    
    def select_area(self,keys)->MapPage:
        WebDriverWait(self.driver,100).until(EC.visibility_of_element_located(Locators.Input_Filter)).send_keys(keys+Keys.RETURN)
        return self
        
    def select_date(self)->MapPage:
        sleep(3)
        a= WebDriverWait(self.driver,100).until(EC.visibility_of_element_located(Locators.Filter_Date))
        self.driver.execute_script("arguments[0].removeAttribute('readonly')",a)
        a.send_keys("01/01/2022"+Keys.RETURN)
        WebDriverWait(self.driver,100).until(EC.visibility_of_element_located(Locators.BTN_filter_Search)).click()
        
        return self
    def select_search(self)->MapPage:
        WebDriverWait(self.driver,2).until(EC.visibility_of_element_located(Locators.Input_Filter)).click()
        # WebDriverWait(self.driver,100).until(EC.visibility_of_element_located(Locators.CLOSE)).click()
        
        return self
    def getTotalResult(self)->MapPage:
        sleep(6)

        el = self.driver.find_element(*Locators.Results)
        
        self.result.num = el.get_attribute("innerText")
        return self
    def sortResult(self):
        WebDriverWait(self.driver,100).until(EC.visibility_of_element_located(Locators.BTN_Dropdown_Price)).click()
        WebDriverWait(self.driver,100).until(EC.visibility_of_element_located(Locators.BTN_Dropdown_Price)).send_keys(Keys.DOWN,Keys.DOWN,Keys.DOWN,Keys.DOWN,Keys.RETURN)

        
        return self
    
    def clickCard(self):
        sleep(2)
        WebDriverWait(self.driver,100).until(EC.visibility_of_element_located(Locators.card)).click()
        chwd = self.driver.window_handles
        p = self.driver.current_window_handle
        for w in chwd:
            if(w!=p):
                self.driver.switch_to.window(w)
        return self
    def getData(self):
        self.result.price = driver.find_element(By.ID,"listingPrice").get_attribute("innerText")
        self.result.address = driver.find_element(By.ID,"listingAddress").get_attribute("innerText")
        self.result.mls = driver.find_element(By.ID,"listingMLSNum").get_attribute("innerText")
        self.result.summary = driver.find_element(By.ID,"propertyDescriptionCon").get_attribute("innerText")

    
if __name__ =="__main__":
    
    service = ChromiumService(Data.CHROME_EXEC,start_error_message="Error")
    driver = webdriver.Chrome(service=service)

    driver.get(Data.BASE_URL)
    
    mapPage = MainPage(driver=driver).click_home()
    mapPage.click_filter()\
           .select_residential()\
           .select_townhouse()\
           .select_bed()\
           .select_bath()\
           .select_area("Richmond Hill, Ontario")\
           .click_filter()\
           .select_date()\
           .getTotalResult()\
           .sortResult()\
           .clickCard()\
           .getData()
    driver.get(Data.BASE_URL)
    mapPage = MainPage(driver=driver).click_home()
    mapPage.click_filter()\
           .select_residential()\
           .select_townhouse()\
           .select_bed()\
           .select_bath()\
           .select_area("Scarborough, Ontario")\
           .click_filter()\
           .select_date()\
           .getTotalResult()\
           .sortResult()\
           .clickCard()\
           .getData()
    print(mapPage.result)
    sleep(100)
                          

    
    