import streamlit as st

st.title("Abdullah Unit Converter")

# Converting the units to meters.
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

# Select the unit to convert from
from_unit = st.selectbox("From Unit:", units)

# Select the unit to convert to
to_unit = st.selectbox("To Unit:", units)

# Enter the value to convert
value = st.number_input("Enter the value:", min_value=0.0, value=1.0)

# Conversion Logic
if st.button("Convert"):
    # Ensure the conversion logic is being triggered.
    st.write("Button clicked!")
    
    # Check if the inputs are valid
    if from_unit == to_unit:
        st.warning("The source and target units are the same. Please choose different units.")
    else:
        # Convert the input value to meters
        value_in_meters = value * to_meters[from_unit]
        
        # Convert meters to the target unit
        converted_value = value_in_meters / to_meters[to_unit]
        
        # Display the result with a success message
        st.success(f"{value} {from_unit} = {converted_value} {to_unit}")
