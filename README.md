# BlueBikes-Analysis-and-Prediction- 2022 and 2023 Q1

"""
**PART 1**

Blue Bikes is a public bicycle sharing system in the Boston area. It serves as a convenient and eco-friendly transportation alternative for thousands of residents and tourists.

With the increase in usage over the years, there is a growing need to understand user behavior and bike usage patterns. This understanding is vital for effective resource allocation, scheduling maintenance, and overall service improvement.

The dataset used for this project is sourced from Blue Bikes' official website. Blue Bikes maintains a comprehensive collection of system data, which is openly available to the public for analysis and insights.

## REAL WORLD PROBLEM AND ROLE OF BIG DATA
Role of Big Data: 
Big data aids in comprehending user behaviors and usage patterns, enabling effective demand forecasting and resource planning. It powers predictive modeling to anticipate demand and facilitates service improvement strategies by identifying high-traffic stations and popular ride times.

## 01
Recommendations

## EXPLORATORY DATA ANALYSIS
01

Dataset Entries:
The dataset comprises 1,048,575 rows and 14 columns

Data Quality:
Missing Data
      The "postal code" column has a significant number of missing values, specifically 110,793 entries. 
      However, the rest of the dataset columns do not have any missing values.
Duplications
       Dataset does not contain any duplicate rows, ensuring the uniqueness of each observation.
Outliers and Suspicious Data
       The "tripduration" column exhibits numerous outliers, indicating the presence of 
       unusually long or short trips compared to the majority of rides.                


Average trip duration for subscribers and customers

Peak hours of ride frequencies for Blue Bikes

Usage of blue bikes on weekdays and weekends

Most popular stations

## MODEL DEVELOPMENT
You can enter a subtitle here if you need it

Models under examination: 
Decision Tree, Random Forest, Gradient Boosting, and Logistic Regression.​​

The ROC curve analysis indicates that the model's predictions were essentially random.

The ROC curve and AUC values suggest a moderate level of discrimination ability, with room for performance enhancement.

Processes undertaken include data preprocessing, model training and evaluation, and hyperparameter tuning.

Performance insights were gathered from measures such as accuracy, precision, recall, F1-score, and the confusion matrix.


The ROC curve depicts the model's capacity to differentiate between rush hour and non-rush hour bike rides.

AUC value of 0.59 indicates moderate discriminatory power.


The AUC value is 0.602, marginally above the line of randomness.


AUC score between 0.58 and 0.59 indicates that the models have some ability to discriminate between rush hour and non-rush hour bike trips, but there is room for improvement. 

## INTERPRETATIONS 
03

Predicting peak hour bike trips based on provided attributes is challenging.
Models demonstrated modest predictive performance, with accuracies ranging from 56.8%       to 59.09%.
Additional data or advanced modeling techniques may be required for better predictions.
Logistic Regression emerged as the most accurate model, making it the preferred choice.
Enhance resource allocation and improve services for Blue Bikes users.
Improve operational efficiency and customer satisfaction.


RECOMMENDATIONS

##  CONCLUSION

04

CONCLUSION

TECHNIQUE

Data Cleaning

Data Preprocessing

Exploratory Data Analysis (EDA)

Predictive Modeling

Model Evaluation

**PART 2**

# Bluebikes Data Analysis (Q1 2023)

This project provides a comprehensive analysis of the Bluebikes trip data for the first quarter of 2023. The main goal is to derive insights about how people use bicycles in Boston.

## Dataset Overview

The dataset contains information about individual bicycle trips, including:
- Trip duration
- Start and stop times
- Start and end station details
- Bike ID
- User type (Subscriber or Customer)
- Postal code

## Analyses Performed

1. Identification of the most popular start and end stations.
2. Analysis of the busiest times of day/month for bicycle trips.
3. Examination of the relationship between user type and trip length.
4. Investigation of the relationship between postal code and trip length.

## Contributions

Feel free to contribute to this analysis by creating pull requests or opening issues.

"""


