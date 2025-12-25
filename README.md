# 🗺️ Travel Destination Finder: ML-Powered Recommendation App

**Live Link:** [🚀 Access the Live Web Application](https://mlprojecttravelrecommendationsystem-qs8k5xn7wfjxsvyrmb8sk5.streamlit.app/)
*(Note: Replace the link above with your actual URL from Streamlit Cloud)*

## 📖 Project Overview
This project is a machine learning-based travel recommendation system. It uses a **Random Forest Regressor** to predict user satisfaction for various travel destinations. Unlike simple filters, this app learns from historical data to understand how factors like budget, season, and transport mode interact to influence a traveler's experience.

The app is built using a modular architecture, keeping data cleaning, model training, and the user interface separated for professional-grade stability.

---

## 🛠️ Technology Stack
* **Language:** Python 3.x
* **Framework:** [Streamlit](https://streamlit.io/) (Web UI)
* **Machine Learning:** [Scikit-learn](https://scikit-learn.org/) (Random Forest)
* **Data Analysis:** Pandas, NumPy
* **Hosting:** GitHub + Streamlit Community Cloud

---

## 📂 Repository Structure
I have modularized the code to ensure the app is "lean" and production-ready:

| File | Description |
| :--- | :--- |
| **`app.py`** | The frontend interface. Handles user inputs, sidebar settings, and displays results. |
| **`model.py`** | The core ML logic. Handles data loading, One-Hot Encoding, and the recommendation algorithm. |
| **`FeatureEng.py`** | The data cleaning engine. Contains my original logic for fixing logical errors and calculating `total_cost`. |
| **`requirements.txt`** | List of dependencies required to run the app in the cloud. |
| **`Original.csv`** | The raw dataset containing travel history and ratings. |

---

## ⚙️ Data Pipeline & Logic
To ensure the highest accuracy, the project follows a specific processing pipeline:

1.  **Cleaning Logic:** The system identifies and removes logical inconsistencies (e.g., ensuring landlocked cities like Agra or Shimla are not categorized as "Beach" destinations).
2.  **Feature Engineering:** A `total_cost` feature is derived by summing entry fees, accommodation, and food costs to give the model a better understanding of the financial requirement.
3.  **Encoding:** Categorical variables (Season, Day Type, etc.) are converted into numerical format using One-Hot Encoding.
4.  **Prediction:** The Random Forest model processes the user's current constraints against the dataset to rank the top 3 unique destinations.

---

## 🚀 How to Run Locally
If you wish to run this project on your local machine:

1.  **Clone the Repo:**
    ```bash
    git clone [https://github.com/your-username/your-repo-name.git](https://github.com/your-username/your-repo-name.git)
    cd your-repo-name
    ```
2.  **Install Requirements:**
    ```bash
    pip install -r requirements.txt
    ```
3.  **Launch the App:**
    ```bash
    streamlit run app.py
    ```

---

## 🎓 Academic Context
This project was developed to demonstrate the deployment of a Machine Learning model from a research environment (Jupyter/Colab) to a live, production-grade cloud environment. It highlights the use of **regression analysis**, **feature engineering**, and **modular software design**.
