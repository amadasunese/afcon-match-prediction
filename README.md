AFCON Match Outcome Predictor

This application predicts the outcome of Africa Cup of Nations (AFCON) matches using a machine learning model. It's built with a Python backend and a Tkinter GUI for easy interaction.

Features

Predict match outcomes (win, lose, draw) based on teams and match stage.
Simple and user-friendly interface.
Prerequisites

To run this application, you need:

Python 3.x
Tkinter (usually comes pre-installed with Python)
joblib
Installation

Clone or download this repository to your local machine.
Ensure Python 3.x is installed.
Navigate to the application's directory.
Usage

Run the application script:
Copy code
python afcon_predictor.py
Enter the details of the match (home team, away team, and stage) in the respective fields.
Click the 'Predict Outcome' button to see the prediction.
Model Information

The application uses a pre-trained Random Forest Classifier model. The model is trained on historical AFCON match data and predicts one of three outcomes: Home Team Wins, Away Team Wins, or Draw.

Customization

The model can be retrained and updated as needed.
The GUI can be modified for additional features or aesthetic changes.
License

This project is open-source and available under the MIT License.

Acknowledgements

This project was built using data from the Africa Cup of Nations and is intended for educational purposes.