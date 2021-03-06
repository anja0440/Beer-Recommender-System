# The Beer-Commender-System

WBS - Data Science final project on Recommender-Systems

The beer-commender will help to select the beer from a menu card, which is closest to one's known preference.


# Project Description

According to latest surveys, the number of breweries worldwide is about 19.000 brewing hundreds of thousands individual beers, 
of more than 100 different styles.

And one does not have to travel far to try a new one, as restaurants with specific regional cuisines offer a variety of different beers.

It is always a good thing to try something new but with regards to beer, there is such a wide range in taste, that you
can easily select one which you do not like at all.

In case of wine, with some experience, one can judge the taste on origin or grape - but what about hops?
What can give some indication about similarity of taste, when it is about beer?

The aim of this Beer-(Re)Commender-System is to provide this indication and a recommendation:
A web-app, which makes it easier to select the right beer for instance from a menu card.


# Data

I used these 2 datasets:

https://www.kaggle.com/datasets/ruthgn/beer-profile-and-ratings-data-set

https://public.opendatasoft.com/explore/dataset/open-beer-database-breweries/export/?disjunctive.state&disjunctive.country



And these sources for more detailed information about beer:

https://www.lanereport.com/74898/2017/03/alltech-and-brewers-journal-survey-finds-94-of-worlds-19000-breweries-are-craft-u-s-has-4750/

https://shorecraftbeer.com/abv-and-ibu-explained/

https://hoohhops.com/beer-characteristics/

https://winning-homebrew.com/beer-astringency.html

https://www.beeradvocate.com/



The data from Kaggle was very clean and contained this information:

Name: Beer name (label)

Style: Beer Style

Brewery: Brewery name

Beer Name (Full): Complete beer name (Brewery + Brew Name), unique identifier for each beer

Description: Notes on the beer if available

ABV: Alcohol content of beer (% by volume)

Min IBU: The minimum IBU value each beer can possess. IBU was not a value available for each beer, but the IBU range for each style was

Max IBU: The maximum IBU value each beer can possess. IBU was not a value available for each beer, but the IBU range for each style was

Mouthfeel: Astringency / Body / Alcohol

Taste: Bitter / Sweet / Sour / Salty

Flavor And Aroma: Fruits / Hoppy / Spices / Malty

The values for each parameter were defined by word counts found in reviews of each beer, coming from appr. 1.5 million reviews on https://www.beeradvocate.com/.

The different types for 'Style' were simplified to generate more meaningful graphics in Tableau (example: 'Porter - American' and 'Porter - Imperial' are reduced to 'Porter).

With the dataset from Opendatasoft I was able to add the origin (country) by brewery.


# Code

The coding was done with Python in a Jupyter Lab notebook, the visualization with Tableau and for the web-app, I used Streamlit.
('Country' and 'Style_red' columns were added with Excel.)


# Visualization of correlation

In Tableau I created different plots to show the correlation of 'mouthfeel', 'taste', 'flavor' and country and 'mouthfeel', 'taste', 'flavor' and style.

In case of the country-related correlation, some regional differences were highlighted, 
and in case of style, the data was reduced to 5 different types: 'Pilsner', 'Bock', 'Lager', 'Wheat Beer' and 'Stout'.

Though this is not a kind of "scientific" analysis, the output of the reviews do provide a distinction of perception of features as 'bitter', 'sweet', 'body', etc..
It proves for instances my own experience that Pilsner is more on the bitter side compared to Stout or Bock.

Similarily the graphics give the impression that Icelandic beers are more malty than from other countries, but in the end it only shows the difference from given reviews.


As the use and amount of specific keywords says more about the reviewer as about the tasted beer, I found the median an appropriate metric.


# Similarities and web-app

To define the similarity, all categorical data except of 'Beer Name (Full)' were dropped. 

Then I took the pairwise cosine_similarity from sklearn and wrote a function which returns a score between 0 and 1: 1 indicating perfect match and 0 the widest distance.

This code is then run with streamlit.


On the web-app, first a beer is selected which one is familiar with and then the unknown is chosen, for example from a menu card.


The web-app will now give a recommendation:

score >= 0.95: 'no risk'

score >= 0.8: 'yep - try it!'

score >= 0.5: 'might be interesting'

score >= 0.4: 'looking for a new experience?'

score < 0.4. 'hands-off'



CHEERS!

