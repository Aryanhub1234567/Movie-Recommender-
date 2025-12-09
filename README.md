# Movie-Recommender-
A machine learning–based movie recommendation system that analyzes user preferences and movie features using collaborative and content-based filtering to deliver personalized suggestions. It includes data preprocessing, model training, and performance evaluation.

Here is a clean, professional, and polished **README.md** for your TMDB Movie Recommendation System project — including setup, explanation, and Streamlit UI usage.

You can copy-paste this directly into a `README.md` file.

---

#  Movie Recommendation System (TMDB + TF-IDF + Cosine Similarity)

A content-based movie recommendation system built using:

* **TMDB 5000 Movies & Credits Dataset**
* **TF-IDF Vectorization**
* **Cosine Similarity**
* **Streamlit Web UI**
* **TMDB API (for posters)**

This project recommends movies based on **plot**, **genres**, **keywords**, **actors**, and **director**.

---

##  Features

✔ Cleans and preprocesses TMDB datasets
✔ Extracts genres, keywords, top 3 actors, and director
✔ Builds a combined **tags** feature
✔ Uses **TF-IDF vectorization** for text representation
✔ Computes **cosine similarity** between movies
✔ Generates top movie recommendations
✔ Beautiful **Streamlit UI**
✔ Fetches **movie posters** with TMDB API

---

##  Project Structure

```
├── tmdb_5000_movies.csv
├── tmdb_5000_credits.csv
├── movie_recommender.ipynb    # Data cleaning + model building
├── movies_df.pkl              # Processed dataframe
├── similarity.pkl             # Cosine similarity matrix
├── app.py                     # Streamlit app
├── README.md
```

---

##  Installation

### **1. Clone or download this project**

```
git clone <repo-url>
cd movie-recommender
```

### **2. Install required libraries**

```
pip install -r requirements.txt
```

(or install manually)

```
pip install pandas numpy scikit-learn streamlit requests
```

---

##  Dataset Used

TMDB datasets (from Kaggle / TMDB):

* **tmdb_5000_movies.csv**
* **tmdb_5000_credits.csv**

After merging, the following columns are used:

* `overview`
* `genres`
* `keywords`
* `cast` (top 3 actors)
* `crew` (director)
* `title`

These are combined into a single `tags` column.

---

##  Data Cleaning & Feature Engineering

###  JSON-like columns parsed:

* `genres`
* `keywords`
* `cast`
* `crew`

###  Extracted features:

* Genres list → `"action adventure fantasy"`
* Keywords list → `"dream subconscious heist"`
* Top 3 actors → `"leonardodicaprio josephgordonlevitt elliotpage"`
* Director → `"christophernolan"`
* Overview → cleaned & tokenized

###  Final `tags` column:

```
overview + genres + keywords + cast + director
```

---

##  Model Building

###  TF-IDF Vectorization

Transforms text into numerical vectors:

```python
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(merged['tags'])
```

###  Cosine Similarity

Computes similarity between movies:

```python
similarity = cosine_similarity(tfidf_matrix)
```

###  Recommendation Function

Returns top 10 similar movies based on cosine similarity.

---

##  Streamlit Web App

### **Run the app**

```
streamlit run app.py
```

### **Features in UI**

* Choose a movie from dropdown
* View recommended movies
* Posters displayed using TMDB API
* Clean responsive layout

---

##  TMDB API Integration

To fetch posters:

1. Create an account on [https://www.themoviedb.org](https://www.themoviedb.org)
2. Go to **Settings → API**
3. Generate **API Key (v3 auth)**
4. Replace in `app.py`:

```python
API_KEY = "YOUR_TMDB_API_KEY"
```

---

##  Screenshots (Optional)

*Add UI screenshots here if you want.*

---

##  Future Enhancements

* Add movie overview in recommendations
* Add actor & director details
* Add rating/popularity filters
* Replace TF-IDF with Word2Vec / BERT embeddings
* Build a collaborative filtering version
* Deploy on Streamlit Cloud or HuggingFace Spaces

---

##  Contributing

Pull requests and improvements are welcome!

---

##  License

This project is open-source (MIT License).

---


