## Krasnoyarsk House Price Prediction project
The goal of this project is to develop a model that accurately predicts house prices in Krasnoyarsk. To achieve this, we employed various data science techniques, including web scraping, data cleaning, exploratory data analysis (EDA), and model building.

### Project Overview
* A tool has been created that estimates housing prices in Krasnoyarsk (MAE ~ 6K euros) to help buyers, sellers, developers and investors who wish to invest in the housing market of the city of Krasnoyarsk to obtain valuable information.
* Find the best deals by number of rooms, price, building status.
* Collected over 2400 apartment listings from a real estate website using Python and Selenium.
* Optimized RandomForestRegressor, ExtraTreesRegressor and GradientBoostingRegressor using GridsearchCV to achieve the best model.
* Created client API using flask

### Code and Resources Used:
Python Version: 3.9.13 <br/>
Packages: pandas, numpy, matplotlib, selenium, seaborn, plotly, sklearn, flask, pickle, tqdm

### Web Scraping
We used Python and the Selenium library to scrape over 2400 flat offers from a real estate market website(link provided below). The web scraper was customized for this project and fetched the following information for each flat offer: room_number, region, area, price, price_sq_m, floor, and layout.

### Data Cleaning
After scraping the data, we performed necessary cleaning steps to ensure its usability for our model.
The cleaning steps include adding a prefix to the original column names, removing duplicate rows, deleting rows with missing or irrelevant values, translating and renaming values in certain columns for clarity, extracting relevant information from columns like city area and premises area, splitting the floor information into separate columns for floor number and total floors, extracting layout and construction status information, cleaning and converting the price column to euros, and finally saving the cleaned data to a new CSV file. <br/>
By following these data cleaning steps, the script ensures that the dataset is free from duplicates, missing values, and irrelevant information, making it more suitable for subsequent analysis tasks. The resulting cleaned dataset includes important features such as flat type, city area, premises area, floor number, total floors, layout, construction status, and price. 

### Exploratory Data Analysis (EDA)
EDA is a crucial step in understanding the data and extracting meaningful insights. Here are some highlights from our EDA:<br/>
* There is a strong linear relationship between price and premises area, indicating that larger apartments tend to have higher prices.
* The number of rooms has a significant impact on housing cost, with one and two-room apartments being the most common and affordable options.
* The city area plays a crucial role in the housing market, with certain districts having a higher concentration of apartments.
* The layout type significantly affects apartment prices, with certain types being more expensive than others.
* The construction status of buildings varies, and apartments under construction are popular, particularly two-room apartments.
* The EDA also identified profitable and popular two-room apartments located in specific regions of Krasnoyarsk.
[alt text](https://github.com/vvalmispild/Krasnoyarsk_Real_Estate_project/blob/main/img/Scatter_plot.png)

### Machine Learning Prediction:
To predict house prices accurately, we experimented with various machine learning models. The following models were trained and evaluated: <br/>
* Linear Regression 
* Lasso Regression 
* Ridge Regression 
* Decision Tree 
* Random Forest 
* Extra Trees 
* K-Nearest Neighbors 
* Gradient Boosting

#### Model performance
The performance of these models was evaluated using metrics such as Mean Absolute Error (MAE), Root Mean Squared Error (RMSE), and R2-score. After careful evaluation, we selected the top three performing models for further consideration: Random Forest, Extra Trees, and Gradient Boosting. Among these, the Gradient Boosting Regressor exhibited the best performance on the test dataset based on the RMSE and R2_score metrics. <br/>
Here are the evaluation results for the selected models: <br/>
<sup>
Model	| MAE	| RMSE	| R2_score |
|----------|:---------:|--------:|---------:|
RandomForestRegressor |	6241.36 |	10772.98 |	0.837661 |
ExtraTreesRegressor |	6068.86 |	10573.05 |	0.843631 |
GradientBoostingRegressor |	6248.75 |	10191.07 |	0.854725 |
</sup>

### Productionization
The final model (GradientBoostingRegressor) was incorporated into a Flask API.
We built a Flask API endpoint to serve our model predictions. The API is hosted on a local web server and accepts requests with a list of values representing a flat listing. It returns an estimated price for the real estate based on the input parameters.<br/>
To use the API, make a POST request to the following endpoint:<br/>
http://localhost:5000/predict
The request payload should include the necessary parameters for a flat listing, and the API will respond with the estimated price.

### Conclusion
The Krasnoyarsk House Price Prediction project offers a valuable tool for estimating house prices in the Krasnoyarsk city housing market. By leveraging web scraping, data cleaning, exploratory data analysis, and advanced machine learning models, we have developed a reliable solution to provide insights for buyers, sellers, developers, and investors. The Flask API allows for easy integration into various applications, enabling users to obtain estimated prices for real estate listings in Krasnoyarsk.


### References:
<sup>
1) https://arevera.ru/apartments/  <br/>
2) https://medium.com/towards-data-science/how-to-easily-deploy-machine-learning-models-using-flask-b95af8fe34d4 
</sup>

<!---![alt text](https://github.com/vvalmispild/Krasnoyarsk_Real_Estate_project/blob/main/img/Scatter_plot.png)
![alt text](https://github.com/vvalmispild/Krasnoyarsk_Real_Estate_project/blob/main/img/Layout.png)-->
