import streamlit as st
import pickle
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

# ------------------------------------------------------
# Load Data
# ------------------------------------------------------

# Load your processed dataframe (after tags creation)
merged = pickle.load(open('movies_df.pkl', 'rb'))

# Load similarity matrix generated from TF-IDF
similarity = pickle.load(open('similarity.pkl', 'rb'))

# ------------------------------------------------------
# Recommendation Function
# ------------------------------------------------------
def recommend(movie_title):
    if movie_title not in merged['title'].values:
        return []

    # Get movie index
    index = merged[merged['title'] == movie_title].index[0]

    # Fetch similarity scores
    distances = similarity[index]

    # Sort movies by similarity
    movies_list = sorted(list(enumerate(distances)),
                         key=lambda x: x[1], reverse=True)[1:11]

    recommended_movies = []
    scores = []
    for i, score in movies_list:
        recommended_movies.append(merged.iloc[i]['title'])
        scores.append(round(score, 3))

    return recommended_movies, scores

# ------------------------------------------------------
# Streamlit UI
# ------------------------------------------------------
st.set_page_config(page_title="Movie Recommender", layout="wide")

st.title("🎬 Movie Recommendation System")
st.write("Select a movie and get similar movie recommendations")

# Dropdown menu for movie selection
movie_list = merged['title'].values
selected_movie = st.selectbox("Select a movie:", movie_list)

# Recommend button
if st.button("Recommend"):
    names, scores = recommend(selected_movie)

    st.subheader("Top Recommendations:")
    
    for i in range(len(names)):
        st.write(f"**{i+1}. {names[i]}** — similarity score: `{scores[i]}`")
