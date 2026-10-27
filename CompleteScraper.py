from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from datetime import datetime

# Initializes the program, gathers start and end date and defines variables
driver = webdriver.Firefox()
print("What is your start year?: ")
startYear = int(input())
print("What is your end year?: ")
endYear = int(input())
loopCondition = 1
pageNo = 1
scoreslinks = []

# Starts the crawler, starts at startYear page
url = "https://www.dci.org/scores/?location=&season=" + str(startYear) + "&pageno=1"
driver.get(url)
time.sleep(3)

# Overarching loop that cycles through each year
while startYear >= endYear :
    scoreslinks = []
    pageNo = 1
    loopCondition = 1

    # Goes through the entirety of each year's page count, grabs every competition link, defined by the page total at the bottom of the page
    while loopCondition != 2 :
        url = "https://www.dci.org/scores/?location=&season=" + str(startYear) + "&pageno=" + str(pageNo)
        driver.get(url)
        time.sleep(2)

        scores = (driver.find_elements(By.CSS_SELECTOR, "a.arrow-btn"))
        endPage = driver.find_element(By.CLASS_NAME, "total-page")
        for i in range(len(scores)) :
            scoreslinks.append(scores[i].get_attribute("href"))
        if(pageNo == int(endPage.text)) :
            loopCondition = 2
        pageNo = pageNo + 1

    i = len(scoreslinks) - 1

    # Goes through and checks whether each score page has already been put into the system based on the web date
    
    startYear = startYear - 1
driver.quit


