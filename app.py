import streamlit as st
import pandas as pd
from model import load_and_train_model, get_recommendations

st.set_page_config(page_title="Travel Destination Finder", page_icon="🗺️", layout="wide")

# Path for the cloud environment
FILE_PATH = 'Engineered_Features.csv'

@st.cache_resource
def load_data():
    return load_and_train_model(FILE_PATH)

st.title("🗺️ Travel Destination Finder")
st.markdown("Enter your preferences below to find your ideal trip.")

try:
    rf_model, df, trained_columns, feature_columns = load_data()
    
    col1, col2 = st.columns(2)
    with col1:
        start_location = st.selectbox('Where are you starting from?', sorted(df['start_location'].unique()))
        season = st.selectbox('What season?', sorted(df['season'].unique()))
        user_budget = st.number_input('Max budget (₹)?', 1000, 50000, 5000)
        
    with col2:
        day_type = st.selectbox('Weekday or Weekend?', sorted(df['day_type'].unique()))
        transport = st.selectbox('Preferred transport?', sorted(df['preferred_transport_mode'].unique()))
        time_h = st.slider('Hours onsite?', 1.0, 24.0, 12.0)
        
    pop_score = st.slider('Crowdedness level?', 0.0, 1.0, 0.7)

    if st.button('Find My Destination ✈️', use_container_width=True):
        inputs = {
            'start_location': start_location, 'season': season, 'day_type': day_type,
            'user_budget': user_budget, 'user_time_constraint_hr': time_h,
            'preferred_transport_mode': transport, 'popularity_score': pop_score
        }
        
        results = get_recommendations(inputs, rf_model, df, trained_columns, feature_columns)

        if results.empty:
            st.warning("No destinations found.")
        else:
            st.subheader("Your Recommendations")
            res_df = results.copy()
            res_df['total_cost'] = res_df['total_cost'].map(lambda x: f"₹{x:,.0f}")
            res_df['predicted_satisfaction'] = res_df['predicted_satisfaction'].map(lambda x: f"{x:.2f} / 5.0")
            st.dataframe(res_df, hide_index=True, use_container_width=True)

except Exception as e:
    st.error(f"Error: {e}")
