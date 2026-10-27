## Import Path to create reliable folder and file paths
from pathlib import Path

## Import pandas for reading, checking, cleaning, and saving the dataset
import pandas as pd


## Locate the main project folder
## __file__ refers to this Python file
## parent.parent moves from python_code back to SWA2124_Final_Project
project_folder = Path(__file__).resolve().parent.parent

## Create the path to the original dataset
file_path = project_folder / "dataset" / "online_shoppers_intention.csv"


## Load the CSV dataset into a pandas DataFrame
df = pd.read_csv(file_path)

## Confirm that the dataset was loaded successfully
print("Dataset loaded successfully")

## Display the original number of rows and columns
print("Dataset shape:", df.shape)


## Display the first 5 rows to preview the dataset
print("\nFirst 5 rows:")
print(df.head())


## Display all column names
print("\nColumn names:")
print(df.columns.tolist())


## Check whether there are any missing values in each column
print("\nMissing values:")
print(df.isnull().sum())


## Count the number of duplicated rows
print("\nNumber of duplicate rows:")
print(df.duplicated().sum())


## Remove duplicated rows from the dataset
df = df.drop_duplicates()


## Display the new dataset size after removing duplicates
print("\nDataset shape after removing duplicates:")
print(df.shape)


## Create the path for the cleaned dataset
cleaned_file_path = (
    project_folder
    / "dataset"
    / "online_shoppers_intention_cleaned.csv"
)


## Save the cleaned dataset without including the row index
df.to_csv(cleaned_file_path, index=False)

## Confirm that the cleaned dataset was saved successfully
print("\nCleaned dataset saved successfully.")