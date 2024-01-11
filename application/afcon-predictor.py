import tkinter as tk
from tkinter import ttk
import joblib

# Load the model
model = joblib.load('model/rf_afcon_prediction_model.joblib')

# Function to predict match outcome
def predict_outcome():
    # Implement your encoding functions here
    home_team_encoded = encode_team(home_team_entry.get())
    away_team_encoded = encode_team(away_team_entry.get())
    stage_encoded = encode_stage(stage_entry.get())

    # Making a prediction
    prediction = model.predict([[home_team_encoded, away_team_encoded, stage_encoded]])[0]

    # Display the prediction
    if prediction == 1:
        result_label.config(text="Home Team Wins")
    elif prediction == -1:
        result_label.config(text="Away Team Wins")
    else:
        result_label.config(text="Draw")

def encode_team(team_name):
    # Implement team encoding
    pass

def encode_stage(stage_name):
    # Implement stage encoding
    pass

# Creating main window, matching the mockup
root = tk.Tk()
root.title("AFCON Match Outcome Predictor")

# Styling (optional, for better aesthetics)
style = ttk.Style()
style.configure('TButton', font=('Arial', 10))
style.configure('TLabel', font=('Arial', 10), padding=10)

# Creating input fields and labels, aligned with the mockup
tk.Label(root, text="Home Team:").grid(row=0, column=0, sticky='e')
home_team_entry = ttk.Entry(root)
home_team_entry.grid(row=0, column=1, sticky='we')

tk.Label(root, text="Away Team:").grid(row=1, column=0, sticky='e')
away_team_entry = ttk.Entry(root)
away_team_entry.grid(row=1, column=1, sticky='we')

tk.Label(root, text="Stage:").grid(row=2, column=0, sticky='e')
stage_entry = ttk.Entry(root)
stage_entry.grid(row=2, column=1, sticky='we')

# Predict button, as shown in the mockup
predict_button = ttk.Button(root, text="Predict Outcome", command=predict_outcome)
predict_button.grid(row=3, column=0, columnspan=2)

# Label to display the result, similar to the mockup
result_label = tk.Label(root, text="", font=('Arial', 12))
result_label.grid(row=4, column=0, columnspan=2)

# Adjusting column weights for proper scaling
root.grid_columnconfigure(1, weight=1)

# Run the application
root.mainloop()
