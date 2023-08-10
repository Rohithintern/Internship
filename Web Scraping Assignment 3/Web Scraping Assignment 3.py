#!/usr/bin/env python
# coding: utf-8

# In[1]:


import selenium
from selenium import webdriver
import pandas as pd
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException,StaleElementReferenceException
import time

import warnings
warnings.filterwarnings('ignore')


# 1. Write a python program which searches all the product under a particular product from www.amazon.in. The product to be searched will be taken as input from user. For e.g. If user input is ‘guitar’. Then search for guitars.

# In[ ]:


driver = webdriver.Chrome(r'/Users/Rohith/FlipRobo/chromedriver')
driver.get('https://www.amazon.in')


# In[ ]:


prod = input('Enter what you want to search :')


# In[ ]:


search = driver.find_element(By.XPATH,'/html/body/div[1]/header/div/div[1]/div[2]/div/form/div[2]/div[1]/input')
search.send_keys(prod)
search.submit()


# 2. In the above question, now scrape the following details of each product listed in first 3 pages of your search results and save it in a data frame and csv. In case if any product has less than 3 pages in search results then scrape all the products available under that product name. Details to be scraped are: "Brand Name", "Name of the Product", "Price", "Return/Exchange", "Expected Delivery", "Availability" and “Product URL”. In case, if any of the details are missing for any of the product then replace it by “-“.

# In[ ]:


name,price,dilevery,url = [],[],[],[]
for i in driver.find_elements(By.XPATH,"//span[@class = 'a-size-base-plus a-color-base a-text-normal']"):
    name.append(i.text)
for i in driver.find_elements(By.XPATH,"//span[@class = 'a-price-whole']"):
    price.append(i.text)
for i in driver.find_elements(By.XPATH,"//span[@class = 'a-color-base a-text-bold']"):
    dilevery.append(i.text)
for i in driver.find_elements(By.XPATH,"//a[@class = 'a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal']"):
    url.append(i.get_attribute('href'))


# In[94]:


nex = driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div[1]/div[1]/div/span[3]/div[2]/div[66]/div/div/span/a[3]')
nex.click()


# In[95]:


for i in driver.find_elements(By.XPATH,"//span[@class = 'a-size-base-plus a-color-base a-text-normal']"):
    name.append(i.text)
for i in driver.find_elements(By.XPATH,"//span[@class = 'a-price-whole']"):
    price.append(i.text)
for i in driver.find_elements(By.XPATH,"//span[@class = 'a-color-base a-text-bold']"):
    dilevery.append(i.text)
for i in driver.find_elements(By.XPATH,"//a[@class = 'a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal']"):
    url.append(i.get_attribute('href'))


# In[98]:


nex = driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div[1]/div[1]/div/span[3]/div[2]/div[65]/div/div/span/a[4]')
nex.click()


# In[99]:


for i in driver.find_elements(By.XPATH,"//span[@class = 'a-size-base-plus a-color-base a-text-normal']"):
    name.append(i.text)
for i in driver.find_elements(By.XPATH,"//span[@class = 'a-price-whole']"):
    price.append(i.text)
for i in driver.find_elements(By.XPATH,"//span[@class = 'a-color-base a-text-bold']"):
    dilevery.append(i.text)
for i in driver.find_elements(By.XPATH,"//a[@class = 'a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal']"):
    url.append(i.get_attribute('href'))


# In[100]:


len(name),len(price),len(dilevery),len(url)


# In[108]:


guti = pd.DataFrame({'Brand Name':name[0:182],'Price':price[0:182],'Expected Dilevery':dilevery,'Product URL':url[0:182],'Availability':'Available'})


# In[110]:


guti.to_csv('guitar.csv')


# In[112]:


df = pd.read_csv('guitar.csv')
df


# In[126]:


driver.close()


# 3. Write a python program to access the search bar and search button on images.google.com and scrape 10 images each for keywords ‘fruits’, ‘cars’ and ‘Machine Learning’, ‘Guitar’, ‘Cakes’.

# In[128]:


driver = webdriver.Chrome(r'/Users/Rohith/FlipRobo/chromedriver')
driver.get('https://images.google.com')


# In[129]:


