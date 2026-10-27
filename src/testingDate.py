from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from datetime import datetime
import os

# Checks the condition of the competition
def checkScores() :
        headings = []
        headingCount = 0
        checks = driver.find_elements(By.CLASS_NAME, "col-2")
        for j in range(len(checks)) :
            if(checks[j].text.__contains__("Not scored")) :
                return 0
                
        # Gathers all "a" css objects into a list
        # Takes those and only takes the href values and adds those into another list
        # Gets the link to the competition recap and sets the url to that
        recaps = driver.find_elements(By.CSS_SELECTOR, "a.arrow-btn")
        for j in range(len(recaps)):
            recaplinks.append(recaps[j].get_attribute("href"))
        driver.get(recaplinks[1])
        time.sleep(3)
        headings = driver.find_elements(By.CSS_SELECTOR, "h2")
        for n in range(len(headings) - 1):
            if(headings[n].text.__contains__("World Class" or "Open Class")) :
                headingCount += 1
            if(headings[n].text.__contains__("All-Age")) :
                headingCount += 1 
                allAge = True
            print(headings[n].text)
        groups = driver.find_elements(By.CLASS_NAME, "sticky-td")
        pageScores = driver.find_elements(By.CLASS_NAME, "data")
        if((headingCount == 1 or 2) and allAge == False and exhibition == False):
            print((len(pageScores) / len(groups)))
        return 1

driver = webdriver.Firefox()

startYear = 2013
scoreslinks = ['https://www.dci.org/scores/final-scores/2013-dci-world-championship-finals/','https://www.dci.org/scores/final-scores/2013-southwest-corps-connection/']
i = len(scoreslinks) - 1

while i >= 0 :
    checkState = 0
    url = scoreslinks[i]
    recaps = []
    recaplinks = []
    groups = []
    
    allAge = False
    exhibition = False

    # Opens up the last link in the array to check from oldest to newest
    # Each iteration checks one closer to beginning
    driver.get(url)  
    time.sleep(2)
    
    # Finds the name and date of the competition for documentation
    date = driver.find_element(By.CLASS_NAME, "score-date-location.justify-center")
    competitions = driver.find_elements(By.CLASS_NAME, "elementor-heading-title.elementor-size-default")
    competition = competitions[2].text
    interText = date.text.splitlines()[0]
    
    # Sets the date in a specific format to be read later
    dt = datetime.strptime(interText, "%B %d, %Y")
    fileDate = dt.strftime("%Y-%d-%m")
    print(fileDate)
    print(competition)
        
    # Opens up the file that represents the current year
    with open("data/competitions/" + str(startYear) + ".csv", "r") as file:
        data = file.read()
        checkCon = 1
        
        
        # Checks the condition of the competition to decide what type of file writing should be done
        # 0 = Not Scored
        # 1 = Normal
        # 2 = Regional or Finals
        checkCon = checkScores()
                
        # Checks if the competition is already in the file
        # If its not, it writes it in and checks the scores
        # If it is, it skips this competition
        # If the competition is not scored, it skips this competition
        if not data.__contains__(fileDate) and (checkCon == 1 or checkCon == 2):
            data = open("data/competitions/" + str(startYear) + ".csv", "w")
            data.write(competition + "\n")
            data.write(fileDate)
            
            # Grabs the name of groups from the "sticky-td" html class
            # Grabs the scores from the "data" html class
            groups = driver.find_elements(By.CLASS_NAME, "sticky-td")
            pageScores = driver.find_elements(By.CLASS_NAME, "data")
            # for j in range(len(pageScores)) :
                #print(pageScores[j].text.replace("\n", ""))
            scrCount = 4
            k = 0
            
            # Starts writing scores to the group's file
            while k < len(groups) :
                if(k == 0):
                    k = 2
                if(groups[k].text == "CORPS") :
                    k += 1
                print(groups[k].text)
                # If it is a normal competition it uses these offsets to gather scores per groups
                if(checkCon == 1):
                    with open("data/groups/" + groups[k].text + ".csv", 'w') as file:
                        file.write(fileDate + "\n")
                        file.write("GE Total: " + pageScores[scrCount].text + "\n")
                        scrCount += 4
                        file.write("Visual Total: " + pageScores[scrCount].text + "\n")
                        scrCount += 4
                        file.write("Music Total: " + pageScores[scrCount].text + "\n")
                        scrCount += 3
                        file.write("Total: " + pageScores[scrCount].text + "\n")
                        scrCount += 5
                
                # If it is a regional or finals competition it uses these offsets to gather scores per groups
                elif(checkCon == 2) :
                    with open("data/groups/" + groups[k].text + ".csv", 'w') as file :
                        file.write(fileDate + "\n")
                        file.write("GE Total: " + pageScores[scrCount].text + "\n")
                        scrCount += 4
                        file.write("Visual Total: " + pageScores[scrCount].text + "\n")
                        scrCount += 4
                        file.write("Music Total: " + pageScores[scrCount].text + "\n")
                        scrCount += 3
                        file.write("Total: " + pageScores[scrCount].text + "\n")
                        scrCount += 5
                k += 1
    print(i)
    i = i - 1
    
    
        
        