import streamlit as st
import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

beer_prof = pd.read_csv(r'C:\Users\Anja Wittler\OneDrive\Dokumente\TG\WBS\bootcamp\project\data\beer\data\beer_profile_and_ratings_v5.csv')

list_of_beers_1 = tuple(beer_prof['Beer Name (Full)'])
list_of_beers_2 = tuple(beer_prof['Beer Name (Full)'])

beer_prof.drop_duplicates(inplace=True)

beer_simil = beer_prof.drop(['Style_red', 'Brewery', 'Description', 'number_of_reviews', 'review_aroma', 'review_appearance', 'review_palate', 'review_taste',
       'review_overall', 'country'], axis=1)

beer_simil.set_index('Beer Name (Full)', inplace=True)

def try_or_not_to_try(beer_A, beer_B):
    
    item_similarities = pd.DataFrame(cosine_similarity(beer_simil),
                                 columns=beer_simil.index, 
                                 index=beer_simil.index)
                                 
    data_simil = item_similarities.filter([beer_A])
    
    known_simil = item_similarities.filter([beer_A])
    
    result_score = data_simil.loc[beer_B,:][0]
    
    if result_score >= 0.95:
        return('no risk')
    elif result_score >= 0.8:
        return('yep - try it!')
    elif result_score >= 0.5:
        return('might be interesting')
    elif result_score >= 0.4:
        return('looking for a new experience?')
    else: return('hands-off')
    
     
st.title('to beer or not to beer..')


primaryColor="#F63366"
backgroundColor="#FFFFFF"

textColor="#262730"
font="cooper black"

base="dark"
    
beer_known = st.selectbox(
     'The beer you already know and like, just type the name',
     list_of_beers_1)

beer_new = st.selectbox(
     'The beer you do not know yet, just type the name',
     list_of_beers_2)

choice = try_or_not_to_try(beer_known, beer_new)

st.write('Your choice :', str(choice))


from PIL import Image
image = Image.open(r'C:\Users\Anja Wittler\OneDrive\Dokumente\TG\WBS\bootcamp\project\data\beer\data\2 beer.jpg')
st.image(image, caption='cheers!')