search = driver.find_element(By.XPATH,'/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
search.send_keys('fruits')
search.submit()


# In[150]:


imag = []
for i in driver.find_elements(By.XPATH,'//img[@class = "rg_i Q4LuWd"]'):
    imag.append(i.get_attribute('src'))


# In[155]:


search = driver.find_element(By.XPATH,'/html/body/c-wiz/c-wiz/div/div[3]/div[2]/div/div[1]/form/div[1]/div[2]/div/div[2]/input')
search.clear()
delay = 2
search.send_keys('cars')
search.submit()


# In[156]:


car = []
for i in driver.find_elements(By.XPATH,'//img[@class = "rg_i Q4LuWd"]'):
    car.append(i.get_attribute('src'))


# In[158]:


search = driver.find_element(By.XPATH,'/html/body/c-wiz/c-wiz/div/div[3]/div[2]/div/div[1]/form/div[1]/div[2]/div/div[2]/input')
search.clear()
delay = 2
search.send_keys('machine learning')
search.submit()


# In[161]:


ml = []
for i in driver.find_elements(By.XPATH,'//img[@class = "rg_i Q4LuWd"]'):
    ml.append(i.get_attribute('src'))


# In[164]:


search = driver.find_element(By.XPATH,'/html/body/c-wiz/c-wiz/div/div[3]/div[2]/div/div[1]/form/div[1]/div[2]/div/div[2]/input')
search.clear()
delay = 2
search.send_keys('guitar')
search.submit()


# In[165]:


guitar = []
for i in driver.find_elements(By.XPATH,'//img[@class = "rg_i Q4LuWd"]'):
    guitar.append(i.get_attribute('src'))


# In[168]:


search = driver.find_element(By.XPATH,'/html/body/c-wiz/c-wiz/div/div[3]/div[2]/div/div[1]/form/div[1]/div[2]/div/div[2]/input')
search.clear()
delay = 2
search.send_keys('cake')
search.submit()


# In[169]:


cake = []
for i in driver.find_elements(By.XPATH,'//img[@class = "rg_i Q4LuWd"]'):
    cake.append(i.get_attribute('src'))


# In[180]:


d = pd.DataFrame({'Fruits':imag[0:10],'Cars':car[0:10],'Machine Learning':ml[0:10],'Guitar':guitar[0:10],'Cake':cake[0:10]})


# In[181]:


d.to_csv('image.csv')


# In[185]:


di = pd.read_csv('image.csv')
di.drop('Unnamed: 0',axis =1)


# In[186]:


driver.close()


# 4. Write a python program to search for a smartphone(e.g.: Oneplus Nord, pixel 4A, etc.) on www.flipkart.com and scrape following details for all the search results displayed on 1st page. Details to be scraped: “Brand Name”, “Smartphone name”, “Colour”, “RAM”, “Storage(ROM)”, “Primary Camera”, “Secondary Camera”, “Display Size”, “Battery Capacity”, “Price”, “Product URL”. Incase if any of the details is missing then replace it by “- “. Save your results in a dataframe and CSV.

# In[250]:


driver = webdriver.Chrome(r'/Users/Rohith/FlipRobo/chromedriver')
driver.get('https:www.flipkart.com')


# In[251]:


close = driver.find_element(By.XPATH,'/html/body/div[2]/div/div/button')
close.click()


# In[252]:


search = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div[1]/div[2]/div[2]/form/div/div/input')
search.send_keys('oneplus nord')
search.submit()


# In[253]:


brand,name,color = [],[],[]
for i in driver.find_elements(By.XPATH,'//div[@class = "_4rR01T"]'):
    brand.append(i.text.split(' ')[0])
    name.append(i.text)
    co = i.text.split('(')[-1]
    color.append(co.split(',')[0])


# In[254]:


ram,rom,pc,display,battery = [],[],[],[],[]
for i in driver.find_elements(By.XPATH,'//ul[@class="_1xgFaf"]'):
    display.append(i.text.split('\n')[1])
    battery.append(i.text.split('\n')[-2])
    
    ra = i.text.split('\n')[0]
    ram.append(ra.split('|')[0])
    rom.append(ra.split('|')[1])
    
    cam = i.text.split('\n')[2]
    pc.append(cam.split('|')[0])


# In[266]:


price,link = [],[]
for i in driver.find_elements(By.XPATH,'//div[@class="_30jeq3 _1_WHN1"]'):
    price.append(i.text)
for i in driver.find_elements(By.XPATH,"//a[@class = '_1fQZEK']"):
    link.append(i.get_attribute('href'))


# In[268]:


len(brand),len(name),len(color),len(ram),len(rom),len(pc),len(display),len(battery),len(price),len(link)


# In[269]:


pho = pd.DataFrame({'Brand Name':brand,'Smartphone Name':name,'Color':color,'RAM':ram,'Storage(ROM)':rom,'Camera':pc,'Display':display,'Battery':battery,'Price':price,'URL':link})


# In[271]:


pho.to_csv('Phone.csv')


# In[273]:


pd.read_csv('Phone.csv').head()


# In[275]:


driver.close()


# 5. Write a program to scrap geospatial coordinates (latitude, longitude) of a city searched on google maps.

# In[22]:


driver = webdriver.Chrome(r'/Users/Rohith/FlipRobo/chromedriver')
driver.get('https://www.google.com/maps')


# In[23]:


search = driver.find_element(By.XPATH,'/html/body/div[3]/div[9]/div[3]/div[1]/div[1]/div[1]/div[2]/form/div[2]/div[3]/div/input[1]')
search.send_keys('Mumbai')


# In[24]:


loc = driver.find_element(By.XPATH,'/html/body/div[3]/div[9]/div[3]/div[1]/div[1]/div[2]/div[2]/div[1]/div/div/div[1]/div/div[2]/div/div/div[1]')
loc.click()


# In[25]:


time.sleep(5)
url = driver.current_url


# In[26]:


ll = url.split('/')[-2]


# In[27]:


lat = ll.split(',')[0].replace('@','')
lon = ll.split(',')[1]


# In[28]:


print('Latitude = ',lat)
print('Longitude = ',lon)


# In[29]:


driver.close()


# 6. Write a program to scrap all the available details of best gaming laptops from digit.in.

# In[75]:


funding = pd.DataFrame({'January':january,'February':february,'March':march})
funding


# In[298]:


driver = webdriver.Chrome(r'/Users/Rohith/FlipRobo/chromedriver')
driver.get('https://www.digit.in')


# In[300]:


search = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div[2]/a/img')
search.click()
delay = 2
here = driver.find_element(By.XPATH,'/html/body/div[2]/div[2]/div/div/input')
here.send_keys('Best gaming laptop' + '\n')


# In[310]:


laptop,date = [],[]
for i in driver.find_elements(By.XPATH,'//div[@class="searchProduct-desc"]'):
    laptop.append(i.text)
for i in driver.find_elements(By.XPATH,'//div[@class = "searchPage"]'):
    date.append(i.text.split('\n')[-1])


# In[313]:


len(date),len(laptop)


# In[314]:


dig = pd.DataFrame({'Laptop Name':laptop,'Date':date})


# In[315]:


dig.to_csv('digit.csv')


# In[316]:


pd.read_csv('digit.csv').head()


# 7. Write a python program to scrape the details for all billionaires from www.forbes.com. Details to be
# scrapped: “Rank”, “Name”, “Net worth”, “Age”, “Citizenship”, “Source”, “Industry”.

# In[359]:


driver = webdriver.Chrome(r'/Users/Rohith/FlipRobo/chromedriver')
driver.get('https://www.forbes.com')


# In[360]:


expl = driver.find_element(By.XPATH,'/html/body/div[1]/header/nav/div[1]/button[1]')
expl.click()
time.sleep(2)


# In[361]:


bill = driver.find_element(By.XPATH,'/html/body/div[1]/header/nav/div[3]/ul/li[1]')
bill.click()


# In[362]:


al = driver.find_element(By.XPATH,'/html/body/div[1]/header/nav/div[3]/ul/li[1]/div[2]/ul/li[2]/a')
al.click()
time.sleep(2)


# In[364]:


rank,nam,net,age,sou,indust = [],[],[],[],[],[]
for i in driver.find_elements(By.XPATH,'//div[@class="table-row "]'):
    rank.append(i.text.split('\n')[0])
    nam.append(i.text.split('\n')[1])
    net.append(i.text.split('\n')[2])
    age.append(i.text.split('\n')[3])
    sou.append(i.text.split('\n')[4])
    indust.append(i.text.split('\n')[5])


# In[367]:


len(rank),len(nam),len(net),len(age),len(sou),len(indust)


# In[368]:


billa = pd.DataFrame({'Rank':rank,'Name':nam,'Net Worth':net,'Age':age,'Source':sou,'Industry':indust})


# In[370]:


billa.to_csv('Billionaries.csv')


# In[372]:


pd.read_csv('Billionaries.csv').head()


# In[373]:


driver.close()


# 8. Write a program to extract at least 500 Comments, Comment upvote and time when comment was posted
# from any YouTube Video.

# In[117]:


driver = webdriver.Chrome(r'/Users/Rohith/FlipRobo/chromedriver')
driver.get('https://www.youtube.com')


# In[134]:


search = driver.find_element(By.XPATH,'/html/body/ytd-app/div[1]/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div[1]/div[1]/input')
search.send_keys('Chaand Baaliyan - Aditya A. (Official Video)')
search.submit()
delay = 5


# In[135]:


song = driver.find_element(By.XPATH,'/html/body/ytd-app/div[1]/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-video-renderer[1]/div[1]/div/div[1]/div/h3/a/yt-formatted-string')
song.click()


# In[136]:


for _ in range(1000):
    driver.execute_script("window.scrollBy(0,1000)")


# In[146]:


op = []
for i in driver.find_elements(By.XPATH,'//div[@class="style-scope ytd-expander"]'):
    op.append(i.text)


# In[154]:


time = []
for i in driver.find_elements(By.XPATH,'//a[@class="yt-simple-endpoint style-scope yt-formatted-string"]'):
    time.append(i.text)


# In[164]:


ti = time[79:579]


# In[152]:


co = op[2:502]


# In[165]:


len(ti),len(co)


# In[167]:


comment = pd.DataFrame({'Comments':co,'Time':ti})


# In[168]:


comment.to_csv('Youtube.csv')


# In[170]:


df = pd.read_csv('Youtube.csv')
df.tail()


# 9. Write a python program to scrape a data for all available Hostels from https://www.hostelworld.com/ in
# “London” location. You have to scrape hostel name, distance from city centre, ratings, total reviews, overall reviews, privates from price, dorms from price, facilities and property description

# In[247]:


driver = webdriver.Chrome(r'/Users/Rohith/FlipRobo/chromedriver')
driver.get('https://www.hostelworld.com')


# In[232]:


try:
    search = driver.find_element(By.XPATH,'/html/body/div[3]/div/div/div[1]/div[1]/div/div[2]/div[4]/div/div[2]/div/div[1]/div/div/div/input')
    search.send_keys('london' + '\n')
    
    lon = driver.find_element(By.XPATH,'/html/body/div[3]/div/div/div[1]/div[1]/div/div[2]/div[4]/div/div[2]/div/div[1]/div/div/ul/li[2]')
    lon.click()
    
    
    go = driver.find_element(By.XPATH,'/html/body/div[3]/div/div/div[1]/div[1]/div/div[2]/div[4]/div/div[2]/div/div[5]/button')
    go.click()
    
    
except NoSuchElementException:
    driver.get('https://www.hostelworld.com/s?q=London,%20England&country=England&city=London&type=city&id=3&from=2022-08-01&to=2022-08-04&guests=2&HostelNumber=&page=1')


# In[233]:


name,dist,rat,price = [],[],[],[]
for i in driver.find_elements(By.XPATH,'//div[@class="property"]'):
    name.append(i.text.split('\n')[0])
    dist.append(i.text.split('\n')[1])
    rat.append(i.text.split('\n')[-3])
    review.append(i.text.split('\n')[-1])
for i in driver.find_elements(By.XPATH,'//div[@class="price title-5"]'):
    price.append(i.text)


# In[234]:


len(name),len(dist),len(rat),len(price)


# In[235]:


lin,des,fac,review = [],[],[],[]
url = driver.find_elements(By.XPATH,'//a[@class="view-button"]')
for i in url:
    lin.append(i.get_attribute('href'))


# In[236]:


for i in lin:
    driver.get(i)
    time.sleep(2)
    try:
        de = driver.find_element(By.XPATH,'/html/body/div[3]/div/div/div[1]/section/div[6]/div/div[2]/div/div/div[2]')
        des.append(de.text)
        
        fa = driver.find_element(By.XPATH,'/html/body/div[3]/div/div/div[1]/section/div[10]/div/ul')
        fac.append(fa.text.replace('\n',','))
        
        re = driver.find_element(By.XPATH,'/html/body/div[3]/div/div/div[1]/section/div[9]/div[1]/div/div[1]')
        review.append(re.text)
        
    except NoSuchElementException:
        des.append('-')


# In[238]:


len(fac),len(des),len(review)


# In[239]:


lon = pd.DataFrame({'Hostel Name':name[0:30], 'Distance from City Centre':dist[0:30], 'Rating':rat[0:30], 'Price':price[0:30], 'Facilities':fac[0:30], 'Property Description':des[0:30]})


# In[241]:


lon.to_csv('Hostel.csv')


# In[244]:


df = pd.read_csv('Hostel.csv')
df.head(5)


# In[248]:


driver.close()

