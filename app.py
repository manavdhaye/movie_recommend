import streamlit as st
import pickle
import pandas as pd
import requests

movies_dict = pickle.load(open("movies_dict.pkl", "rb"))
movie = pd.DataFrame(movies_dict)
similarity = pickle.load(open("similarity.pkl", "rb"))

st.title("Movie Recommend System")
# def fetch_poster(movie_id):
#     url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=e35dc50ce48f138827d97f4247d37089"
#     response=requests.get(url)
#     data=response.json()
#     return f"https://image.tmdb.org/t/p/original{data['poster_path']}"

def recommend(selected_movie):
    movie_index = movie[movie["title"] == selected_movie].index[0]
    distances = similarity[movie_index]

    recommended_movies = []
    #recommend_poster=[]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    for i in movie_list:
        recommended_movies.append(movie.iloc[i[0]].title)
        #recommend_poster.append(fetch_poster(movie.iloc[i[0]].movie_id))
    return recommended_movies

select_movie_name = st.selectbox(
    "Select a movie:",
    movie['title'].values,
)

if st.button("Recommend"):
    recommended_names = recommend(select_movie_name)
    st.subheader("Top 5 Recommended Movies:")
    for idx, name in enumerate(recommended_names, start=1):
        st.write(f"{idx}. {name}")


