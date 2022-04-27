from selenium.webdriver.common.by import By



class Locators:
    
    # HOME PAGE
    BTN_FindHome = (By.XPATH,"/html/body/form/div[5]/span[2]/div/div[1]/a")
    
    
    ## MAP PAGE
    
    BTN_filter = (By.ID,"mapSearchMoreBtn")
    
    
    BTN_Dropdown_Building_Type = (By.XPATH,"/html/body/div[9]/div[3]/div[22]/span/span[1]/span")
    BTN_Dropdown_Select_Building_Type = (By.XPATH,"/html/body/span/span/span[2]/ul/li[3]")
    
    
    BTN_Dropdown_Bed_Num = (By.ID,"select2-ddlBeds-container")
    
    # BTN_Dropdown_Bed_Num = (By.XPATH,"/html/body/div[9]/div[3]/div[18]/span/span[1]/span/span[1]")
    BTN_Dropdown_Select_Bed_Num = (By.XPATH,"/html/body/span/span/span[2]/ul/li[6]")
    
    
    
    BTN_Dropdown_Bath_Num = (By.ID,"select2-ddlBaths-container")
    
    # BTN_Dropdown_Bath_Num = (By.XPATH,"/html/body/div[9]/div[3]/div[19]/span/span[1]/span/span[1]")
    BTN_Dropdown_Select_Bath_Num =(By.XPATH,"/html/body/span/span/span[2]/ul/li[6]")
    
    Filter_Date=(By.ID,"dteListedSince")
    
    
    # Filter_Date=(By.XPATH,"/html/body/div[9]/div[3]/div[21]/div/div/input")
    
    BTN_filter_Search=(By.ID,"mapMoreFiltersSearchBtn")
    
    Input_Filter=(By.ID,"mapMoreSearchTxt") 
    CLOSE=(By.ID,"mapMoreFiltersCloseBtn")
    Input_Element=(By.ID,"txtMapSearchInput")
    
    #Highest 
    BTN_Dropdown_Price = (By.XPATH,"/html/body/form/div[5]/div[2]/span/div/div[3]/div/div[1]/div[2]/div[2]/div[2]/div[2]/span/span[1]/span")

    Results = (By.ID,"mapResultsNumVal")
    
    card = (By.CLASS_NAME,"cardCon")
    
    
    
    
    