# Movie Recommendation System (Content-Based)
# Run this in a Jupyter Notebook. Each cell is separated by comments.

# --- Cell 1: Install & Import Libraries ---
# !pip install pandas scikit-learn
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# --- Cell 2: Create Sample Movie Dataset ---
data = {
    'title': [
        'Inception', 'Interstellar', 'The Dark Knight', 'The Matrix',
        'The Prestige', 'Shutter Island', 'Memento', 'Tenet',
        'The Social Network', 'The Imitation Game'
    ],
    'genre': [
        'Sci-Fi Thriller', 'Sci-Fi Adventure', 'Action Crime', 'Sci-Fi Action',
        'Mystery Thriller', 'Psychological Thriller', 'Mystery Thriller', 'Sci-Fi Thriller',
        'Drama Biography', 'Drama Biography'
    ],
    'description': [
        'A thief enters dreams to steal secrets.',
        'A team travels through a wormhole in space.',
        'Batman fights the Joker in Gotham City.',
        'A hacker discovers the world is a simulation.',
        'Two magicians compete with dangerous tricks.',
        'A marshal investigates a psychiatric facility.',
        'A man with short-term memory loss seeks revenge.',
        'A secret agent manipulates time to stop an attack.',
        'The rise of Facebook and Mark Zuckerberg.',
        'A mathematician cracks wartime codes.'
    ]
}

movies = pd.DataFrame(data)
movies

# --- Cell 3: Combine Genre + Description for Features ---
movies['features'] = movies['genre'] + ' ' + movies['description']

# --- Cell 4: Vectorize Text Data ---
vectorizer = TfidfVectorizer(stop_words='english')
feature_vectors = vectorizer.fit_transform(movies['features'])

# --- Cell 5: Compute Similarity ---
similarity = cosine_similarity(feature_vectors)

# --- Cell 6: Recommendation Function ---
def recommend(movie_title):
    if movie_title not in movies['title'].values:
        return f"'{movie_title}' not found in movie list."

    index = movies[movies['title'] == movie_title].index[0]
    similarity_scores = list(enumerate(similarity[index]))

    sorted_scores = sorted(similarity_scores, key=lambda x: x[1], reverse=True)

    print(f"Recommendations for: {movie_title}\n")
    for i, score in sorted_scores[1:6]:  # top 5
        print(f"{movies.iloc[i]['title']}  (Similarity: {round(score,2)})")

# --- Cell 7: Try It ---
recommend('Inception')
