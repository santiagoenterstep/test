from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import pandas as pd

# print working directory
# print(os.getcwd())
# base_path = os.getcwd()
# Path to your WebDriver (e.g., ChromeDriver)
# driver_path = 'scrapper/chromedriver'
# driver_path = os.path.join(base_path, driver_path)
# print(driver_path)

# load scraper.xlsx with specific headers
# headers = ['name', 'rut']
# df = pd.read_excel('scrapper/scraper.xlsx', header=None, names=headers)
# print(df)

# # get list of ruts, remove '-' and '.' and spaces
# rut_list = df['rut'].str.replace('-', '').str.replace('.', '').str.replace(' ', '').tolist()
# print(rut_list)

# # URL to scrape
# for rut in rut_list:
#     url = f"https://www.cmfchile.cl/institucional/mercados/entidad.php?mercado=V&rut=96639280&grupo=&tipoentidad=RGAGF&row=AAAwy2ACTAAABzXAAS&vig=VI&control=svs&pestania=47"


url = "https://www.cmfchile.cl/portal/principal/613/w3-propertyvalue-18572.html"
# Set up Selenium WebDriver
driver = webdriver.Chrome()

# Open the webpage
driver.get(url)

# Example: Extract the page title
title = driver.title
print("Page Title:", title)

# Extract specific data here (this is just an example)
# Example: Find an element by ID
element = driver.find_element(By.ID, 'listado_fiscalizados')
#print(element)
elems = driver.find_elements(By.XPATH, "//a[@href]")
for elem in elems:
    text = str(elem.get_attribute("href"))
    if "institucional" in text:
        print(text)

# Close the driver
driver.quit()