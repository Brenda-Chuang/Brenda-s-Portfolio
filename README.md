# Project 1: Pre-Owned Vehicles Analysis Dashboard

## Dashboard Overview
https://github.com/Brenda-Chuang/Brenda-s-Portfolio/assets/171400447/ea17b7b6-2215-4f8d-89a4-5b9dd8a9dfb4

## Problem Statement

This project aims to provide insights into various aspects of pre-owned vehicle stocking, including the top makes and models in stock, common vehicle features, customer preferences, pricing dynamics, and depreciation rates. <br/>

Specifically, the analysis aims to address the following questions:<br/>

- Vehicle Stocking analysis:
1. What are the Top 8 makes of the in-stock vehicle?
2. What are the most common features of the vehicles in stock (Fuel type, transmission, drivetrain, Colour and body type)?
- Vehicle Views analysis:
1. Which make and model combinations are most popular based on views, and do they align with the current inventory levels?
2. What are the most viewed odometer ranges for the top makes and models?
-  Vehicle Pricing Analysis:
1. What is the relationship between vehicle price and the number of views?
2. What is the average price distribution, categorised by odometer readings, for the top makes and models of vehicles?
- Customer Preferences Analysis:
1. What is the colour and body type that is most viewed?
2. Regarding the top 3 viewed makes and models, what are the most viewed body types and the relative most common vehicle features?

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
Step 8: Write the cleaned vehicle data into a CSV file <br/>

Detailed steps and codes are documented in [Pre-Owned Vehicles cleaned.ipynb](https://github.com/Brenda-Chuang/Brenda-s-Portfolio/blob/main/Pre-Owned%20Vehicles%20Project/Vehicle%20scrapping%20code/Pre-Owned%20Vehicles_cleaned.ipynb).<br/>

## Data Analysis and Visualisation

- Vehicle Stocking analysis:
1. What are the Top 8 makes of the in-stock vehicle?<br/>
[Visualisation: Top 8 Makes in Stock (bar chart)]<br/>
Of 1,584 vehicles in stock, the top 8 makes are Toyota (752), Ford (169), Mitsubishi (89), Mercedez Benz (64), Isuzu (54), Hyundai (45), Peugeot (39), and Suzuki (38).
2. What are the most common features of the vehicles in stock (Fuel type, transmission, drivetrain, Colour and body type)?<br/>
[Visualisation: Stock Fuel Type/Transmission/Drivetrain (pie chart) & Most In-Stock Colour and Body Type (card)]<br/>
Fuel Type: Diesel (63.3%); Transmission: Automatic (81.8%); Drivetrain: 4WD (50.6%); Colour: White; Body Type: Wagon.

- Vehicle Views analysis:
1. Which make and model combinations are most popular based on views, and do they align with the current inventory levels?<br/>
[Visualisation: Top Makes and Models by Views (Table)]<br/>
Toyota Hilux, with 68,587 views and 276 units in stock, is the most viewed and stocked make and model, second to which is the Toyota Landcruiser, with 58,854 views and 124 units in stock. Ford Ranger is the third most popular make and model, with 39,576 views and 134 units in stock.
The top-viewed makes and models are stocked with higher volume, indicating that the dealer is likely meeting customer interest.<br/>

2. What are the most viewed odometer ranges for the top makes and models?<br/>
[Visualisation: Heat Map for Price and Views by Odometer Bucket (Matrix)]<br/>
For the Toyota Hilux, the highest view (25,663) is located at an odometer between 101 and 200k, followed by an odometer of 1-10k, with 22,383 views. In addition, the Toyota Landcruiser’s odometer of 101-200 has the most views (22,010 views), while most views of the Toyota Landcruiser 70 Series are under 10k odometer (28,905 views). Ford Ranger’s odometer under 10k and 101-200k are the most viewed buckets, with 15,499 and 11,646 views, respectively.<br/>

- Vehicle Pricing Analysis:
1.	What is the relationship between vehicle price and the number of views?<br/>
[Visualisation: Price and Views Scatter Plot]<br/>
The overall vehicle price and number of views are positively correlated, indicating that higher-priced vehicles tend to receive more views. However, among the top 8 in-stock vehicles, Peugeot's price and number of views show a negative correlation, meaning that higher-priced Peugeot vehicles tend to receive fewer views.
2.	What is the average price distribution, categorised by odometer readings, for the top makes and models of vehicles?<br/>
[Visualisation: Heat Map for Price and Views by Odometer Buckets] <br/>
The analysis highlights that under 10k odometer readings, Toyota ($81.7k) and Mercedes-Benz ($81.9k) have the highest average prices. However, Toyota appears to exhibit a comparatively lower depreciation rate across odometer buckets compared to Mercedes-Benz, indicating potentially better long-term value retention for Toyota vehicles. However, the trends observed at the made level may oversimplify the situation, as different models within the same make can have distinct pricing characteristics. Further analysis and a larger sample size are needed at the model level to provide more accurate insights.

- Customer Preferences Analysis: 
1.	What is the colour and body type that is most viewed?<br/>
[Visualisation: Most Viewed Colour and Body Type (card)] <br/>
White is the most viewed colour, and wagon is the most viewed body type across all makes and models, which aligns with the stocking situation.<br/>
2.	Regarding the top 3 viewed makes and models, what are the most viewed body types and the relative most common vehicle features? <br/>
[Visualisation: Top Makes and Models by Views (Table) & tooltip] <br/>
(1)	Toyota Hilux (Double Cab Chassis): 4 doors; 5 seats, colour: white; fuel type: diesel; transmission: automatic; drivetrain: 4WD; 4 engine cylinders (2.8L). <br/>
(2)	Toyota Landcruiser (Wagon): 4 doors; 7 seats, colour: white; fuel type: diesel; transmission: automatic; drivetrain: 4WD; 4 engine cylinders (4.5L). <br/>
(3)	Ford Ranger (Double Cab Pickup): 4 doors; 5 seats, colour: white; fuel type: diesel; transmission: automatic; drivetrain: 4WD; 5 engine cylinders (3.2L). <br/>

## Conclusion:
-	Toyota dominates both in terms of stock volume and views, with the Hilux and Landcruiser being the most popular models.
-	The majority of vehicles in stock have diesel engines, automatic transmission, and 4WD drivetrains.
-	The Toyota Hilux, Toyota Landcruiser, and Ford Ranger are the top-viewed makes and models, and they correspond with the higher volume of stock.
-	The analysis of odometer ranges for top-viewed makes and models shows a varying preference, with either the odometer reading between 100 to 200k or under 10k having the highest views.
-	There is a positive correlation between vehicle price and the number of views, except for outliers such as Peugeot, which show a negative correlation.
-	Different makes exhibit different depreciation rates across odometer buckets, with Toyota and Mercedes-Benz showing higher initial average prices, and the former having a better long-term retention value.
-	White wagons are the most stocked and viewed across all makes and models, indicating a strong preference among customers for this combination.
-	For the top three viewed makes and models, the commonalities in features 4 doors, diesel engine, automatic transmission, and 4WD drivetrain, suggesting a preference among customers for these specifications.
