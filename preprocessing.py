
import pandas as pd
import numpy as np
from joblib import load
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
MODEL_PATH = BASE_DIR / 'model_strategies' / 'model1_predicting_combined_sales' / 'preprocessor.pkl'

#Constants
product_map = {
    'VBurger': 'Veg Burger',
    'Veggie Burger': 'Veg Burger',
    'V. Burger': 'Veg Burger',
    'Veg Burger': 'Veg Burger',
    
    'Fries': 'Fries',    

    'F Burger': 'Falafel Burger',
    'Falafel Burger': 'Falafel Burger',
    
    'Chz Burger': 'Cheese Burger',
    'Cheese Burger': 'Cheese Burger',

    'Chicken Burger': 'Chicken Burger',
    'Chk Burger': 'Chicken Burger',
    'Chicken Brg': 'Chicken Burger',
    'Chicken Br': 'Chicken Burger',

    'Coca-Cola': 'Coca-Cola',
    'Coke': 'Coca-Cola',

    # Instructions — 'Custom Order'
    'X-CHeese': 'Custom',
    'NO TOMATOES': 'Custom',
    'No Tom Plz': 'Custom',
    'No Chz': 'Custom',
    'Absolute no cheese': 'Custom',
    'No Lettuce': 'Custom',
    'Fast Please': 'Custom',
    'Extra Cheese': 'Custom',
    'Carmalized Onions': 'Custom',
}

special_map={
    'Yes':1,
    'No':0,
    'Y':1,
    'N':0,
    'nO':0
}
# preprocessor=load('model_strategies/model1_predicting_combined_sales/preprocessor.pkl')
preprocessor=load(MODEL_PATH)

upper_limit_s3=34050.15

final_cols=['ProductName_Cheese Burger',
 'ProductName_Chicken Burger',
 'ProductName_Coca-Cola',
 'ProductName_Custom',
 'ProductName_Falafel Burger',
 'ProductName_Fries',
 'ProductName_Veg Burger',
 'Day_Friday',
 'Day_Monday',
 'Day_Saturday',
 'Day_Sunday',
 'Day_Thursday',
 'Day_Tuesday',
 'Day_Wednesday',
 'Day_Count',
 'specials',
 'Inflation_Percentage',
 'Unemployment_Percentage',
 'Amt',
 'Weekend']

def preprocess(data):
    data=pd.DataFrame(data, index=[0])
    data['Weekend'] = data['Day'].isin(['Friday','Saturday', 'Sunday']).astype(int)
    data['Amt']=-1
    data['Day_Count']=-1
    data=data[['Day_Count', 'ProductName',	'Day',	'specials',	'Inflation_Percentage',	'Unemployment_Percentage',	'Amt',	'Weekend']]
    data=preprocessor.transform(data)
    data=pd.DataFrame(data,columns=final_cols)
    data.drop(['Day_Count', 'Amt'], axis=1, inplace=True)
    return data
    