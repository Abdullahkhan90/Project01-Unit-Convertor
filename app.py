import streamlit as st

st.title("Abdullah Unit Convertor")

# Converting the units to meters.
to_meters = {
    "meters": 1.0,
    "kolimeters": 1000.0,
    "mile": 1609.34,
    "feet": 0.3048,
    "yard": 0.9144
    }

units = list(to_meters.keys())
st.write("## Let's convert units and find your equivalent length!")
# Select the unit to convert from
from_unit = st.selectbox("From Unit:", units)

# Select the unit to convert to
to_unit = st.selectbox("To Unit:", units)

# Enter the vaue to convert
value = st.number_input("Enter the value:", min_value=0.0, value=1.0)

# Conversion Logic
if st.button("Convert"):
    #Convert the input vaue to meters
    value_in_meters = value * to_meters[from_unit]
    #Convert meters to the target unit
    converted_value = value_in_meters / to_meters[to_unit]
