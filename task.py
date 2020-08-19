# importing libraries
import selenium
from selenium import webdriver as wb

#using google chrome driver
webD=wb.Chrome('chromedriver.exe')
# opening the link
webD.get('https://www.magicbricks.com/property-for-sale/residential-real-estate?proptype=Multistorey-Apartment,Builder-Floor-Apartment,Penthouse,Studio-Apartment,Residential-House,Villa,Residential-Plot&cityName=Bangalore')


# function to extract URL from string
def getURL(string):
    from urlextract import URLExtract
    extractor = URLExtract()
    urls = extractor.find_urls(string)
    x1=str(urls[0]).find(',')
    return str(urls[0])[:x1-1]
    


# extracting all the link of the properties
propertyList=webD.find_elements_by_class_name('m-srp-card')
urls=[]
for i in propertyList:
    urls.append(getURL(i.get_attribute('data-code')))



from tqdm import tqdm
allDetails=[]
for i in tqdm(urls):
    #webD=wb.Chrome('chromedriver.exe')
    webD.get(i)
    
    try:
        Headline=webD.find_element_by_xpath('//*[@id="propertyDetailTabId"]/div[3]/div[1]/div/div[1]/div[3]/h1/span[1]').text
    except:
        Headline="NaN"
    try:
        Price=webD.find_element_by_xpath('//*[@id="priceSv"]').text
    except:
        Price="NaN"
    try:
        Address=webD.find_element_by_xpath('//*[@id="propDetailDescriptionId"]/div[2]/div/div[4]/div[2]').text
    except:
        Address="NaN"
    try:
        Bedrooms=webD.find_element_by_xpath('//*[@id="firstFoldDisplay"]/div[1]/div[2]/div').text
    except:
        Bedrooms="NaN"
    try:
        Lift=webD.find_element_by_xpath('//*[@id="propDetailDescriptionId"]/div[2]/div/div[8]/div[2]/div/div[1]').text
    except:
        Lift="Nan"
    try:
        Bathrooms=webD.find_element_by_xpath('//*[@id="firstFoldDisplay"]/div[2]/div[2]').text
    except:
        Bathrooms="NaN"
    try:
        Balcony=webD.find_element_by_xpath('//*[@id="firstFoldDisplay"]/div[3]/div[2]').text
    except:
        Balcony="NaN"
    try:
        SuperArea=webD.find_element_by_xpath('//*[@id="secondFoldDisplay"]/div[1]/div[2]').text
    except:
        SuperArea="NaN"  
    try:
        Status=webD.find_element_by_xpath('//*[@id="fourthFoldDisplay"]/div[1]/div[2]').text
    except:
        Status="NaN"
    try:
        TransactionType=webD.find_element_by_xpath('//*[@id="fourthFoldDisplay"]/div[2]/div[2]').text
    except:
        TransactionType="NaN"
    try:
        Floor=webD.find_element_by_xpath('//*[@id="fourthFoldDisplay"]/div[3]/div[2]').text
    except:
        Floor="Nan"
    try:
        Carparking=webD.find_element_by_xpath('//*[@id="fourthFoldDisplay"]/div[1]/div[2]').text
    except:
        Carparking="NaN"
    try:
        Furnishedstatus=webD.find_element_by_xpath('//*[@id="fourthFoldDisplay"]/div[4]/div[2]').text
    except:
        Furnishedstatus="NaN"
    try:
        Description=webD.find_element_by_xpath('//*[@id="propDetailDescriptionId"]/div[2]/div/div[1]').text
    except:
        Description="NaN"
    try:
        Pricebreakup=webD.find_element_by_xpath('//*[@id="propDetailDescriptionId"]/div[2]/div/div[2]/div[2]').text
    except:
        Pricebreakup="NaN"
    try:
        Landmarks=webD.find_element_by_xpath('//*[@id="propDetailDescriptionId"]/div[2]/div/div[6]/div[2]').text
    except:
        Landmarks="NaN"

    Ageofconstruction="NaN"
    Pricecomparison="NaN"
    Expectedrent="NaN"
    MonthlyEMI="NaN"
    try:
        OwnerBuilder=webD.find_element_by_xpath('//*[@id="thirdFoldDisplay"]/div[1]/div[2]/span/a').text
    except:
        OwnerBuilder="Nan"
    try:
        TypeofOwnership=webD.find_element_by_xpath('//*[@id="thirdFoldDisplay"]/div[2]/div[2]').text
    except:
        TypeofOwnership="NaN"
    try:
        Pricepersqft=webD.find_element_by_xpath('//*[@id="secondFoldDisplay"]/div[1]/div[3]').text
    except:
        Pricepersqft="NaN"
    
    
    data={
    'Headline':Headline,
    'Price':Price,
    'Address':Address,
    'Bedrooms':Bedrooms,
    'Bathrooms':Bathrooms,
    'Balcony':Balcony,
    'Super Area':SuperArea,
    'Price per sqft':Pricepersqft,
    'Status':Status,
    'Transaction Type':TransactionType,
    'Floor':Floor,
    'Car parking':Carparking,
    'Furnished status':Furnishedstatus,
    'Lifts':Lift,
    'Description':Description,
    'Price breakup':Pricebreakup,
    'Landmarks':Landmarks,
    'Age of construction':Ageofconstruction,
    'Price comparison':Pricecomparison,
    'Expected rent':Expectedrent,
    'Monthly EMI':MonthlyEMI,
    'Owner/Builder':OwnerBuilder,
    'Type of Ownership':TypeofOwnership
    }
    allDetails.append(data)


# library to convert all the data into dataframe
import pandas as pd

df=pd.DataFrame(allDetails)
# saving the data
df.to_csv('OutPut.csv')
