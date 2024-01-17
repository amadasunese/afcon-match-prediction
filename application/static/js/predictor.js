document.addEventListener("DOMContentLoaded", function() {
    const form = document.querySelector("form");
    form.addEventListener("submit", function(event) {
        const homeTeam = document.getElementById("home_team").value;
        const awayTeam = document.getElementById("away_team").value;
        const predictionResult = document.querySelector(".prediction-result");

        // Check if home and away teams are the same
        if (homeTeam === awayTeam) {
            alert("Home and away teams cannot be the same.");
            event.preventDefault(); // Prevent form submission
            return; // Stop further execution
        }

        // Display a loading message
        if(predictionResult) {
            predictionResult.innerHTML = "Loading prediction...";
        }
    });
});
