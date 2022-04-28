from __future__ import annotations

from time import sleep
import unittest
from datetime import datetime

from selenium.webdriver.common.by import By
from selenium.webdriver.chromium.service import ChromiumService
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import HtmlTestRunner


from locators import Locators
from data import Data, Results


# Sources that helped: https://medium.com/@asheeshmisra29/web-automation-selenium-webdriver-and-python-getting-started-part-3-a9c07143d36d

class BasePage:
    """Basepage, class where all other pages extend from"""
    def __init__(self,driver:webdriver.Chrome) -> None:
        """__init__

        Args:
            driver (webdriver): webdriver
        """
        self.driver = driver
class MainPage(BasePage):
    """MainPage

    Args:
        BasePage (webdriver): webdriver
    """
    def click_home(self)->MapPage:
        """click_home

        Returns:
            MapPage: this
        """
        # self.driver.find_element(*Locators.BTN_FindHome).click()
        self.driver.get(Data.BASE_URL)
        WebDriverWait(self.driver,100).until(EC.visibility_of_element_located(Locators.BTN_FindHome)).click()
        return MapPage(driver=self.driver)


class MapPage(BasePage):
    """MapPage /map of realtor.ca

    Args:
        BasePage (webdriver): webdriver

    """
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
        WebDriverWait(self.driver,100).until(EC.visibility_of_element_located(Locators.Input_Filter)).send_keys(keys)
        return self
        
    def select_date(self)->MapPage:
        sleep(3)
        a= WebDriverWait(self.driver,100).until(EC.visibility_of_element_located(Locators.Filter_Date))
        self.driver.execute_script("arguments[0].removeAttribute('readonly')",a)
        a.send_keys("01/01/2022")
        # WebDriverWait(self.driver,100).until(EC.visibility_of_element_located(Locators.BTN_filter_Search)).click()
        
        return self
    def select_search(self)->MapPage:
        WebDriverWait(self.driver,100).until(EC.visibility_of_element_located((By.ID,"mapMoreFiltersSearchBtn"))).click()
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
        self.result.price = self.driver.find_element(By.ID,"listingPrice").get_attribute("innerText")
        self.result.address = self.driver.find_element(By.ID,"listingAddress").get_attribute("innerText")
        self.result.mls = self.driver.find_element(By.ID,"listingMLSNum").get_attribute("innerText")
        self.result.summary = self.driver.find_element(By.ID,"propertyDescriptionCon").get_attribute("innerText")
        return self

class Test_Home_Base(unittest.TestCase):
    
    driver = webdriver.Chrome(executable_path=Data.CHROME_EXEC)
    
    def setUp(self) -> None:
        # service = ChromiumService(Data.CHROME_EXEC,start_error_message="Error")
        # self.driver = webdriver.Chrome(service=service)
        self.start = datetime.now()
        
        
    def tearDown(self) -> None:
        # self.driver.close()
        # self.driver.quit()
        self.end = datetime.now()
        diff = self.end - self.start
        print(diff.microseconds/1000,"ms")

class Test_Home(Test_Home_Base):
    cPAGE:MapPage = None
    # def setUp(self):
    #     return super().setUp()
    def test_01_home_page(self):

        m= MainPage(driver=self.driver).click_home()
        self.cPAGE = m
        self.assertIn("https://www.realtor.ca/map",m.driver.current_url)
        # m.click_filter()
        # self.assertEqual("","")
        
    def test_02_filter(self):
        
        MapPage(driver=self.driver).click_filter()
        box = self.driver.find_element(By.ID,"mapSearchMoreCon")
        self.assertTrue(box.is_displayed())
    def test_03_res(self):
        MapPage(driver=self.driver).select_residential()
        box = self.driver.find_element(By.ID,"select2-ddlPropertyTypeRes-container")
        self.assertEqual("Residential",box.text)
    def test_04_town(self):
        MapPage(driver=self.driver).select_townhouse()
        box = self.driver.find_element(By.ID,"select2-ddlBuildingType-container").text
        self.assertEqual("Row / Townhouse",box)
        

    def test_05_bed_bath(self):
        MapPage(driver=self.driver).select_bed().select_bath()
        bed = self.driver.find_element(*Locators.BTN_Dropdown_Bed_Num).text
        bath = self.driver.find_element(*Locators.BTN_Dropdown_Bath_Num).text
        self.assertEqual("3",bed)
        self.assertEqual("3",bath)
        
    def test_06_area(self):
        MapPage(driver=self.driver).select_area("Richmond Hill, Ontario")
        box = self.driver.find_element(By.ID,"mapMoreSearchTxt")
        value = box.get_attribute("value")
        self.assertEqual("Richmond Hill, Ontario",value)
    
    def test_07_date(self):
        MapPage(driver=self.driver).select_date()
        box = self.driver.find_element(*Locators.Filter_Date)
        value = box.get_attribute("value")
        self.assertEqual("01/01/2022",value)
    def test_08_Search(self):
        MapPage(driver=self.driver).select_search()
        sleep(1)
        box = self.driver.find_element(By.ID,"mapSearchMoreCon")
        self.assertEqual(False,box.is_displayed())
    def test_09_results(self):
        result = int(MapPage(driver=self.driver).getTotalResult().result.num)
        self.assertIsInstance(result,int)
        print(f"{result=}")
        
    def test_10_info(self):
        House = MapPage(driver=self.driver).sortResult().clickCard().getData().result
        self.assertIsInstance(House,Results)
        
        print(f"{House.price=}")
        print(f"{House.address=}")
        print(f"{House.mls=}")
        print(f"{House.summary=}")
          
if __name__ =="__main__":
    # service = ChromiumService(Data.CHROME_EXEC,start_error_message="Error")
    # driver = webdriver.Chrome(service=service)
    # driver.get(Data.BASE_URL)
    # mapPage = MainPage(driver=driver).click_home()
    # mapPage.click_filter()\
    #        .select_residential()\
    #        .select_townhouse()\
    #        .select_bed()\
    #        .select_bath()\
    #        .select_area("Richmond Hill, Ontario")\
    #        .click_filter()\
    #        .select_date()\
    #        .getTotalResult()\
    #        .sortResult()\
    #        .clickCard()\
    #        .getData()
    # driver.get(Data.BASE_URL)
    # mapPage = MainPage(driver=driver).click_home()
    # mapPage.click_filter()\
    #        .select_residential()\
    #        .select_townhouse()\
    #        .select_bed()\
    #        .select_bath()\
    #        .select_area("Scarborough, Ontario")\
    #        .click_filter()\
    #        .select_date()\
    #        .getTotalResult()\
    #        .sortResult()\
    #        .clickCard()\
    #        .getData()
    # print(mapPage.result)
    # Test_Home().test_home_page()
    # runner = unittest.TextTestRunner(failfast=True)
    # runner.run(suite())
    # template_args={
    #     "time" : 
    # }
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(add_timestamp=True))
    # sleep(1)
                          

    