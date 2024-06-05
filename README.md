# Project 1: Pre-Owned Vehicles Analysis Dashboard

## Problem Statement


## Data Collection 

The data for this project was scrapped from Westside Auto Wholesale.<br/>

Web Scraping Tools and Method:
- Python libraries: Playwright and BeautifulSoup. <br/>
- The data was scraped by dividing it into several sections based on car models.
  This avoids the occasion that requires rerunning the code to fetch all required data.

The shop webpage contains all vehicle boxes in which the vehicle data are displayed. The scrapping process involves finding all links associated with the vehicle boxes and accessing the individual vehicle pages to scrap the required data. The required vehicle data for this project are categorised into three sections: 
- Vehicle Main Details and Statistics: Make, Model, Price, and View.
- Vehicle Features: Model Year, Odometer, Fuel Type, Drivetrain, Transmission, Seats, Engine.
- Additional Vehicle Details: Series, Transmission, Body, Colour, VIN, Badge, Engine, Drive Type, Stock number, and Rego.<br />

The web scraping code and detailed steps are documented in [Pre-Owned Vehicles scrapping.py](https://github.com/Brenda-Chuang/Brenda-s-Portfolio/blob/main/Pre-Owned%20Vehicles%20Project/Vehicle%20scrapping%20code/Pre-Owned%20Vehicles%20scrapping.py).<br/>

## Data Cleaning

The data cleaning was performed using Python and the Pandas library, including the following steps:<br/>

Step 1: Concat all vehicle files into one single file <br/>
Step 2: Observe the data frame <br/>
Step 3: Drop unnecessary columns <br/>
Step 4: Remove unnecessary unit content in data <br/>
Step 5: Split separate information stored in the same column <br/>
Step 6: Replace missing values <br/>
Step 7: Change data type <br/>
Step 7: Write the cleaned vehicle data into a CSV file <br/>

Detailed steps and codes are documented in [Pre-Owned Vehicles cleaned.ipynb](https://github.com/Brenda-Chuang/Brenda-s-Portfolio/blob/main/Pre-Owned%20Vehicles%20Project/Vehicle%20scrapping%20code/Pre-Owned%20Vehicles_cleaned.ipynb).<br/>



## Features

- **Top 8 Vehicle Makes in Stock**: Display the top 8 vehicle makes with the most stock volume.
- **Inventory and Views by Make and Model**: View the volume of cars in stock and the number of views categorized by make and model.
- **Heat Map for Price and Views by Odometer**: Interactive heat map displaying average prices and total views by make/model and odometer buckets.
- **Average Price by Model Year**: View average prices change based on the model year of the vehicles.
- **Most In-Stock and Most Viewed Colours and Body Types**: Insights into the most common and most popular car colours and body types.
- **Fuel Type and Drivetrain Distribution**: Showcase the distribution of cars based on fuel type and drivetrain.
