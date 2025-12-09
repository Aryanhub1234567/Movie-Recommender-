import streamlit as st
import pickle
import pandas as pd
import requests

# ------------------------------------------------------
# Load Data
# ------------------------------------------------------
merged = pickle.load(open('movies_df.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

API_KEY = "YOUR_TMDB_API_KEY"

# ------------------------------------------------------
# TMDB Poster Fetch Function
# ------------------------------------------------------
def fetch_poster(movie_title):
    """Fetch poster for a given movie title using TMDB API."""
    url = f"https://api.themoviedb.org/3/search/movie?api_key={API_KEY}&query={movie_title}"
    data = requests.get(url).json()
    
    # If no results, return a placeholder
    if data["results"] == []:
        return "https://via.placeholder.com/500x750?text=No+Poster"
    
    poster_path = data["results"][0].get("poster_path", None)

    if poster_path:
        full_path = "https://image.tmdb.org/t/p/w500" + poster_path
        return full_path
    else:
        return "https://via.placeholder.com/500x750?text=No+Poster"

# ------------------------------------------------------
# Recommendation Function
# ------------------------------------------------------
def recommend(movie_title):
    if movie_title not in merged['title'].values:
        return [], []

    index = merged[merged['title'] == movie_title].index[0]
    distances = similarity[index]

    movies_list = sorted(list(enumerate(distances)),
                         key=lambda x: x[1], reverse=True)[1:11]

    recommended_movies = []
    posters = []

    for i, _ in movies_list:
        movie_name = merged.iloc[i]['title']
        recommended_movies.append(movie_name)
        posters.append(fetch_poster(movie_name))

    return recommended_movies, posters

# ------------------------------------------------------
# Streamlit UI
# ------------------------------------------------------
st.set_page_config(page_title="Movie Recommender", layout="wide")

st.title("🎬 Movie Recommendation System")
st.write("Select a movie to get recommendations along with posters")

movie_list = merged['title'].values
selected_movie = st.selectbox("Select a movie:", movie_list)

if st.button("Recommend"):
    names, posters = recommend(selected_movie)

    st.subheader("Top Recommendations:")

    cols = st.columns(5)  # Display 5 posters per row

    for i in range(len(names)):
        with cols[i % 5]:
            st.image(posters[i], width=150)
            st.text(names[i])
            st.markdown("---")

