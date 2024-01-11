from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

# Load the model (make sure to provide the correct path)
model = joblib.load('model/rf_afcon_prediction_model.joblib')

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = ""
    if request.method == 'POST':
        # Retrieve form data
        # home_team = request.form['home_team']
        # away_team = request.form['away_team']
        # stage = request.form['stage']
        
        # # Encode the inputs using your encoding functions
        # home_team_encoded = encode_team(home_team)
        # away_team_encoded = encode_team(away_team)
        # stage_encoded = encode_stage(stage)
        
        # # Make prediction
        # prediction = model.predict([[home_team_encoded, away_team_encoded, stage_encoded]])[0]
        
        # # Convert prediction to string
        # prediction = "Home Team Wins" if prediction == 1 else "Away Team Wins" if prediction == -1 else "Draw"

        home_team = request.form['home_team']
        away_team = request.form['away_team']
        stage = request.form['stage']
        
        # Encode the inputs using your encoding functions
        home_team_encoded = encode_team(home_team)
        away_team_encoded = encode_team(away_team)
        stage_encoded = encode_stage(stage)

        # Ensure that all inputs are valid (not NaN or infinity)
        if np.isnan(home_team_encoded) or np.isnan(away_team_encoded) or np.isnan(stage_encoded):
            # Handle the invalid input case here
            return "Invalid input. Please check the entered values."
        
        # Making a prediction only if all inputs are valid
        prediction = model.predict([[home_team_encoded, away_team_encoded, stage_encoded]])[0]
        # Convert prediction to string and return it
        return prediction


    return render_template('index.html', prediction=prediction)

def encode_team(team_name):
    # Implement the encoding for team names
    pass

def encode_stage(stage_name):
    # Implement the encoding for stage
    pass


# Function to predict match outcome
def predict_outcome():
    # Retrieve form data
    home_team = request.form['home_team']
    away_team = request.form['away_team']
    stage = request.form['stage']
    
    # Encode the inputs using your encoding functions
    home_team_encoded = encode_team(home_team)
    away_team_encoded = encode_team(away_team)
    stage_encoded = encode_stage(stage)

    # Ensure that all inputs are valid (not NaN or infinity)
    if np.isnan(home_team_encoded) or np.isnan(away_team_encoded) or np.isnan(stage_encoded):
        # Handle the invalid input case here
        return "Invalid input. Please check the entered values."
    
    # Making a prediction only if all inputs are valid
    prediction = model.predict([[home_team_encoded, away_team_encoded, stage_encoded]])[0]
    # Convert prediction to string and return it
    return prediction

if __name__ == '__main__':
    app.run(debug=True)
