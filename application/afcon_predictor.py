from flask import Flask, render_template, request, redirect, url_for, flash
import joblib
import numpy as np
import pandas as pd
from datetime import datetime
from collections import OrderedDict
from flask_mail import Mail, Message


app = Flask(__name__)

# Flask-Mail configuration
app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 465
app.config["MAIL_USE_SSL"] = True
app.config["MAIL_USERNAME"] = 'amadasunese@gmail.com'
app.config["MAIL_PASSWORD"] = 'qxxo axga dzia jjsw'
mail = Mail(app)

# Secret key for message flashing
app.secret_key = 'your_secret_key'


# Load the model (make sure to provide the correct path)
rf_model = joblib.load('model/rf_afcon_prediction_model.joblib')


# Function to encode team names and stage
def encode_team(team_name, team_encoding):
    return team_encoding.get(team_name, np.nan)

def encode_stage(stage_name, stage_encoding):
    return stage_encoding.get(stage_name, np.nan)


@app.route('/', methods=['GET', 'POST'])
def index():
    # Load your historical match data
    matches_df = pd.read_csv('data/Matches_ed.csv')

    # Other code to read team names from Excel
    teams_df = pd.read_excel('data/Matches23_with_Winners.xls')
    # team_names = teams_df['Teams'].tolist()
    team_names = list(OrderedDict.fromkeys(teams_df['HomeTeam'].tolist()))

    prediction = None
    stats_message = None

    if request.method == 'POST':
        home_team = request.form['home_team']
        away_team = request.form['away_team']
        stage = request.form['stage']



        # Encoding and prediction logic
        # Define your encoding dictionaries
        team_encoding = {team: idx for idx, team in enumerate(team_names)}
        stage_encoding = {'Final': 0, 'Group stage': 1, 'Quarter-finals': 2, 'Round of 16': 3, 'Semi-finals': 4, 'third place': 5}

        # Encode the inputs
        home_team_encoded = encode_team(home_team, team_encoding)
        away_team_encoded = encode_team(away_team, team_encoding)
        stage_encoded = encode_stage(stage, stage_encoding)

        # Check if encoded values are numeric and not NaN
        inputs_are_numeric = all(isinstance(value, (int, float)) and not np.isnan(value) 
                                 for value in [home_team_encoded, away_team_encoded, stage_encoded])


        if inputs_are_numeric:
            # Making a prediction
            prediction_result = rf_model.predict([[home_team_encoded, away_team_encoded, stage_encoded]])[0]


            # Format the prediction text to include the team names
            if prediction_result == 1:
                prediction_text = f"{home_team} Wins"
            elif prediction_result == -1:
                prediction_text = f"{away_team} Wins"
            else:
                prediction_text = "Draw"


            # Calculate head-to-head statistics
            stats_message = calculate_head_to_head_stats(home_team, away_team, matches_df)

            # Combine prediction with stats message
            prediction = f"{prediction_text}, {stats_message}"
        else:
            prediction = "Invalid input. Please check the entered values."

    return render_template('index.html', team_names=team_names, prediction=prediction)


def calculate_head_to_head_stats(home_team, away_team, matches_df):
    # Filter the DataFrame for matches where either team was playing
    head_to_head_matches = matches_df[((matches_df['HomeTeam'] == home_team) & (matches_df['AwayTeam'] == away_team)) |
                                      ((matches_df['HomeTeam'] == away_team) & (matches_df['AwayTeam'] == home_team))]

    # Calculate statistics
    total_matches = len(head_to_head_matches)
    home_wins = len(head_to_head_matches[(head_to_head_matches['HomeTeam'] == home_team) & (head_to_head_matches['Winner'] == 'Home')])
    away_wins = len(head_to_head_matches[(head_to_head_matches['AwayTeam'] == away_team) & (head_to_head_matches['Winner'] == 'Away')])
    draws = len(head_to_head_matches[head_to_head_matches['Winner'] == 'Draw'])

    # Format the statistics message
    stats_message = f"Head-to-Head: Played {total_matches}, {home_team} Wins {home_wins}, {away_team} Wins {away_wins}, Draws {draws}"

    return stats_message


@app.route('/feedback', methods=['GET', 'POST'])
def feedback():
    if request.method == 'POST':
        # Process the submitted data
        name = request.form.get('name')
        email = request.form.get('email')
        feedback_content = request.form.get('feedback')

        # Send an email with the feedback
        msg = Message("Feedback Received", 
                      sender=app.config["MAIL_USERNAME"], 
                      recipients=["amadasunese@gmail.com"]) # Replace with your email
        msg.body = f"Name: {name}\nEmail: {email}\nFeedback: {feedback_content}"
        mail.send(msg)

        # Flash a message and redirect to the feedback page
        flash('Thank you for your feedback, ' + name + '!')
        return redirect(url_for('feedback'))

    return render_template('feedback.html')



if __name__ == '__main__':
    app.run(debug=True)
