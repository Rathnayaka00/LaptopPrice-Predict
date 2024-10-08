import streamlit as st
import pickle
import numpy as np


with open('predictor.pickle', 'rb') as file:
    model = pickle.load(file)

def predict_price(features):
    return model.predict(features)

st.title('Laptop Price Prediction')


ram = st.number_input('RAM (GB)', min_value=1, max_value=64, value=8)
weight = st.number_input('Weight (kg)', min_value=0.5, max_value=5.0, value=1.5, step=0.1)


company_options = ['Acer', 'Apple', 'Asus', 'Dell', 'HP', 'Lenovo', 'MSI', 'Other', 'Toshiba']
company = st.selectbox('Company', company_options)


type_options = ['2 in 1 Convertible', 'Gaming', 'Netbook', 'Notebook', 'Ultrabook', 'Workstation']
type_name = st.selectbox('Type', type_options)


cpu_options = ['AMD', 'Intel Core i3', 'Intel Core i5', 'Intel Core i7', 'Other']
cpu = st.selectbox('CPU', cpu_options)


gpu_options = ['AMD', 'Intel', 'Nvidia']
gpu = st.selectbox('GPU', gpu_options)


screen_options = ['Touchscreen', 'IPS']
screen_type = st.selectbox('Screen Type', screen_options)

if st.button('Predict Price'):
    features = [ram, weight] + [0] * 25 

    company_index = company_options.index(company) + 4 
    features[company_index] = 1

    type_index = type_options.index(type_name) + 13 
    features[type_index] = 1

    cpu_index = cpu_options.index(cpu) + 19 
    features[cpu_index] = 1

    gpu_index = gpu_options.index(gpu) + 24 
    features[gpu_index] = 1

    if screen_type == 'Touchscreen':
        features[2] = 1
    elif screen_type == 'IPS':
        features[3] = 1


    prediction = predict_price(np.array(features).reshape(1, -1))
    
    st.success(f'The predicted price of the laptop is ${prediction[0]:.2f}')