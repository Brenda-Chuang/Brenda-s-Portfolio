# import the necessary libraries 
from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
import time
import pandas as pd
import re

# Initialize Playwright
with sync_playwright() as p:
    # Launch the browser
    browser = p.chromium.launch(headless=False)
    
    # Create a new browser page
    page = browser.new_page()
    
    # Navigate to the webpage
    page.goto("https://www.westsideauto.com.au/cars?makes=Toyota")
    
    # Wait for some time to let the page load
    time.sleep(5)
    
    # Scroll until no more new cars are loaded
    previous_height = page.evaluate("document.body.scrollHeight")
    while True:
        page.evaluate("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(5)  # Wait for new cars to load
            
        # Check if new content has been loaded
        new_height = page.evaluate("document.body.scrollHeight")
        if new_height == previous_height:
            break
        previous_height = new_height  # continue the loop
    
    # Get the page content after scrolling
    page_content = page.content()
    
    # Parse the page content using BeautifulSoup
    soup = BeautifulSoup(page_content, 'html.parser')

    # Find all car items 
    cars = soup.find_all('a', class_="styles_vehicleCard__57dQ_")

    # Create an empty list to store car links
    carlinks = []

    # Fetch all car links in each item
    for link in cars:
        carlink = link.attrs['href']
        carlinks.append('https://www.westsideauto.com.au' + carlink)

    # Create an empty list to store vehicle dictionaries
    vehicle_list = []

    # Fetch vehicle features and details in each car link
    for carlink in carlinks:
        # Navigate to the car link
        page.goto(carlink)
        
        # Wait for some time to let the page load
        time.sleep(3)

        # Get the page content after loading
        page_content = page.content()
        
        # Parse the page content using BeautifulSoup
        soup = BeautifulSoup(page_content, 'html.parser')
        
        # Extract make and model
        name = soup.find('h1').text.strip()
        split_name = name.split(" ", 1)
        make = split_name[0]  # The first part is the make
        model = split_name[1] if len(split_name) > 1 else ''  # The second part is the model, or an empty string if not available

        # Extract price
        price_element = soup.find('div', class_="_uid__priceTag__8_0wn")
        price = price_element.text.strip().split('$')[1] if price_element else 'N/A'
        
        # Extract the number of poeple viewed the car
        view_element = soup.find('div', class_= "_uid__recentlyViewed__P_9ND _uid__show__BQYtF")
        view_text = view_element.text.strip()
        # Extract the number using regular expression and return the first group (number)
        view = re.search(r'(\d+)', view_text).group(1) 

        # Fetch vehicle features
        features = {}
        features_element = soup.find_all('div', class_="styles_item__EWJ8_")
        for feature in features_element:
            title = feature.find('span').text.strip()
            content = feature.find('div', class_="styles_value__vbzpT").text.strip()
            features[title] = content
        
        # Scrap data in the vehicle details table
        details = {}
        table_div = soup.find('div', class_="styles_featureTable__Zf2Dc FeatureTable_featureTable__AKGtE styles_flat__J5bju FeatureTable_flat__2VLQv")
        if table_div:
            rows = table_div.find_all('tr')
            for row in rows:
                label = row.find_all('td')[0].text.strip()
                value = row.find_all('td')[1].text.strip()
                details[label] = value
        
        # Combine all data into a dictionary
        vehicle = {
            'Make': make,
            'Model': model,
            'Price': price,
            'View': view,
            **features,
            **details
        }
        
        # Append the vehicle dictionary to the created vehicle_list
        vehicle_list.append(vehicle)
        
    # Close the browser
    browser.close()

# Create a DataFrame for the vehicle list
df = pd.DataFrame(vehicle_list)

# Write the data to a csv file
df.to_csv("Vehicle_Toyota.csv")

'''
Note: The data was scraped by dividing it into several sections based on car models.
      This avoids the time that need to rerun the code to fetch all required data.

'''        
     