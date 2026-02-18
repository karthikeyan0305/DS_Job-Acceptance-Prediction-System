from src.load_data import load_data
from src.data_clean import data_clean
from src.eda import perform_data
from src.feature_engineering import feature_engineering
from src.model_evaluation import evaluate_model
from src.model_training import train_model

df = load_data()

df = data_clean(df)

df = feature_engineering(df)

df.to_csv("Data/HR_Job_Placement_Dataset_cleaned.csv", index=False)

perform_data(df)

model, X_test, y_test = train_model(df)

evaluate_model(model,X_test,y_test)
