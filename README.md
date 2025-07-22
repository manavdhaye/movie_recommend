# 🎬 Movie Recommendation System

A simple **Content-Based Movie Recommender System** built using **Streamlit**, **Pandas**, and **Pickle**, which suggests top 5 similar movies based on cosine similarity of movie metadata.

---

## 🚀 Features

- Select any movie from the dropdown.
- Get **Top 5 recommended movies** based on content similarity.
- Uses **movie metadata** like genres, cast, crew, and overview for comparison.
- Easy-to-use **web interface** built with Streamlit.

---

## 🧠 How It Works

1. Dataset used: [TMDB Movie Metadata](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)
2. Columns selected from the dataset:
   - `movie_id`, `genres`, `keywords`, `title`, `overview`, `cast`, `crew`
3. Preprocessing Steps:
   - Created a new `tags` column by combining the above metadata.
   - Applied **Count Vectorizer** to convert text data into numerical vectors.
   - Used **Cosine Similarity** to find similar movies based on these vectors.
4. Recommendation Logic:
   - When a user selects a movie, it fetches the most similar ones.
   - Returns the top 5 recommendations.

---

## 🛠 Tech Stack

- **Python**
- **Streamlit** – UI framework for building web apps
- **Pandas** – Data processing
- **Scikit-learn** – Vectorization and similarity computation
- **Pickle** – Model/data serialization

---

## 📂 Project Files

| File Name          | Description                                      |
|--------------------|--------------------------------------------------|
| `app.py`           | Main Streamlit app to run the recommender        |
| `movies_dict.pkl`  | Contains preprocessed movie metadata              |
| `similarity.pkl`   | Contains precomputed cosine similarity matrix     |

