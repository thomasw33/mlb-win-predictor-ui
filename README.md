MLB Win Prediction AI Project
Thomas Woodcum 
CSC 4444

This project uses multiple regression models and an interactive UI to predict MLB team wins based on payroll. There are two sections of this project:

1. A Google Colab Notebook used for training, testing, and analysis.
2. A Streamlit web UI that utilizes the Random Forest model to make preictions based on 2019-2024 using team and payroll.

**Files Included**
- mlb_win_predictor_notebook.ipynb: This is the Google Colab Notebook used for training, testing, and analyzing the models. It also includes visuals for the models.
- MLB_train.csv: The training dataset, covering MLB wins and payroll from 2000 to 2018.
- MLB_test.csv: The testing dataset, covering MLB wins and payroll from 2019 to 2024.
- app.py: The Streamlit UI application that allows the Random Forest Model to be tested and visualized.
- model.pkl: The trained Random Forest model that is used by the Streamlit app.
- requirements.txt: A text file that downloads the necessary Python packages for running the Streamlit app locally.

**Colab Instructions**
- First, I will show you how to run the model in Google Colab to see the results of the models.

- Open the Google Colab Notebook. The link to the notebook is here:
https://colab.research.google.com/drive/1Pi1dw18O0oOKP0nPSFDS9Tft10M1ThdE?usp=sharing

- Upload CSV Files:
  
Once the notebook has been loaded, upload the training and testing files using the upload button on the left bar or "files.upload()" in the code:

MLB_train.csv
MLB_test.csv

- Run the Notebook
Run the notebook (It should all be in one cell). Once it runs you should have:
- Four trained models (Linear Regression, Ridge, Lasso, Random Forest)
- Evaluated model performance
- Generated and saved residual and prediction plots
- Comparable modles using R², MAE, RMSE, and MBE
- Identified over/underperforming teams

- Download/View Graphs (optional)

If you would like to view the graphs as PNG files they will be saved and downloadable.

**Streamlit UI Instructions**

- Open the Streamlit App. The link is here:

https://mlb-win-predictor-ui-thomas-w-csc-4444.streamlit.app/

- Interact with the Interface
  
This App utilizes the trained Random Forest model to:

- Allow users to select a team and year (2019 - 2024)
- Select the Predict button to reveal the predicted number of wins for that year along with the salary
- Compare to the number of games the team actually won in a given year

- Run Streamlit App Locally:
  
Here are the steps to install any necessary libraries and run the app locally on your device

- Step 1: Open your terminal and run the following:
  
git clone https://github.com/thomasw33/mlb-win-predictor-ui.git
- And then navigate to the folder
cd mlb-win-predictor-ui

- Step 2: Install the necessary packages:
  
pip install streamlit pandas scikit-learn

- Step 3: Run the Streamlit App:
  
streamlit run app.py

- Step 3.5: Troubleshooting Streamlit:
  
If you get an error when running the app, run this line:

$env:Path += ";$HOME\AppData\Roaming\Python\Python311\Scripts"
(replacing Python311 with whatever version of Python you have installed)

-Step 4: Run the Streamlit App again (If necessary):

streamlit run app.py




