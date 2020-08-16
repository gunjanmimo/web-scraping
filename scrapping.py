from bs4 import BeautifulSoup as soup  # HTML data structure
from urllib.request import urlopen as uReq  # Web client
# html file writing function
def htmlWrite(a):
    f= open("test.html","a")
    #print("writing Data...")
    f.write(str(a))
    f.close()

# ! csv file strore
fileName = "product.csv"
f= open(fileName,"w")
headers="title, price\n"
f.write(headers)

# URl to web scrap from.
# in this example we web scrap graphics cards from Newegg.com
page_url = "http://www.newegg.com/Product/ProductList.aspx?Submit=ENE&N=-1&IsNodeId=1&Description=GTX&bop=And&Page=1&PageSize=36&order=BESTMATCH"

# opens the connection and downloads html page from url
uClient = uReq(page_url)

# parses html into a soup data structure to traverse html
# as if it were a json data type.
page_soup = soup(uClient.read(), "html.parser")
uClient.close()

# finds each product from the store page
containers = page_soup.findAll("div", {"class": "item-container"})

# print("total containers:",len(containers))
# container = containers[0]
# print("writing HTML...")
# htmlWrite(container)



#finding price of the products
price=page_soup.findAll("li",{"class":"price-current"})
# print(len(price))
# print(len(containers))
# print("saving Data...")
# htmlWrite(price[0].strong.text+" $")

i=0
for container in containers:
    for p in price:
        title=container.a.img['title']
        productPrice=p.strong.text
        # htmlWrite("product:{}".format(i)+"\n"+container.a.img['title']+"\n"+"price: "+p.strong.text+" $\n\n")
        # i=i+1
        f.write(title+","+productPrice+"\n")


f.close()