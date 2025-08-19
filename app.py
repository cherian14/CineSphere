import streamlit as st
import pandas as pd
import numpy as np
import requests
import os
import re
import random

# --- [CORRECTED IMPORTS] ---
# These lines were missing, causing the error. They are now restored.
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
from sklearn.decomposition import TruncatedSVD

# --- [CONFIGURATION] ---
st.set_page_config(page_title="CineSphere", layout="wide", initial_sidebar_state="collapsed")
TMDB_API_KEY = '834637f1ba956e811582e872eea42dea'
DATASET_DIR = 'ml-latest-small'

# --- [DYNAMIC VISUALS] ---
CINEMATIC_BACKDROPS = [
    'https://image.tmdb.org/t/p/original/h8gHn0OzBoaefsYseUoMHuSm0EC.jpg', # Blade Runner 2049
    'https://image.tmdb.org/t/p/original/d5NXSklXo0qyIY2VIFlznpCw9p0.jpg', # Dune
    'https://image.tmdb.org/t/p/original/xJHokMbljvjADYdit5fKbrVNERo.jpg', # Interstellar
    'https://image.tmdb.org/t/p/original/kGzFbGhp99zva6oZODW5atUtnqi.jpg', # The Dark Knight
]
selected_backdrop = random.choice(CINEMATIC_BACKDROPS)


# --- [THE CINEMATIC ENGINE: STYLING & UI] ---
st.markdown(f"""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@700;900&family=Lato:wght@400;700&display=swap');
        
        .stApp {{ background: #141414; color: #FFFFFF; font-family: 'Lato', sans-serif; }}
        h1, h2, h3, h4, h5, h6 {{ font-family: 'Montserrat', sans-serif; color: #FFFFFF; }}
        header, footer, [data-testid="stSidebar"], .css-1d391kg {{ display: none !important; }}
        
        /* --- Hero Section (Netflix Style) --- */
        .hero {{
            position: relative; height: 90vh; display: flex; align-items: center; justify-content: center; text-align: center; padding: 2rem;
            background-image: url('{selected_backdrop}');
            background-size: cover; background-position: center;
        }}
        .hero::before {{
            content: ''; position: absolute; top: 0; left: 0; right: 0; bottom: 0;
            background: linear-gradient(to top, #141414 10%, rgba(20, 20, 20, 0.6) 50%, #141414 100%);
        }}
        .hero-content {{ position: relative; z-index: 2; }}
        .hero-title {{ font-family: 'Montserrat', sans-serif; font-weight: 900; font-size: 4.5rem; text-shadow: 0 0 30px rgba(0,0,0,0.9); }}
        .hero-subtitle {{ font-size: 1.5rem; margin-top: 1rem; }}

        /* --- Content Sections --- */
        .section {{ padding: 4rem 5%; border-bottom: 8px solid #222; }}
        .section-header {{ font-size: 2.5rem; font-weight: 700; margin-bottom: 1.5rem; text-align: center; }}

        /* --- Button Styles --- */
        .stButton>button {{
            background-color: rgba(109, 109, 110, 0.4); color: #FFFFFF; border: 1px solid rgba(109, 109, 110, 0.7);
            padding: 1rem; border-radius: 8px; font-weight: bold; font-family: 'Montserrat', sans-serif;
            transition: all 0.2s ease; height: 100%;
        }}
        .stButton>button:hover {{ background-color: rgba(229, 9, 20, 0.7); border-color: rgba(229, 9, 20, 0.7); transform: scale(1.05); }}
        
        /* Primary Action Button (Netflix Red) */
        .st-emotion-cache-p5msec {{
            background-color: #E50914 !important;
            border: none !important;
            font-size: 1.2rem !important;
            padding: 1rem 2rem !important;
            border-radius: 4px !important;
            width: auto !important;
            margin: 1rem auto !important;
            display: block !important;
        }}
        .st-emotion-cache-p5msec:hover {{
            background-color: #F6121D !important;
        }}

        /* --- Poster & Results Styling --- */
        .poster-container img {{ border-radius: 8px; transition: transform 0.2s ease-in-out; }}
        .poster-container img:hover {{ transform: scale(1.05); border: 2px solid #fff; }}
        .results-container {{ min-height: 400px; }}

        /* --- Footer --- */
        .footer {{ text-align: center; padding: 2rem; color: #767676; }}
        .footer a {{ color: #767676; text-decoration: none; }}
        .footer a:hover {{ text-decoration: underline; }}
    </style>
""", unsafe_allow_html=True)


