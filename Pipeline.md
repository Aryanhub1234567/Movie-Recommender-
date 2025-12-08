Convert Movie Text (Genre + Description) into Numerical Vectors
Here’s a **clear, simple, and project-specific explanation** of how **cosine similarity** is implemented in your movie recommendation system.

---

# ⭐ How Cosine Similarity Is Implemented in This Movie Recommender Project

The Cosine Similarity implementation happens in **three main steps**:

---

# **1. Convert Movie Text (Genre + Description) into Numerical Vectors**

In the code:

```python
movies['features'] = movies['genre'] + ' ' + movies['description']
vectorizer = TfidfVectorizer(stop_words='english')
feature_vectors = vectorizer.fit_transform(movies['features'])
```

### What this does:

* Each movie has text like `"Sci-Fi Thriller A thief enters dreams..."`.
* TF-IDF vectorizer converts this **text into a vector of numbers**.
* Each number represents how important a word is for a movie.

So now each movie = a large vector like:

```
[0.21, 0.00, 0.13, 0.56, ...]
```

---

# **2. Calculate Cosine Similarity Between All Movie Vectors**

```python
similarity = cosine_similarity(feature_vectors)
```

### What this does:

* Compares every movie with every other movie.
* Creates a matrix like:

| Movie         | Inception | Matrix | Tenet | ... |
| ------------- | --------- | ------ | ----- | --- |
| **Inception** | 1.00      | 0.68   | 0.71  | ... |
| **Matrix**    | 0.68      | 1.00   | 0.53  | ... |
| **Tenet**     | 0.71      | 0.53   | 1.00  | ... |

### Why cosine similarity?

Cosine similarity measures the **angle between two vectors**, not magnitude.

Formula:
$$
[
\text{cosine similarity} = \frac{A \cdot B}{||A|| , ||B||}
]
$$
Meaning:

* If the angle is small → vectors aligned → very similar.
* Values range **0 (different)** to **1 (identical)**.

This is perfect for TF-IDF where:

* Long descriptions don’t overpower short ones.
* Only the text meaning matters.

---

# **3. Get Top Similar Movies for a Given Movie**

In the recommender function:

```python
index = movies[movies['title'] == movie_title].index[0]
similarity_scores = list(enumerate(similarity[index]))
sorted_scores = sorted(similarity_scores, key=lambda x: x[1], reverse=True)
```

### What happens:

* Pick similarity row for the chosen movie.
* Sort movies by high similarity.
* Return the top similar ones.

Example:

If you call:

```python
recommend('Inception')
```

The system finds other movies with similar:

* genres
* descriptions
* keywords

because their feature vectors have **small angles between them**.

---

# ⭐ In One Line

**Cosine similarity works by converting movie text into numerical vectors using TF-IDF, then measuring how similar these vectors are by comparing their angles.**

---

Here is the **exact list of columns from `tmdb_5000_movies.csv` that are useful for a content-based movie recommendation system** — and which ones you can ignore.

---

# ✅ **Useful Columns (Keep These)**

### **1. title**

* Needed for input and output of your recommendation system.

### **2. overview**

* Main natural-language description of the movie.
* Perfect for TF-IDF / text vectorization.
* Very important for similarity.

### **3. genres**

* Contains genre metadata (e.g., Action, Adventure).
* Helps cluster movies by themes.

### **4. keywords**

* Important for identifying movie topics.
* Usually contains concepts like “dream”, “future”, “space travel”.

### **5. id**

* Useful for merging with `tmdb_5000_credits.csv`.
* Not directly used in recommendations.

---

# 🟡 **Optional but Can Be Used (If You Want Advanced Features)**

### **6. tagline**

* A short slogan; can improve text features slightly.

### **7. popularity**

* Numeric score; can be used to break ties or rank results.

### **8. vote_average**

* Can be used to rank higher-rated movies first *after* similarity.

### **9. vote_count**

* Helps filter out less-rated movies.

### **10. original_language**

* Can be used to filter recommendations by language.

---

# ❌ **Not Useful for Basic Content-Based Recommendation (Ignore These)**

These do **not** help determine content similarity:

* **budget**
* **homepage**
* **production_companies**
* **production_countries**
* **release_date**
* **revenue**
* **runtime**
* **spoken_languages**
* **status**
* **original_title**

These are either:

* numeric irrelevant features
* metadata that doesn’t define “similar story/plot”
* not helpful in content-based filtering

---

# ⭐ Final Recommended Features to Use

For a solid TMDB content-based movie recommender:

### ✔ **title**

### ✔ **overview**

### ✔ **genres**

### ✔ **keywords**

### ✔ **(from credits.csv)** cast & director

These together build a strong “tags” feature.

---

# If you want next:

I can share the **exact list of steps** to convert these useful columns into a final “tags” column (without code), or build the full recommendation system notebook.

Just tell me!
