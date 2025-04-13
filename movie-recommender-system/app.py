import streamlit as st
import pickle
import pandas as pd
import requests
# import streamlit as st

# Custom CSS for background image
page_bg_css = f"""
<style>
body {{
    background-image: url("https://images.alphacoders.com/128/1286361.jpg");
    background-size: cover; /* Ensures the image covers the entire page */
    background-repeat: no-repeat;
    background-attachment: fixed; /* Keeps the image fixed during scrolling */
    opacity: 0.8; /* Adjusts the opacity of the background */
}}
</style>
"""

# Apply CSS to the page
st.markdown(page_bg_css, unsafe_allow_html=True)


def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=606f0a99068edc096beedfaeafbb32ce&language=en-US'.format(movie_id))
    data =response.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']
def recommend(movie):
    movie_index=movies[movies['title']==movie].index[0]
    distances=similarity[movie_index]
    movie_list=sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]
    recommed_movies=[]
    recommed_movies_poster=[]
    for i in movie_list:
        movie_id=movies.iloc[i[0]].movie_id
        recommed_movies.append(movies.iloc[i[0]].title)
        recommed_movies_poster.append(fetch_poster(movie_id))

    return recommed_movies,recommed_movies_poster

movie_dict=pickle.load(open('movie_dict.pkl', 'rb'))
movies=pd.DataFrame(movie_dict)
similarity=pickle.load(open('similarity.pkl', 'rb'))



st.title('Movie Recommender System')
selected_movie_name = st.selectbox(
    "How would you like to be contacted?",
    movies['title'].values)
if st.button("Recommend"):
    names,poster=recommend(selected_movie_name)
    col1, col2, col3,col4,col5 = st.columns(5)

    with col1:
        st.text(names[0])
        st.image(poster[0])
    with col2:
        st.text(names[1])
        st.image(poster[1])
    with col3:
        st.text(names[2])
        st.image(poster[2])
    with col4:
        st.text(names[3])
        st.image(poster[3])
    with col5:
        st.text(names[4])
        st.image(poster[4])




