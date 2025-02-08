from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import pandas as pd
import time
import random

#Set up Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--incognito")
chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.199 Safari/537.36")

#Initialize WebDriver
driver = webdriver.Chrome(options=chrome_options)

def scrape_bigbasket(category_url):
    driver.get(category_url)
    time.sleep(random.uniform(5, 10))

    products = []
    l_height = 0

    while True:
        product_names = driver.find_elements(By.CSS_SELECTOR, "h3.block.m-0.line-clamp-2.font-regular.text-base.leading-sm.text-darkOnyx-800.pt-0\\.5.h-full")
        prices        = driver.find_elements(By.CSS_SELECTOR, ".Label-sc-15v1nk5-0.Pricing___StyledLabel-sc-pldi2d-1.gJxZPQ.AypOi")
        discounts     = driver.find_elements(By.CSS_SELECTOR, "span.font-semibold.lg\\:text-xs.xl\\:text-sm.leading-xxl.xl\\:leading-md")

        for i in range(len(product_names)):
            try:
                name = product_names[i].text
            except:
                name = None
            try:
                price = prices[i].text
            except:
                price = None
            try:
                discount = discounts[i].text.strip()
            except:
                discount = None

            products.append({
                "Product_Name": name,
                "Price": price,
                "Discount": discount,
                "Category": category_url.split("/")[-1]
            })

        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(random.uniform(5, 10))

        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == l_height:
            break
        l_height = new_height

    return products

#URLs for categories
categories = {
    "Fruits"        : "https://www.bigbasket.com/ps/?q=fruits&nc=as",
    "Vegetables"    : "https://www.bigbasket.com/ps/?q=vegetable&nc=as",
    "Dairy"         : "https://www.bigbasket.com/ps/?q=dairy&nc=as",
    "Beverages"     : "https://www.bigbasket.com/ps/?q=beverages&nc=as",
    "Snacks"        : "https://www.bigbasket.com/ps/?q=snacks&nc=as",
    "Grocery"       : "https://www.bigbasket.com/ps/?q=grocery&nc=as",
    "Household"     : "https://www.bigbasket.com/ps/?q=household&nc=as",
    "Personal Care" : "https://www.bigbasket.com/ps/?q=personal+care&nc=as",
    "Meat"          : "https://www.bigbasket.com/ps/?q=meat&nc=as",
    "Fish"          : "https://www.bigbasket.com/ps/?q=fish&nc=as",
    "Eggs"          : "https://www.bigbasket.com/ps/?q=eggs&nc=as",
    "Bakery"        : "https://www.bigbasket.com/ps/?q=bakery&nc=as",
    "Branded Foods" : "https://www.bigbasket.com/ps/?q=branded+foods&nc=as",
    "Baby Care"     : "https://www.bigbasket.com/ps/?q=baby+care&nc=as"
}

all_data = []

#Scrape each category
for category, url in categories.items():
    print(f"Scraping category: {category}")
    data = scrape_bigbasket(url)
    all_data.extend(data)

#Save to CSV file
df = pd.DataFrame(all_data)
df.to_csv("bigbasket.csv", index=False)

driver.quit()
print("Scraping completed. Data saved to 'bigbasket.csv'")



#--------------------Data_load_and_analysis--------------------------

#Import important libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings("ignore")

df = pd.read_csv("bigbasket.csv")

#Extract numeric value from Price and Discount column
df['Price'] = df['Price'].str.extract(r'(\d+)')
df['Price'] = pd.to_numeric(df['Price'])
df['Discount'] = df['Discount'].str.extract(r'(\d+)')
df['Discount'] = pd.to_numeric(df['Discount'])

#Replace null values in price with mean and discount with zero
df['Price'] = df['Price'].fillna(df['Price'].mean())
df['Discount'] = df['Discount'].fillna(0)

df['Category'] = df["Category"].apply(lambda x: x.split("=")[1].split("&")[0] if "=" in x and "&" in x else None)
df['Category'] = df['Category'].str.replace('+', ' ')

#save file to csv
df.to_csv('bigbasket_cln.csv', index=False)

#save file to MySQL database 
import pymysql
import pandas as pd
connection = pymysql.connect(host='localhost', user='root', password="GKB@mysql_ds07", database='code_it') 
cursor = connection.cursor()

df = pd.read_csv('bigbasket_cln.csv')
#insert into MySQL table
for _, row in df.iterrows():
    cursor.execute("""INSERT INTO bigbasket_cln (Product_Name, Price, Discount, Category)
         VALUES (%s, %s, %s, %s)
    """, (row["Product_Name"], row["Price"], row["Discount"], row["Category"]))

connection.commit()
print("Data inserted successfully")

querry = "SELECT * FROM bigbasket_cln"
cursor.execute(querry)
rows = cursor.fetchall()
for row in rows:
    print(row)

cursor.close()
connection.close()