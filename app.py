import streamlit as st
import pandas as pd
import pickle

# Load the saved model
with open('xgb_model.pkl', 'rb') as file:
    model = pickle.load(file)

# Function to predict E. coli reduction
def predict_reduction(diameter, flow_rate, absorption_coefficient):
    input_data = pd.DataFrame(
        [[diameter, flow_rate, absorption_coefficient]], columns=['D', 'F', 'A'])
    prediction = model.predict(input_data)[0]
    return prediction

# Set page config with background image
st.set_page_config(
    page_title='UV Reactor Intensity Prediction',
    page_icon=':microscope:',
    layout='centered',
    initial_sidebar_state='auto'
)

# Add a background image
st.markdown(
    """
    <style>
        .css-18e3th9 {
            background-image: url('https://images.unsplash.com/photo-1594784022066-e3b5ce6ca015');
            background-size: cover;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Title and input fields
st.title('UV Reactor Intensity Prediction')
st.write('Enter the values for Diameter, Flow rate, and Absorption Coefficient to predict E. coli reduction.')

diameter = st.number_input('Diameter', min_value=0.0, max_value=100.0, value=5.0)
flow_rate = st.number_input('Flow rate', min_value=0.0, max_value=1000.0, value=100.0)
absorption_coefficient = st.number_input('Absorption Coefficient', min_value=0.0, max_value=1000.0, value=100.0)

if st.button('Predict'):
    prediction = predict_reduction(diameter, flow_rate, absorption_coefficient)
    prediction_text = f'Predicted E. coli reduction: {"<span style=\'color: red;\'>" + str(prediction) + " log</span>" if prediction < 5 else str(prediction) + " log"}'
    uv_dose_value = prediction * 2.5
    uv_dose_text = f'Predicted UV dose value
