import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import warnings
import os

warnings.filterwarnings('ignore')

def load_and_train_model(csv_path):
    if not os.path.exists(csv_path):
        # Trigger cleaning if file is missing
        import FeatureEng
        df = FeatureEng.run_cleaning()
    else:
        df = pd.read_csv(csv_path)

    target_variable = 'satisfaction_rating'
    features_df = df.drop(target_variable, axis=1)
    feature_columns = features_df.columns
    
    X_encoded = pd.get_dummies(features_df, drop_first=True, dtype=int)
    y = df[target_variable]
    trained_columns = X_encoded.columns

    rf_model = RandomForestRegressor(n_estimators=100, random_state=42, n_jobs=-1)
    rf_model.fit(X_encoded, y)
    
    return rf_model, df, trained_columns, feature_columns

def get_recommendations(user_inputs, model, original_df, trained_cols, base_feature_cols):
    user_start = user_inputs['start_location']
    candidate_trips = original_df[original_df['start_location'] == user_start].copy()
    
    if candidate_trips.empty:
        return pd.DataFrame()
        
    test_df = candidate_trips.copy()
    broadcast_inputs = user_inputs.copy()
    broadcast_inputs.pop('start_location')
    
    for key, value in broadcast_inputs.items():
        if key in test_df.columns:
            test_df[key] = value
            
    test_df_ordered = test_df[base_feature_cols]
    encoded_test_df = pd.get_dummies(test_df_ordered, drop_first=True, dtype=int)
    final_test_df = encoded_test_df.reindex(columns=trained_cols, fill_value=0)
    
    predictions = model.predict(final_test_df)
    results_df = test_df_ordered.copy()
    results_df['predicted_satisfaction'] = predictions
    
    display_cols = ['end_location', 'destination_type', 'transport_mode', 'total_cost', 'popularity_score', 'estimated_travel_time_hr', 'predicted_satisfaction']
    final_display_cols = [col for col in display_cols if col in results_df.columns]
    final_results = results_df[final_display_cols]
    
    final_results = final_results.sort_values(by='predicted_satisfaction', ascending=False)
    return final_results.drop_duplicates(subset=['end_location', 'destination_type'], keep='first').head(3)
