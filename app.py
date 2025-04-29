# This is where I imported everything I needed for the project. I did it at the beginning so that it would not get confusing later
import streamlit as st
import pandas as pd
import numpy as np
import joblib

# This is what loads the model that I brought over from the Colab Notebook and reads the CSV file that contains the testing data
model = joblib.load("model.pkl")
test_data = pd.read_csv("MLB_test.csv")

# This is where I create 2 new features Payroll per win and log salary (as in logarithm)
test_data["Payroll_per_Win"] = test_data["Total_Payroll"] / test_data["Wins"]
test_data["Log_Salary"] = np.log(test_data["Total_Payroll"])

# This is the initial setup for the Streamlit App
st.title("MLB Win Predictor (2019–2024)")

team_selected = st.selectbox("Select a Team:", sorted(test_data["Team"].unique()))
year_selected = st.selectbox("Select a Year:", sorted(test_data["Year"].unique()))

# This is where the app predicts the wins based off of the team and year that the user selects
if st.button("Predict"):
    row = test_data[(test_data["Team"] == team_selected) & (test_data["Year"] == year_selected)]

    if row.empty:
        st.warning("No data found for that team and year.")
    else:
        total_payroll = row.iloc[0]["Total_Payroll"]
        payroll_per_win = row.iloc[0]["Payroll_per_Win"]
        log_salary = row.iloc[0]["Log_Salary"]
        actual_wins = row.iloc[0]["Wins"]

        X_input = pd.DataFrame([{
            "Total_Payroll": total_payroll,
            "Payroll_per_Win": payroll_per_win,
            "Log_Salary": log_salary
        }])

        predicted_wins = model.predict(X_input)[0]
	# This is what is output when the predict button is selected
        st.markdown(f"**Team Payroll**: ${total_payroll:,.0f}")
        st.success(f"**Predicted Win Total**: {predicted_wins:.1f}")
        st.info(f"**Actual Win Total**: {actual_wins}")