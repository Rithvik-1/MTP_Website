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

# Add a background image and style for UV dose
st.markdown(
    """
    <style>
        .css-18e3th9 {
            background-image: url('https://images.unsplash.com/photo-1594784022066-e3b5ce6ca015');
            background-size: cover;
        }
        .alert-box {
            padding: 10px;
            border-radius: 5px;
            margin: 10px 0px;
            font-size: 18px; /* Larger font size for better readability */
        }
        .uv-dose-box {
            background-color: #e6ffe6; /* Light green background for UV dose */
            padding: 10px;
            border-radius: 5px;
            font-size: 18px; /* Consistent font size with the alert box */
            color: #2c662d; /* Dark green text color */
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
    if prediction < 5:
        color = "#ffcccc"  # Light red
        text_color = "darkred"
        alert_msg = "<span style='color: darkred;'> - Alert: Critical low level!</span>"
    else:
        color = "#ccffcc"  # Light green
        text_color = "darkgreen"
        alert_msg = "<span style='color: darkgreen;'> - Alert: Satisfactory level!</span>"
        
    prediction_text = f'<div class="alert-box" style="background-color: {color};"><strong>Predicted E. coli reduction:</strong> <span style="color: {text_color};">{prediction:.3f} log</span>{alert_msg}</div>'
    st.markdown(prediction_text, unsafe_allow_html=True)

    uv_dose_value = prediction * 2.5
    uv_dose_text = f'<div class="uv-dose-box"><strong>Predicted UV dose value:</strong> {uv_dose_value:.3f} J/cm²</div>'
    st.markdown(uv_dose_text, unsafe_allow_html=True)




# import streamlit as st
# import pandas as pd
# import pickle

# # Load the saved model
# with open('xgb_model.pkl', 'rb') as file:
#     model = pickle.load(file)

# # Function to predict E. coli reduction
# def predict_reduction(diameter, flow_rate, absorption_coefficient):
#     input_data = pd.DataFrame(
#         [[diameter, flow_rate, absorption_coefficient]], columns=['D', 'F', 'A'])
#     prediction = model.predict(input_data)[0]
#     return prediction

# # Set page config with background image
# st.set_page_config(
#     page_title='UV Reactor Intensity Prediction',
#     page_icon=':microscope:',
#     layout='centered',
#     initial_sidebar_state='auto'
# )

# # Add a background image
# st.markdown(
#     """
#     <style>
#         .css-18e3th9 {
#             background-image: url('https://images.unsplash.com/photo-1594784022066-e3b5ce6ca015');
#             background-size: cover;
#         }
#     </style>
#     """,
#     unsafe_allow_html=True
# )

# # Title and input fields
# st.title('UV Reactor Intensity Prediction')
# st.write('Enter the values for Diameter, Flow rate, and Absorption Coefficient to predict E. coli reduction.')

# diameter = st.number_input('Diameter', min_value=0.0, max_value=100.0, value=5.0)
# flow_rate = st.number_input('Flow rate', min_value=0.0, max_value=1000.0, value=100.0)
# absorption_coefficient = st.number_input('Absorption Coefficient', min_value=0.0, max_value=1000.0, value=100.0)

# if st.button('Predict'):
#     prediction = predict_reduction(diameter, flow_rate, absorption_coefficient)
#     alert_message = " (critical low!)" if prediction < 5 else ""
#     st.success(f'Predicted E. coli reduction: {prediction:.3f} log{alert_message}')
    
#     uv_dose_value = prediction * 2.5
#     st.success(f'Predicted UV dose value: {uv_dose_value:.3f} J/cm²')
