# Cricket-Prediction
Indian Cricket Team Prediction for World Cup ODI

# Cricket Prodigy Predictor

Welcome to the Cricket Prodigy Predictor repository! 🏏

## Project Overview

In the thrilling world of cricket, where every ball can change the course of a match, we present to you the Cricket Prodigy Predictor. This data science project focuses on forecasting the performance of batsmen in One Day International (ODI) matches, especially in the high-stakes arena of the Cricket World Cup.

## Mission

Our mission is to leverage machine learning to develop a predictive algorithm that considers various factors such as opposing teams, venue conditions, and the current form of players. By diving into the dynamic strategies of cricket, we aim to provide accurate forecasts for individual player performances.

## Acknowledgements

- Research insights contributed by Kalpdrum Passi and Niravkumar Pandey from Laurentian University, Sudbury, Canada.
- Data scraping and analytics from espncricinfo.com & Statsguru.
- Weather-related data fetched through openweathermap.org API.

## Approach

After an in-depth analysis of different models, the Random Forest emerged as the champion for this project. Its ability to create an ensemble of decision trees proved effective in predicting batsmen performance, considering the multitude of factors involved in the game.

## Stages of the Project

### 1. Data Collection
We gathered data about players and their historical records from espncricinfo using pandas dataframe methods like `pd.read_html()` and inspect method extraction through Chrome. Weather data was collected using the openweathermap.org API.

### 2. Data Engineering

This crucial phase involved organizing and enhancing the data. Techniques like feature selection, one-hot encoding for weather and opposition teams, frequency encoding for the ground (pitch), and correlation matrix for feature selection were employed. Cleaning up null values and transforming attribute types were also part of this phase.
# Feature Importance 
* **Correlation Matrix**
  <p align="center">
  <a href="https://postimg.cc/4Yy50Bvh" target="_blank">
    <img src="https://i.postimg.cc/t4tMYcYD/plot-2.png" alt="Correlation Chart">
  </a>
</p>

### 3. Model Selection and Prediction
With 40 Random Forest models in action, we predicted the performance of Indian batsmen for various metrics such as 4s, 6s, 100s, and 50s. The results were not just acceptable but impressive, providing valuable insights into player capabilities.

### 4. Reiterating

To ensure the highest accuracy, we iterated through the entire process multiple times, fine-tuning our models and processes for better results.

### 5. Deployment

The model is deployed on Streamlit Cloud Hosting, offering a user-friendly interface for exploring the predictions. The frontend is built using Streamlit, providing an intuitive and engaging experience.

## User Architecture

Different scores are evaluated based on consistency, which is a function of strike rate, number of 4s, number of 6s, number of 50s, and number of 100s. Psychological readiness is determined by considering both consistency and the preferred weather conditions when the player performed at their best.
<p align="center">
  <a href="https://postimg.cc/yW2n3m1r" target="_blank">
    <img src="https://i.postimg.cc/VLkhTg31/Flow-Chart.png" alt="Flow Chart">
  </a>
</p>


## Explore the App

Check out our prediction model in action! Visit the [Cricket Prodigy Predictor App](https://cricket-prediction.streamlit.app/) and witness the magic of data science unfolding.

Feel free to explore, analyze, and enjoy the exciting world of cricket predictions! 🚀

*Note: For more detailed insights and technical details, refer to the project's Jupyter notebooks and scripts in the repository.*

