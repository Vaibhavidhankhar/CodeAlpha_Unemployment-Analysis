from flask import Flask, render_template, request, jsonify
import os
import pandas as pd

app = Flask(__name__)

# Load cleaned data with properly parsed and coerced dates & numeric columns (from your notebook output)
base_dir = os.path.dirname(os.path.abspath(__file__))
pickle_path = os.path.join(base_dir, "unemployment_data.pkl")
df = pd.read_pickle(pickle_path)

# Extract unique states and zones for dropdowns (ensure uniqueness)
states = sorted(df['Region'].dropna().unique())
zones = sorted(df['Zone_x'].dropna().unique())

@app.route('/')
def index():
    return render_template('index.html', states=states, zones=zones)

@app.route('/filter', methods=['POST'])
def filter_data():
    selected_states = request.json.get('states', [])
    selected_zones  = request.json.get('zones', [])

    # Start with all data
    filtered_df = df.copy()

    # Apply filters if any
    if selected_states:
        filtered_df = filtered_df[filtered_df['Region'].isin(selected_states)]
    if selected_zones:
        filtered_df = filtered_df[filtered_df['Zone_x'].isin(selected_zones)]

    # Drop rows with missing critical values to avoid NaN in plotting
    filtered_df = filtered_df.dropna(
        subset=['Date_x', 'Date_y', 
                'Estimated Unemployment Rate (%)_x', 'Estimated Unemployment Rate (%)_y',
                'Estimated Labour Participation Rate (%)_x', 'Estimated Labour Participation Rate (%)_y',
                'Estimated Employed_x', 'Estimated Employed_y']
    )

    # Prepare JSON response, format dates as ISO strings for JS parsing
    result = []
    for _, row in filtered_df.iterrows():
        result.append({
            "__state": row['Region'],
            "__zone": row['Zone_x'],
            "__dateX": row['Date_x'].strftime('%Y-%m-%d') if pd.notnull(row['Date_x']) else None,
            "__dateY": row['Date_y'].strftime('%Y-%m-%d') if pd.notnull(row['Date_y']) else None,
            "__unemX": float(row['Estimated Unemployment Rate (%)_x']),
            "__unemY": float(row['Estimated Unemployment Rate (%)_y']),
            "__lprX": float(row['Estimated Labour Participation Rate (%)_x']),
            "__lprY": float(row['Estimated Labour Participation Rate (%)_y']),
            "__empX": float(row['Estimated Employed_x']),
            "__empY": float(row['Estimated Employed_y']),
            "__monthX": int(row['Month_x']),
            "__monthY": int(row['Month_y']),
            "__monthNameX": row['MonthName_x'],
            "__monthNameY": row['MonthName_y']
        })

    return jsonify(result)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