# --- [DATA LOADING & MODEL TRAINING ENGINE] ---
@st.cache_resource
def load_data_and_train_models():
    if not os.path.exists(DATASET_DIR):
        st.error(f"FATAL: Dataset folder '{DATASET_DIR}' not found. Please follow manual download instructions.")
        st.stop()
    movies = pd.read_csv(os.path.join(DATASET_DIR, 'movies.csv'))
    ratings = pd.read_csv(os.path.join(DATASET_DIR, 'ratings.csv'))
    
    movie_stats = ratings.groupby('movieId').agg(rating_count=('rating', 'count'), rating_avg=('rating', 'mean'))
    movies = movies.merge(movie_stats, on='movieId', how='left').fillna(0)
    movies['trending_score'] = movies['rating_avg'] * np.log(movies['rating_count'] + 1)
    
    movies['genres_str'] = movies['genres'].str.replace('|', ' ', regex=False).fillna('')
    tfidf_vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = tfidf_vectorizer.fit_transform(movies['genres_str'])
    cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)
    movies = movies.reset_index()
    title_to_index = pd.Series(movies.index, index=movies['title'])
    return movies, cosine_sim, title_to_index

movies_df, cosine_sim, title_to_index = load_data_and_train_models()


# --- [HELPER & RECOMMENDATION FUNCTIONS] ---
def get_movie_poster(movie_title):
    clean_title = re.sub(r'\s*\(\d{4}\)$', '', movie_title)
    search_url = f"https://api.themoviedb.org/3/search/movie?api_key={TMDB_API_KEY}&query={clean_title}"
    try:
        r = requests.get(search_url); r.raise_for_status()
        data = r.json()
        if data['results']:
            poster_path = data['results'][0]['poster_path']
            if poster_path: return f"https://image.tmdb.org/t/p/w500/{poster_path}"
    except: return None
    return None

def get_mood_based_recommendations(mood, n=5):
    genre_map = {
        "thrilling": ["Action", "Thriller", "Crime", "War"], "heartfelt": ["Romance", "Drama", "Children"],
        "visionary": ["Sci-Fi", "Fantasy", "IMAX"], "lighthearted": ["Comedy", "Adventure", "Musical"],
        "unsettling": ["Horror", "Mystery", "Film-Noir"], "epic": ["Adventure", "War", "Western"],
        "imaginative": ["Animation", "Fantasy", "Children"], "acclaimed": ["Drama", "Documentary"],
        "witty": ["Comedy", "Romance"], "mysterious": ["Mystery", "Thriller", "Sci-Fi"]
    }
    target_genres = genre_map.get(mood, [])
    if not target_genres: return pd.DataFrame()
    genre_regex = "|".join(target_genres)
    candidate_movies = movies_df[movies_df['genres'].str.contains(genre_regex, case=False, na=False)]
    return candidate_movies.sample(n, random_state=42) if len(candidate_movies) > n else candidate_movies

def get_content_based_recommendations(title, n=5):
    if title not in title_to_index: return pd.DataFrame()
    idx = title_to_index[title]
    sim_scores = sorted(list(enumerate(cosine_sim[idx])), key=lambda x: x[1], reverse=True)[1:n+1]
    movie_indices = [i[0] for i in sim_scores]
    return movies_df.iloc[movie_indices]

# =================================================================================
# --- [THE NARRATIVE INTERFACE: A SINGLE, SCROLLING CANVAS] ---
# =================================================================================

# --- HERO SECTION ---
st.markdown(f"""
<div class="hero">
    <div class="hero-content">
        <h1 class="hero-title">Unlimited cinematic journeys.</h1>
        <h2 class="hero-subtitle">Your story begins with a single choice.</h2>
    </div>
</div>
""", unsafe_allow_html=True)


