



<br>

<p align="center">
<h1 align="center" style="font-size: 5rem; font-weight: 900; border-bottom: none;">CineSphere.</h1>
<h2 align="center" style="font-weight: 400; font-style: italic;">This is not a search bar. This is a dialogue with cinema.</h2>
</p>

<br>
<p align="center">
<a href="#"><img src="https://img.shields.io/badge/Python-3.9+-blue.svg" alt="Python Version"></a>
<a href="#"><img src="https://img.shields.io/badge/Framework-Streamlit-red.svg" alt="Framework"></a>
<a href="#"><img src="https://img.shields.io/badge/License-MIT-green.svg" alt="License"></a>
<a href="#"><img src="https://img.shields.io/badge/Status-Prototype-orange.svg" alt="Status"></a>
</p>

<p align="center">
<img src="https://i.imgur.com/your_link_to_a_stunning_screenshot_or_gif.gif" alt="CineSphere Live Demo" width="850"/>
</p>

> We have all been there. Lost in the endless scroll. An ocean of options, a desert of choice. The paradox of our time is that we have access to nearly every film ever made, yet have never found it harder to choose one.

**CineSphere** is a working prototype built on a single, radical belief: choosing a film should be as intentional and rewarding as watching one. It is an interactive experience designed to understand your narrative impulse, transforming passive selection into an active journey of discovery.

---

## 🚀 Launch Sequence: T-Minus 3 Steps to Discovery

This experience is designed for a flawless local deployment. Follow these three steps precisely.

### STEP 1: ASSEMBLE THE ENVIRONMENT
First, clone the repository to your local machine and install the core Python dependencies with a single command.

```bash
# Click the copy icon in the top right of this block to copy all commands at once.

# 1. Clone the repository and navigate into it
git clone https://github.com/your-username/CineSphere.git
cd CineSphere

# 2. Install all required packages
pip install streamlit pandas numpy scikit-learn requests
```

### STEP 2: ACQUIRE THE CORE DATASET
The engine is powered by the MovieLens dataset. A one-time manual download is required.

1.  **Download:** Get the dataset from the official source:
    *   **Direct Link:** [**ml-latest-small.zip**](https://files.grouplens.org/datasets/movielens/ml-latest-small.zip)

2.  **Unzip & Place:**
    *   Unzip the downloaded file. This will create a folder named `ml-latest-small`.
    *   Move this entire **`ml-latest-small`** folder into the root of the **`CineSphere`** directory you just cloned.
    *   **CRITICAL:** Your folder structure must have `app.py` and the `ml-latest-small/` folder side-by-side.

### STEP 3: ACTION!
With the environment and dataset in place, launch the application.

```bash
# 3. Run the Streamlit application
streamlit run app.py
```
Your default browser will open, and the cinematic journey will begin.

---

## 🎨 The Canvases: A Dual-Methodology Approach

The entire experience unfolds on a single, seamless canvas, presenting two distinct pathways for discovery.

#### I. The Archive: An Instrument of Precision.
For the enthusiast who arrives with a masterpiece in mind. Select any film, and our engine performs an instantaneous vector analysis of its generic and thematic signatures, revealing its artistic siblings.

#### II. The Director's Chair: An Instrument of Inspiration.
For the viewer in search of a *feeling*. Your choice from an expanded palette of ten cinematic moods becomes the guiding principle for our curation engine, crafting a personalized film festival that honors your narrative impulse.

---

## 🏛️ The Blueprint: An Architecture of Experience

Every technical decision was made in service of a single goal: to make a complex, data-driven application feel effortless, intuitive, and beautiful.

| Component      | Technology       | Role & Purpose                                                                                                   |
| :------------- | :--------------- | :--------------------------------------------------------------------------------------------------------------- |
| **🖥️ The Stage**    | `Streamlit`      | Leveraged to render a dynamic, single-page application from a pure Python script for a seamless user experience. |
| **🧠 The Intellect** | `Scikit-learn`   | The heart of our "Archive." `TfidfVectorizer` and `linear_kernel` are our instruments for mapping cinematic connections. |
| **🎨 The Visuals** | `TMDB API`       | Integrates directly with The Movie Database to ensure every recommendation is presented with its stunning poster art. |
| **💾 The Library** | `Pandas` & `Numpy`| The backbone for efficient data manipulation and numerical operations on the MovieLens dataset.                 |

---

## The Architect

**[Your Name]**

*   **LinkedIn:** [Your LinkedIn URL]
*   **GitHub:** [Your GitHub Profile URL]
*   **Portfolio:** [Your Portfolio Website URL]
