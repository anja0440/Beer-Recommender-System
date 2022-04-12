# The Beer-Commender-System

A WBS - Data Science - final project on recommender-systems

The beer-commender will help to select the beer from a menu card, which is closest to one's known preference.


# Project Description

According to latest surveys, the number of breweries worldwide is about 20.000 and most restaurants with specific regional
cuisines offer a variety of different beers.


It is always interesting to taste a new type of beer but there is such a wide range in taste, that you
can easily select one which you do not like at all.

In case of wine, for example, - with some experience - one can judge on origin or grape - but what about hops?
What can give some indication about similarity of taste, flavors or mouthfeel?

Providing this indication and a recommendation is the aim of my Beer-Commender-System:
A web-app, that makes it easier to select a type from a list, as for instance from a menu card.


# Data

I have been using these 2 datasets:

https://www.kaggle.com/datasets/ruthgn/beer-profile-and-ratings-data-set

https://public.opendatasoft.com/explore/dataset/open-beer-database-breweries/export/?disjunctive.state&disjunctive.country



And these sources for more detailed information about beer:

https://shorecraftbeer.com/abv-and-ibu-explained/

https://hoohhops.com/beer-characteristics/

https://winning-homebrew.com/beer-astringency.html



The data from Kaggle was already clean and contained this information:

Name: Beer name (label)

Style: Beer Style

Brewery: Brewery name

Beer Name (Full): Complete beer name (Brewery + Brew Name) -- unique identifier for each beer

Description: Notes on the beer if available

ABV: Alcohol content of beer (% by volume)

Min IBU: The minimum IBU value each beer can possess. IBU was not a value available for each beer, but the IBU range for each style was

Max IBU: The maximum IBU value each beer can possess. IBU was not a value available for each beer, but the IBU range for each style was

Mouthfeel: Astringency / Body / Alcohol

Taste: Bitter / Sweet / Sour / Salty

Flavor And Aroma: Fruits / Hoppy / Spices / Malty

(There was als information about reviews but I did not include this into my project as there is no point in arguing about matters of taste .. .)


With the dataset from Opendatasoft I was able to add the origin (country) by brewery.


The total number of different beer types is 779, with breweries in: United States, Germany, United Kingdom, Ireland, Belgium, Norway, Canada, France, Netherlands, Finland, Austria, 
Russia, Czech Republic, Greece, New Zealand, Lithuania, Poland, Japan, Sweden, Latvia.

# Code

The coding was done with Python in a Jupyter Lab notebook, the visualization with Tableau and for the web-app, I used Streamlit.


In Tableau some regional differences could be highlighted. 
Using median for each feature, for instance regarding 'maltyness' a clear difference is visible for countries Belgium and Ireland. 
(Which, of course, is based on the available data and might change, the more beer types are added.)


To define the similarity, all categorical data except of 'Beer Name (Full)' were dropped. 

Then I took the pairwise cosine_similarity from sklearn and wrote a function which returns a score between 0 and 1: 1 indicating perfect match and 0 the widest distance.

This code was then run with streamlit.

On the web-app, first a beer is selected which one already knows and likes and then another from, for example, a menu card is chosen.

The web-app will now hen give a recommendation:

score >= 0.95: 'no risk'

score >= 0.8: 'yep - try it!'

score >= 0.5: 'might be interesting'

score >= 0.4: 'looking for a new experience?'

score < 0.4. 'hands-off'



CHEERS!

