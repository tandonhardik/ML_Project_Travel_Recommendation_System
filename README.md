# 🗺️ Journey Genie: Personalized Destination Discovery

**Live Demo:** [🚀 View the Live Application](https://mlprojecttravelrecommendationsystem-qs8k5xn7wfjxsvyrmb8sk5.streamlit.app/)

## 📖 Project Overview
**Journey Genie** is a predictive recommendation system designed to eliminate "analysis paralysis" for travelers. Unlike traditional search engines that rely on rigid filters, this system acts as a "personal concierge" by predicting a **Satisfaction Rating** (on a 1-5 scale) for potential destinations based on unique user constraints like budget, season, and travel time.



---

## ✨ Key Features
* **Satisfaction-Based Ranking:** Ranks destinations based on predicted user satisfaction rather than just availability.
* **Constraint Synthesis:** Processes complex inputs including Budget, Season, Day Type, and Time constraints in real-time.
* **Cold Start Resolution:** Assists users who lack a specific destination in mind by generating personalized candidate trips instantly.
* **Data Integrity Logic:** Built-in cleaning ensures the system never recommends impossible scenarios (e.g., landlocked "Beach" destinations).

---

## 🛠️ Technology Stack
* **Machine Learning:** [Scikit-learn](https://scikit-learn.org/) (Random Forest Regressor)
* **Web Framework:** [Streamlit](https://streamlit.io/) (Interactive UI)
* **Data Analysis:** Pandas & NumPy
* **Visualization:** Matplotlib & Seaborn

---

## 📂 Project Structure
To ensure production-grade stability, the project is divided into specialized modules:

| File | Description |
| :--- | :--- |
| **`app.py`** | The Streamlit-based interactive frontend. |
| **`model.py`** | Core engine handling Random Forest training and the "Generate-Score-Rank" workflow. |
| **`FeatureEng.py`** | Implementation of data cleaning and cost aggregation logic. |
| **`Original.csv`** | Raw "SmartTourRoutePlanner" dataset. |
| **`requirements.txt`** | Dependency list for cloud deployment. |

---

## ⚙️ Methodology & Pipeline
The system utilizes a **Random Forest Regressor** (100 decision trees) to capture non-linear relationships in travel satisfaction data.



### 1. Data Pre-processing
* **Cost Aggregation:** Created a `total_cost` feature by summing entry fees, accommodation, and food costs.
* **Logical Cleaning:** Removed geographically impossible records (e.g., landlocked "Beach" destinations).
* **Bias Mitigation:** Dropped features like `preferred_destination` to ensure the model learns from fundamental attributes.

### 2. Prediction & Ranking Workflow
1.  **Candidate Generation:** Retrieves a catalog of all unique, valid destinations from the dataset.
2.  **Hypothetical Construction:** Builds a "trip" for every destination using current user constraints.
3.  **Scoring:** The Random Forest engine predicts a satisfaction rating for every candidate trip.
4.  **Ranking:** Outputs the top 3 results sorted by the highest predicted satisfaction.

---

## 🚀 Future Work
* **Live API Integration:** Connecting to real-time flight and hotel booking APIs for dynamic pricing.
* **Deep Learning:** Implementing Neural Networks to capture even more complex feature interactions.
* **Hybrid Filtering:** Combining satisfaction ranking with user-user collaborative filtering.

---

## 🎓 Academic Context
Developed for the **Machine Learning (UML501)** course at the **Department of Computer Science and Engineering, Thapar Institute of Engineering and Technology**.

**Group Details (Sub-Group: 3Q11):**
* Devansh Chhabra (102317041)
* Neeraj (102317014)
* **Submitted to:** Ms. Manisha Malik
