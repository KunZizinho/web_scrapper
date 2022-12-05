# web_scrapper

# Importing libraries
    - Selenium -->  import webdriver from selenium for browser 
    automatization
        from selenium import webdriver
        from selenium.webdriver.chrome.service import Service
        from webdriver_manager.chrome import ChromeDriverManager

    - BeutifulSoup --> for parsing HTML and XML documents
            from bs4 import BeautifulSoup
    - Pandas --> for data analysis and manipulation
            import pandas as pd
    - Requests library --> for http requests
            import requests


# Step 1
 Fisrt we're gonna inspect website we are scrapping.
 for this excercise we are using https://realpython.github.io/fake-jobs/ .
 we are gonna scrape HTML content fro the website. 
 Look for a parrent ellement that contains content that we want to parse.

 # Step 2
 Parsing HTML content with BeutifulSoup.
 We parsed <div> with id of "ResultContainer" and declared as result
 then wo declared empty list jobs and with pandas final dataframe.

 # Step 3
  
  Now we are gonna start a for loop that is gonna go thru our scraped data and look for elements that we decided to look for.
  In  this case we are looking for title, company and location .
  then from our scalar values we passed to dictionary and declared job.
  And we keep appending our data frame till we get to last iteration where we append our df data frame to our final data frame out side of the loof.

  # Step 4

  and we use to_csv method to create csv file with our scraped and organized information. 