# --- TRENDING NOW SHELF ---
with st.container():
    st.markdown('<div class="section">', unsafe_allow_html=True)
    st.markdown('<h2 class="section-header">Trending Now</h2>', unsafe_allow_html=True)
    trending_movies = movies_df.sort_values('trending_score', ascending=False).head(10)
    trend_cols = st.columns(10)
    for i, (idx, row) in enumerate(trending_movies.iterrows()):
        poster = get_movie_poster(row['title'])
        if poster: trend_cols[i].image(poster, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)


# --- SEARCH ENGINE SECTION (The Archive) ---
with st.container():
    st.markdown('<div class="section">', unsafe_allow_html=True)
    st.markdown('<h2 class="section-header">The Archive</h2>', unsafe_allow_html=True)
    st.write("For the seasoned enthusiast. Analyze the cinematic DNA of a known masterpiece to reveal its artistic siblings.")
    
    if 'archive_results' not in st.session_state: st.session_state.archive_results = None
    if 'quiz_results' not in st.session_state: st.session_state.quiz_results = None

    movie_list = movies_df['title'].sort_values().tolist()
    movie_input = st.selectbox("Choose a Masterpiece for Analysis:", movie_list, index=movie_list.index("Matrix, The (1999)"), label_visibility="collapsed")
    num_recommendations = st.slider("Number of Similar Films to Reveal:", min_value=1, max_value=10, value=5)

    if st.button("Analyze & Reveal Similar Films", type="primary"):
        st.session_state.archive_results = get_content_based_recommendations(movie_input, num_recommendations)
        st.session_state.quiz_results = None
        
    archive_results_container = st.container(border=False)
    if st.session_state.archive_results is not None:
         with archive_results_container:
            st.write("---"); st.markdown(f"### For the admirer of '{movie_input}':")
            rec_cols = st.columns(num_recommendations)
            for i, (idx, row) in enumerate(st.session_state.archive_results.iterrows()):
                poster = get_movie_poster(row['title'])
                if poster: rec_cols[i].image(poster, caption=row['title'], use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)


# --- INTERACTIVE QUIZ SECTION (The Director's Chair) ---
with st.container():
    st.markdown('<div class="section">', unsafe_allow_html=True)
    st.markdown('<h2 class="section-header">The Director\'s Chair</h2>', unsafe_allow_html=True)
    st.write("Or, if you seek inspiration, tell us the emotional core of your desired story. Your choice crafts the narrative.")

    moods = {
        "Thrilling & Intense": "thrilling", "Heartfelt & Emotional": "heartfelt", "Visionary & Complex": "visionary",
        "Lighthearted & Fun": "lighthearted", "Dark & Unsettling": "unsettling", "Epic & Grandiose": "epic",
        "Imaginative & Animated": "imaginative", "Critically-Acclaimed": "acclaimed", "Witty & Charming": "witty",
        "Mysterious & Tense": "mysterious"
    }
    
    quiz_cols_1 = st.columns(5)
    quiz_cols_2 = st.columns(5)
    mood_list = list(moods.items())

    for i in range(5):
        mood_text, mood_key = mood_list[i]
        if quiz_cols_1[i].button(mood_text, key=f"mood_{i}"):
            st.session_state.quiz_results = get_mood_based_recommendations(mood_key, 5)
            st.session_state.archive_results = None
    for i in range(5, 10):
        mood_text, mood_key = mood_list[i]
        if quiz_cols_2[i-5].button(mood_text, key=f"mood_{i}"):
            st.session_state.quiz_results = get_mood_based_recommendations(mood_key, 5)
            st.session_state.archive_results = None

    quiz_results_container = st.container(border=False)
    if st.session_state.quiz_results is not None:
        with quiz_results_container:
            st.write("---"); st.markdown("### Your Curated Narrative:")
            rec_cols = st.columns(5)
            for i, (idx, row) in enumerate(st.session_state.quiz_results.iterrows()):
                poster = get_movie_poster(row['title'])
                if poster: rec_cols[i].image(poster, caption=row['title'], use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

# --- FOOTER ---
st.markdown("""
<div class="footer">
    <p>CineSphere: A Cinematic Discovery Prototype</p>
    <p><a href="#">Questions? Contact Us</a></p>
</div>
""", unsafe_allow_html=True)