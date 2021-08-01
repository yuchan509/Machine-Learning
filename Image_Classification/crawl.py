# Crawling.
from urllib.request import urlretrieve # Save network objects (documents from URL addresses) as local files
from urllib.parse import quote_plus    # korean support
from bs4 import BeautifulSoup as bs    # Essential module
from selenium import webdriver         # Google crolling
import os

keyword = input( "Input keyword : " )
crawl_n = int( input( "Input count : ") )
URL     = "https://www.google.com/search?q=" + str( keyword ) + "&hl=ko&tbm=isch"
driver  = webdriver.Chrome('c:/chromedriver.exe')
options = webdriver.ChromeOptions()
options.add_experimental_option( 'excludeSwitches', ['enable-logging'] )
driver.get(URL)

html    = driver.page_source
soup    = bs( html, features="html.parser" )
img     = soup.select('img')
s_list  = []
n       = 1

dir_path = './img/'
os.mkdir(dir_path + "/" + keyword + "/")
path     = dir_path + '/' + keyword + '/'

print("Searching...")
for i in img:
    try:
        s_list.append( i.attrs["src"] )
    except KeyError:
        s_list.append( i.attrs["data-src"] )

print("Downloading...")
for i in s_list:
    print(n)
    urlretrieve( i, path + keyword + str(n) + ".jpg" )
    n+=1
    if n > crawl_n:
        break
    
driver.close()
print("Finish")