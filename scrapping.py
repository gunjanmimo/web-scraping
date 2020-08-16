from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup 

#writing function
def write(a):
    f = open('test.html',"a")
    f.write(str(a))
    f.close()




myURL= "https://www.newegg.com/global/in-en/Storage/EventSaleStore/ID-878?cm_sp=TOPVGAStore"

#opening up the connection, grabbing the page

uClient = uReq(myURL)
pageHTML= uClient.read()
uClient.close()


pageSOUP = soup(pageHTML,"html.parser")

#grab each product
containers = pageSOUP.findAll("div",{"class":"item-cell"})

container = containers[1]
write(container.a )