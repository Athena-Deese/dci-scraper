from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from datetime import datetime
import os

# Checks the condition of the competition

driver = webdriver.Firefox()

startYear = 2013
scoreslinks = ['https://www.dci.org/scores/final-scores/2013-southwest-corps-connection/', 'https://www.dci.org/scores/final-scores/2013-dci-world-championship-finals/']
i = len(scoreslinks) - 1
while i >= 0 :
    url = scoreslinks[i]
    
    # Opens up the last link in the array to check from oldest to newest
    # Each iteration checks one closer to beginning
    driver.get(url)  
    time.sleep(2)
    
    # Finds the date and name of the competition from the main page
    date = driver.find_element(By.CLASS_NAME, "score-date-location.justify-center")
    competitions = driver.find_elements(By.CLASS_NAME, "elementor-heading-title.elementor-size-default")
    competition = competitions[2].text
    interText = date.text.splitlines()[0]
    
    # Sets the date in a specific format to be read later
    dt = datetime.strptime(interText, "%B %d, %Y")
    fileDate = dt.strftime("%Y-%d-%m")
    print(fileDate)
    print(competition)
    
    # Opens up the data folder relating to the year of the competition
    with open("data/competitions/" + str(startYear) + ".csv", "r") as file:
        data = file.read()
        
        # Checks if either the competition has already been checked, or if it is unscored
        # Then skips the competition is either is true
        if(data.__contains__(fileDate)) :
            print("Skipped")
            i -= 1
            continue
        checks = driver.find_elements(By.CLASS_NAME, "col-2")
        if(checks[6].text.__contains__("Not scored")):
            print("Skipped")
            i -= 1
            continue
        print("Was not skipped")
    
    

    i = i - 1
    
    
        
        