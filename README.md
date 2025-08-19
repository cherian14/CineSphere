# 🎬 CineSphere

<p align="center">
  <h1 align="center" style="font-size: 5rem; font-weight: 900; border-bottom: none;">CineSphere.</h1>
  <h2 align="center" style="font-weight: 400; font-style: italic;">This is not a search bar. This is a dialogue with cinema.</h2>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.9+-blue.svg" alt="Python Version">
  <img src="https://img.shields.io/badge/Framework-Streamlit-FF4B4B.svg" alt="Streamlit">
  <img src="https://img.shields.io/badge/ML%20Library-Scikit--learn-F7931E.svg" alt="Scikit-learn">
  <img src="https://img.shields.io/badge/License-MIT-green.svg" alt="License: MIT">
  <img src="https://img.shields.io/badge/Status-Prototype-informational.svg" alt="Status: Prototype">
</p>

---

## 🌌 The Premise

We have all been there. Lost in the endless scroll. An ocean of options, a desert of choice.  
The paradox of our time: access to nearly every film ever made, yet never finding it harder to choose one.  

Streaming platforms present catalogues—grids of static posters, served by algorithms that know *what* we watched, but never *why*.  
They see patterns in data, but miss the soul in the machine.  

That era is over.  
CineSphere is a working prototype built on a single, radical belief:  
**choosing a film should be as intentional and rewarding as watching one.**

---

## 🖼️ The Experience

CineSphere transforms recommendation into **curation**. It is not an algorithm whispering patterns; it is a dialogue with your narrative impulse.  

The application unfolds on a seamless canvas, offering two distinct pathways:

### 🎥 I. The Archive (For the Connoisseur)
An instrument of precision.  
- **Cinematic DNA Analysis:** Select a film; our engine performs a vector analysis of its genre & thematic signatures.  
- **Reveal Artistic Siblings:** Discover films with the same artistic soul. Choose between a single perfect pairing or a ten-film festival.  

### 🎬 II. The Director's Chair (For the Adventurer)
An instrument of inspiration.  
- **The Emotional Core:** Begin with one simple question: *What is the emotional core of your desired story?*  
- **A Spectrum of Narrative:** Choose from ten cinematic moods—from *Dark & Unsettling* to *Epic & Grandiose*.  
- **Instant Curation:** Receive a curated set of films that honor your chosen emotional journey.  

---

## 🏛️ Architecture & Philosophy

Every technical decision serves a singular vision:  
to make a complex, data-driven application feel effortless, intuitive, and cinematic.  

### 🔧 Technology Stack
- **Python 3.9+** → the foundation.  
- **Streamlit** → transforms Python scripts into an interactive single-page app.  
- **Scikit-learn** → powers "The Archive" with `TfidfVectorizer` and `linear_kernel`.  
- **Pandas & NumPy** → data manipulation at scale.  
- **TMDB API** → world-class visuals for high-fidelity posters.  

### 🎨 Guiding Principles
- From **passive scrolling** to **active discovery**.  
- **Visual storytelling** as a design principle.  
- **Performance as a feature**, with intelligent caching for instantaneous results.  

---

# ⚡ Setup & Launch CineSphere

# Step 1 — Install dependencies
pip install streamlit pandas numpy scikit-learn requests

# Step 2 — Download MovieLens dataset
curl -O https://files.grouplens.org/datasets/movielens/ml-latest-small.zip
unzip ml-latest-small.zip
rm ml-latest-small.zip

# Step 3 — Run CineSphere
streamlit run app.py
