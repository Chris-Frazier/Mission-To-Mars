
# coding: utf-8

# In[3]:


# Import BeautifulSoup
from bs4 import BeautifulSoup
import requests
import pandas as pd


# In[11]:


#url of page to be scraped
url = 'https://mars.nasa.gov/news/'


# In[12]:


# Retrieve page with the requests module
response = requests.get(url)


# In[14]:


# Create BeautifulSoup object; parse with 'html.parser'
soup = BeautifulSoup(response.text, 'html.parser')


# In[15]:


# Examine the results, then determine element that contains sought info
print(soup.prettify())


# In[17]:


news_title = soup.title.text


# In[22]:


news_p = soup.body.p.text


# In[23]:


news_p


# In[84]:


# Import Splinter and set the chromedriver path
from splinter import Browser
executable_path = {'executable_path': 'chromedriver.exe'}
browser = Browser('chrome', **executable_path, headless=False)


# In[85]:


# Visit the following URL
url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars#submit"
browser.visit(url)


# In[90]:


xpath = '//a[@id="full_image"]'


# In[91]:


result = browser.find_by_xpath(xpath)


# In[82]:


results = browser.find_by_xpath(xpath)
img = results[0]
img.click()


# In[92]:


result


# In[93]:


result.click()


# In[107]:


html = browser.html
soup = BeautifulSoup(html, 'html.parser')
img_url = soup.find('img', class_="fancybox-image")["src"]
img_url


# In[46]:


url2 = 'https://twitter.com/marswxreport?lang=en'


# In[47]:


response2 = requests.get(url2)


# In[48]:


soup2 = BeautifulSoup(response2.text, 'html.parser')


# In[56]:


#print(soup2.prettify())


# In[50]:


soup2.body.p


# In[4]:


url3 = 'https://space-facts.com/mars/'


# In[5]:


tables = pd.read_html(url3)
tables


# In[6]:


#!pip install lxml


# In[51]:


from splinter import Browser
executable_path = {'executable_path': 'chromedriver.exe'}
browser = Browser('chrome', **executable_path, headless=False)


# In[52]:


url4 = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
browser.visit(url4)


# In[54]:


links = browser.find_by_xpath('//h3')
links


# In[55]:


links[0].click()


# In[44]:


html = browser.html
soup = BeautifulSoup(html, 'html.parser')


# In[57]:


img1_url = soup.find('img', class_="wide-image")["src"]
img1_url


# In[59]:


img1_title = soup.find('h2', class_="title").text
img1_title


# In[63]:


browser.visit(url4)
links = browser.find_by_xpath('//h3')
links


# In[64]:


links[1].click()


# In[66]:


html = browser.html
soup = BeautifulSoup(html, 'html.parser')
img2_url = soup.find('img', class_="wide-image")["src"]
img2_url
img2_title = soup.find('h2', class_="title").text
img2_title


# In[67]:


browser.visit(url4)
links = browser.find_by_xpath('//h3')
links


# In[68]:


links[2].click()
html = browser.html
soup = BeautifulSoup(html, 'html.parser')
img3_url = soup.find('img', class_="wide-image")["src"]
img3_url
img3_title = soup.find('h2', class_="title").text
img3_title


# In[72]:


browser.visit(url4)
links = browser.find_by_xpath('//h3')
links


# In[73]:


links[3].click()
html = browser.html
soup = BeautifulSoup(html, 'html.parser')
img4_url = soup.find('img', class_="wide-image")["src"]
img4_url
img4_title = soup.find('h2', class_="title").text
img4_title


# In[77]:


dict1 = {img1_title :img1_url}
dict2 = {img2_title :img2_url}
dict3 = {img3_title :img3_url}
dict4 = {img4_title :img4_url}


# In[78]:


hemisphere_image_urls = [dict1,dict2,dict3,dict4]


# In[79]:


hemisphere_image_urls


# In[ ]:


get_ipython().system('jupyter nbconvert --to script config_template.ipynb')


def scrape():
    mars_data = {}
    # Import BeautifulSoup
    from bs4 import BeautifulSoup
    import requests
    import pandas as pd

    url = 'https://mars.nasa.gov/news/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    news_title = soup.title.text
    news_p = soup.body.p.text

    '''
    try:
        from splinter import Browser
        executable_path = {'executable_path': 'chromedriver.exe'}
        browser = Browser('chrome', **executable_path, headless=False)

        url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars#submit"
        browser.visit(url)

        xpath = '//a[@id="full_image"]'
        result = browser.find_by_xpath(xpath)
        result.click()
        html = browser.html
        soup = BeautifulSoup(html, 'html.parser')
        img_url = soup.find('img', class_="fancybox-image")["src"]
     except:   
        img_url = 'image not found'
        
    #url2 = 'https://twitter.com/marswxreport?lang=en'
    #response2 = requests.get(url2)
    #soup2 = BeautifulSoup(response2.text, 'html.parser')
      
    '''
    
    url3 = 'https://space-facts.com/mars/'
    tables = pd.read_html(url3)

    from splinter import Browser
    executable_path = {'executable_path': 'chromedriver.exe'}
    browser2 = Browser('chrome', **executable_path, headless=False)
    url4 = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser2.visit(url4)
    links = browser2.find_by_xpath('//h3')
    links[0].click()
    html = browser2.html
    soup = BeautifulSoup(html, 'html.parser')
    img1_url = soup.find('img', class_="wide-image")["src"]
    img1_title = soup.find('h2', class_="title").text
    browser2.visit(url4)
    links = browser2.find_by_xpath('//h3')
    links[1].click()
    html = browser2.html
    soup = BeautifulSoup(html, 'html.parser')
    img2_url = soup.find('img', class_="wide-image")["src"]
    img2_title = soup.find('h2', class_="title").text
    browser2.visit(url4)
    links = browser2.find_by_xpath('//h3')
    links[2].click()
    html = browser2.html
    soup = BeautifulSoup(html, 'html.parser')
    img3_url = soup.find('img', class_="wide-image")["src"]
    img3_title = soup.find('h2', class_="title").text
    browser2.visit(url4)
    links = browser2.find_by_xpath('//h3')
    links[3].click()
    html = browser2.html
    soup = BeautifulSoup(html, 'html.parser')
    img4_url = soup.find('img', class_="wide-image")["src"]
    img4_title = soup.find('h2', class_="title").text
    dict1 = {img1_title :img1_url}
    dict2 = {img2_title :img2_url}
    dict3 = {img3_title :img3_url}
    dict4 = {img4_title :img4_url}
    hemisphere_image_urls = [dict1,dict2,dict3,dict4]

    mars_data['News_title'] = news_title
    mars_data['News'] = news_p
    mars_data['Featured_image'] = img_url
    mars_data['Mars_facts'] = tables
    mars_data['Hemispheres'] = hemisphere_image_urls

    return mars_data