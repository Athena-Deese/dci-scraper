# Athena's DCI Score Scraper
This program is meant to go through the DCI scores website and track down each individual competitions 
scores and iterates over your list.
This program is ***NOT DONE***, do not use it expecting it to work right now.

## How to reset
To run this for yourself, you need to delete every CSV file from data/groups as well as deleting **THE DATA** from every file in the data/competitions folder.
**DO NOT** delete the CSV files in data/competitions, only delete the **data**

## How to use
When you run this file, it will ask for a start and end year. The start date should be later than the end date because this program
works backwards. It will then open a botted Firefox tab and start iterating through the competition links in the given range.
After this program finishes running, the scores as well as the date for each score should be in each individual group's data/groups CSV file, 
as well as every competition date and name in the respective data/competitions CSV file.

## Program output
This program will output CSV files relating to every **WORLD** and **OPEN** class groups that performed in each of these competitions.
