# importing selenium, Beautiful soup and Pandas
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import requests
from bs4 import BeautifulSoup
import pandas as pd

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(id="ResultsContainer")
job_elements = results.findAll('div', class_="card-content")  #  here we're finding elements by HTML class name
jobs=[]
final = pd.DataFrame()
for job_element in job_elements:

    title_element = job_element.find("h2", class_="title")
    company_element = job_element.find("h3", class_="company")
    location_element = job_element.find("p", class_="location")

    a = 'Title'
    b = 'Company'
    c = 'Location'
    # job = {
    #     "Title": title_element.text.strip(),
    #     "Company": company_element.text.strip(),
    #     "Location": location_element.text.strip()
    # }
    job = {a: title_element.text.strip(), b: company_element.text.strip(), c: location_element.text.strip()}
    print(job, 'loop')
    df = pd.DataFrame([job])
    print(df, "****************************************")
    # df.to_csv("jobs.csv", index=[], encoding='utf-8')
    final = final._append(df)
final.to_csv("jobs.csv", index=[0], encoding='utf-8')
print(final, "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")



