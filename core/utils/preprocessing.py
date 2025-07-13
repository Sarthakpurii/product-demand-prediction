import pandas as pd
from joblib import load


preprocessor=load('model_strategies/model1_predicting_combined_sales/preprocessor.pkl')

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
    