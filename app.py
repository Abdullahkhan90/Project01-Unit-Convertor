import streamlit as st

# Custom CSS to style the app
st.markdown("""
    <style>
    .stApp {
        background-color: #f0f8ff;
    }
    .stSelectbox, .stNumberInput, .stButton {
        background-color: #e0f7fa;
    }
    .stSelectbox select, .stNumberInput input {
        font-size: 18px;
        padding: 10px;
    }
    h1 {
        color: #1e3a8a;
        font-size: 36px;
        font-family: 'Arial', sans-serif;
        text-align: center;
    }
    h2 {
        color: #00796b;
        font-size: 28px;
        font-family: 'Arial', sans-serif;
        text-align: center;
    }
    .stButton>button {
        background-color: #00796b;
        color: white;
        font-size: 18px;
        padding: 10px;
    }
    .stButton>button:hover {
        background-color: #004d40;
    }
    </style>
""", unsafe_allow_html=True)

# Title of the app
st.title("Abdullah Unit Converter")

# Converting the units to meters
to_meters = {
    "meters": 1.0,
    "kilometers": 1000.0,
    "mile": 1609.34,
    "feet": 0.3048,
    "yard": 0.9144
}

# List of units
units = list(to_meters.keys())
st.write("## Let's convert units and find your equivalent length!")

# Layout of the UI
col1, col2 = st.columns(2)

with col1:
    # Select the unit to convert from
    from_unit = st.selectbox("From Unit:", units)

with col2:
    # Select the unit to convert to
    to_unit = st.selectbox("To Unit:", units)

# Enter the value to convert
value = st.number_input("Enter the value:", min_value=0.0, value=1.0)

# Conversion Logic
if st.button("Convert"):
    # Convert the input value to meters
    value_in_meters = value * to_meters[from_unit]
    
    # Convert meters to the target unit
    converted_value = value_in_meters / to_meters[to_unit]

    # Display the result with a nice success message
    st.success(f"{value} {from_unit} = {converted_value} {to_unit}")
