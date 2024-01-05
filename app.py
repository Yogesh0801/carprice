import streamlit as st
import pandas as pd
import numpy as np
import pickle
import joblib
from xgboost import XGBRegressor

Fuel_Type  = {'Petrol':0,'Diesel':1, 'CNG':2,}

Seller_Type  = {'Dealer':0, 'Individual':1,}

Transmission  = {'Manual':0, 'Automatic':1,}



# Loading the Model pickle file
#model =  pickle.load(open('xg_model.pkl','rb'))
model = joblib.load(open('xg_model1.pkl','rb'))

# Creating the function funtion to accept inputs and creating an 2d array and predicting the result.

def predict(Present_Price,Kms_Driven,Fuel_Types
                       ,Seller_Types,Transmissions,Owner,Age):
    """Function To accept the values"""
    fuel_type = Fuel_Type[Fuel_Types]
    seller_type = Seller_Type[Seller_Types]
    transmission = Transmission[Transmissions]
    data_new = pd.DataFrame({
        'Present_Price':Present_Price,
        'Kms_Driven':Kms_Driven,
        'Fuel_Type':fuel_type,
        'Owner':Owner,
        'Age':Age,
        'Seller_Type':seller_type,
        'Transmission':transmission
        
    },index=[0])
    print(data_new)
    
    result = model.predict(data_new)[0].round(2)
    
    return result.round(2)



if __name__=="__main__":
    st.header("Car Price Prediction")
    col1,col2 = st.columns([2,1])
    Present_Price = col1.slider("Present_Price",max_value=3000000,min_value=800000)
    Kms_Driven = col1.slider("Kms_Driven",max_value=50000,min_value=1000)
    fuel_type = col1.selectbox("Fuel_type:",list(Fuel_Type.keys()))
    seller_type = col2.selectbox("Seller_type:",list(Seller_Type.keys()))
    transmission = col2.selectbox("Transmission:",list(Transmission.keys()))
    Owner = col2.selectbox("Owner:",list(range(0,3)))#list(Owner.keys()))
    Age = col1.selectbox("Select Age:",list(range(1,15)))
    result = predict(Present_Price,Kms_Driven,fuel_type,seller_type,transmission,Owner,Age).round(2)
    print(result)
    submit_button = st.button("Predict")
    if submit_button:
        larger_text = f"<h2 style='color: white;'>The Predicted Price is : {result} Lakhs</h2>"
        st.markdown(larger_text,unsafe_allow_html=True)




