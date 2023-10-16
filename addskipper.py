#some mind blowing fact-----------------------------------------------------------------------------------------------------------------------------------------------------------
#Turns out adding a ‘period’ at the end of the domain name in the URL bar does the magic. For example, if a video arrives with an
# URL “www.youtube.com/watch”, simply adding a ‘period’ after the domain name such as “www.youtube.com./watch” does the magic.
# According to a supporting report explaining how to block YouTube ads and how this trick works, it works simply by breaking a landing page in a way that videos do load but end up failing to load quite a lot of aspects such as advertisements in this case. This also circumvents the ads that run when you tap on any video to watch or while binge-watching any video. Note that this doesn’t work on YouTube apps since you’ll need to tweak the
# URL to get it working, however, it does work flawlessly on desktop and on mobile browsers with the desktop mode enabled.
# If you are still clueless on how it actually works, here, adding a period overthrows the ability to match the hostname. This, in turn, breaks the page as to only loading the content it offers and not the ads and a few other parts of the website. It also
# blocks cookies and paywalls that news sites and other websites might institute to pay for reading a blog or article.
#==================================================================================================================================================================================
# this program will skip the add from youtube
#pre-requisite python install
#modules needed-selenium and pyderman
#selenium ?
#One of the most widely used test automation tools in Python is Selenium. 
#It's open-source and free to use. Selenium with Python is used to carry out automated test cases for browsers or web applications
# pyderman ?
#This is a fast, simple, dependency-free package that can automatically find & download any version of the Google 
#Chrome (chromeDriver), Firefox (geckoDriver), PhantomJS, Opera (operaDriver), and Edge (edgeDriver) web drivers
from selenium import webdriver 
from selenium.webdriver.common.by import By
import selenium.webdriver.support.ui as ui
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import pyderman
import time
driverpath = pyderman.install(browser=pyderman.chrome)
driver =webdriver.Chrome(driverpath)

driver.maximize_window()
weburl="https://www.youtube.com/"
driver.get(weburl)

wait=ui.WebDriverWait(driver,300)

while True:
    try:
        if EC.presence_of_all_elements_located((By.XPATH,".//div/div/div/div/div/span/button/div[contains(text(),'Skip Ad')]")):
           button = driver.find_element("xpath",".//div/div/div/div/div/span/button/div[contains(text(),'Skip Ad')]")
           # in the upper line it was not uses find_element_by_xpath becasuse it was uppdated in the latest version of selenium istead we use this the uppdated format find_element("xpath", '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
           driver.execute_script("arguments[0].click();",button)
           print("Ad skipped")
           time.sleep(2)
        else:
             continue
    
    except NoSuchElementException:
     print("waiting ...")
    time.sleep(2)
         

    