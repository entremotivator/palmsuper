# main.py

import streamlit as st
from recommend_movies import RecommendMovies

# Load secrets from st.secrets
palm_api_key = st.secrets["palm_api"]["key"]

# Use the API key in your code
SESSION_HEADERS = {
    "accept": "application/json",
    "Authorization": f"Bearer {palm_api_key}"
}

st.title("Recommendation System Using Palm")
text_box = st.text_input("Your movie goes here 🎥")
col1, col2 = st.columns(2)

r_m = RecommendMovies(api_key=palm_api_key)

if text_box:
    result = r_m.generate(str(text_box))

    for i in range(len(result)):
        if result[i] != []:
            if i % 2 == 0:
                col1.image(f"https://image.tmdb.org/t/p/w300_and_h450_bestv2{result[i][0]['poster_path']}")
                col1.write(result[i][0]['title'])
            else:
                col2.image(f"https://image.tmdb.org/t/p/w300_and_h450_bestv2{result[i][0]['poster_path']}")
                col2.write(result[i][0]['title'])
