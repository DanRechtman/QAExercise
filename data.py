from dataclasses import dataclass


class Data:
    CHROME_EXEC = "C:/Users/minic/Downloads/chromedriver_win32/chromedriver.exe"    
    
    BASE_URL = "https://www.realtor.ca/"
    
    
@dataclass
class Results:
    num: str =""
    price: str =""
    address: str =""
    mls: str = ""
    summary: str=""