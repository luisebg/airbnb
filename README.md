# Become a datascientist: project 1
## Airbnb datasets analysis: motivation
This repository was created to put in practice the learned lessons from the first part of the Udacity nanodegree "become a datascientist".

See the summary of the results in [The top 5 things that will make you the best Airbnb host](https://medium.com/@Luisebg/the-top-5-things-that-will-make-you-the-best-airbnb-host-a9f01b258030)

I aimed to follow the six steps of the CRoss Industry Standard Process for Data Mining or best known as CRISP-DM.
The mentioned steps are:
* Business understanding - what does the business need?
* Data understanding - what data do we have/need?
* Data preparation - how do we orgnize the data for modeling?
* Modeling - what modeling techniques should we apply?
* Evaluation - which model best meets the business objectives?
* Deployment - how do stakeholders access the results.
see reference [here](https://www.datascience-pm.com/crisp-dm-2/)

In this repository, the stakeholders will be the Medium audience who reads the article required by the project.

## Proposed questions
The main goal of the project is propose at least 3 questions and answer them based on Aibnb datasets.
The proposed questions are:
1. Which are the factors that dertermine the price of an airbnb? Location, commodities, etc.
2. Which are the most common amenities offered in Airbnb.
3. How is airbnb demand over the year? Which day of the week has more demand?

## Files description
* Data_analysis - answers the proposed questions from above.
* utils - it has some useful function required during the data analysis.
*  /Datasets/airbnb boston/zip-codes.geojson - JSON file with Seattle zip codes geometries.
*  /Datasets/airbnb seattle/zip-codes.geojson - JSON file with Seattle zip codes geometries.

## Setup
In order to run the files of this repository, you need to have python 3.x and install the following packages:

* pandas
* seaborn
* matplotlib
* folium
* json
* plotly

Download the [Seattle](https://www.kaggle.com/airbnb/seattle) and [Boston](https://www.kaggle.com/airbnb/boston) and move the calendar.csv and listings.csv files into their respective folders under /Datasets/.

## Licensing
This repository is licensed under MIT license. Feel free to use it as you need.

## Authors
Luis Enrique Beltran - data passionate and engineer

## Acknowledgements
Thanks to Continental Automotive that paid this training