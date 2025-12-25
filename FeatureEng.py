import pandas as pd

def run_cleaning():
    df = pd.read_csv('Original.csv')

    # 1. Data Cleaning: Remove rows with logical errors
    error_mask = (df['end_location'].isin(['Agra', 'Shimla'])) & (df['destination_type'] == 'Beach')
    df_clean = df[~error_mask].copy()

    # 2. Feature Engineering: Create 'total_cost'
    df_clean['total_cost'] = (
        df_clean['entry_fee'] + 
        df_clean['accommodation_cost'] + 
        df_clean['food_cost']
    )

    # 3. Feature Selection: Drop unused columns
    cols_to_drop = [
        'route_id', 'total_distance_km', 'traffic_density', 
        'entry_fee', 'accommodation_cost', 'food_cost', 'preferred_destination'
    ]
    df_final = df_clean.drop(columns=cols_to_drop)

    # Reorder columns
    final_column_order = [
        'start_location', 'end_location', 'estimated_travel_time_hr', 'season', 
        'day_type', 'transport_mode', 'destination_type', 'popularity_score', 
        'total_cost', 'user_budget', 'user_time_constraint_hr', 
        'preferred_transport_mode', 'satisfaction_rating'
    ]
    df_final = df_final[final_column_order]

    # Save the engineered dataset
    df_final.to_csv('Engineered_Features.csv', index=False)
    return df_final

if __name__ == "__main__":
    run_cleaning()
