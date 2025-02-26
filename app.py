import streamlit as st
from pint import UnitRegistry

# Initialize Pint UnitRegistry
ureg = UnitRegistry()
Q_ = ureg.Quantity

# Define a function to perform the conversion
def convert_units(value, from_unit, to_unit):
    try:
        quantity = Q_(value, from_unit)
        converted_quantity = quantity.to(to_unit)
        return converted_quantity.magnitude
    except:
        return None

# Streamlit App
st.set_page_config(page_title="🔢 Abdullah Unit Converter", layout="centered")

# Custom CSS for styling and animations
st.markdown("""
    <style>
    /* General Styling */
    body {
        font-family: 'Arial', sans-serif;
    }
    .stButton>button {
        background-color: #87c7d9;  /* Light blue button */
        color: white;
        font-size: 16px;
        padding: 10px 24px;
        border-radius: 8px;
        border: none;
        transition: background-color 0.3s ease, transform 0.2s ease;
    }
    .stButton>button:hover {
        background-color: #63b3c8;  /* Darker blue on hover */
        transform: scale(1.05);
    }
    .stTextInput>div>div>input, .stSelectbox>div>div>div {
        border: 2px solid #87c7d9;  /* Light blue border */
        border-radius: 8px;
        padding: 10px;
        transition: border-color 0.3s ease;
    }
    .stTextInput>div>div>input:focus, .stSelectbox>div>div>div:focus {
        border-color: #63b3c8;  /* Darker blue on focus */
    }
    .stMarkdown h1 {
        color: #239196;
        text-align: center;
        animation: fadeIn 2s;
    }
    .stMarkdown h2, .stMarkdown h3 {
        color: #239196;
    }
    .stSuccess {
        background-color: #b3dce8;
        color: #0c2782;
        padding: 10px;
        border-radius: 8px;
        border: 1px solid #c3e6cb;
        animation: slideIn 0.5s ease;
    }
    .stError {
        background-color: #dcf9fa;
        color: #2a95b0;
        padding: 10px;
        border-radius: 8px;
        border: 1px solid #f5c6cb;
        animation: shake 0.5s;
    }
    /* Animations */
    @keyframes fadeIn {
        from { opacity: 0; }
        to { opacity: 1; }
    }
    @keyframes slideIn {
        from { transform: translateY(-20px); opacity: 0; }
        to { transform: translateY(0); opacity: 1; }
    }
    @keyframes shake {
        0% { transform: translateX(0); }
        25% { transform: translateX(-10px); }
        50% { transform: translateX(10px); }
        75% { transform: translateX(-10px); }
        100% { transform: translateX(0); }
    }
    </style>
    """, unsafe_allow_html=True)

# Title
st.title("🔢 Abdullah Unit Converter")
st.markdown("""
Instantly convert between various units in real-time! Whether it’s length, mass, temperature, volume, speed, or more – this tool has got you covered!
""")

# Define supported units
unit_categories = {
    "Length": ["meter", "foot", "inch", "mile", "kilometer", "light_year"],
    "Mass": ["kilogram", "gram", "pound", "ounce", "ton"],
    "Temperature": ["celsius", "fahrenheit", "kelvin"],
    "Volume": ["liter", "gallon", "cubic_meter", "cubic_inch"],
    "Speed": ["meter_per_second", "kilometer_per_hour", "mile_per_hour"],
    "Energy": ["joule", "calorie", "btu", "electron_volt"],
}

# Input fields
st.subheader("Enter Your Conversion")

# Updated column layout to ensure dropdowns are fully visible
col1, col2, col3 = st.columns([1, 2, 2])  # Adjust column widths for better display

with col1:
    value = st.number_input("Enter value:", value=1.0, step=0.1)

with col2:
    category = st.selectbox("Select unit category:", list(unit_categories.keys()), key="category")

with col3:
    from_unit = st.selectbox("Select from unit:", unit_categories[category], key="from_unit")

# Target unit
target_unit = st.selectbox("Select target unit:", unit_categories[category], key="target_unit")

# Convert button
if st.button("Convert"):
    with st.spinner("Converting..."):  # Add a loading spinner
        result = convert_units(value, from_unit, target_unit)
        if result is not None:
            st.success(f"✅ **{value} {from_unit} = {result:.4f} {target_unit}**")
        else:
            st.error("❌ Invalid conversion. Please check your units.")

# Add examples and references
with st.expander("📚 Supported Units and Examples"):
    st.markdown("""
    ### Length
    - **meter (m)**, **foot (ft)**, **inch (in)**, **mile (mi)**, **kilometer (km)**, **light_year (ly)**
    - Example: `5 feet to meters`, `10 kilometers to miles`

    ### Mass
    - **kilogram (kg)**, **gram (g)**, **pound (lb)**, **ounce (oz)**, **ton (ton)**
    - Example: `10 kg to pounds`, `150 grams to ounces`

    ### Temperature
    - **celsius (°C)**, **fahrenheit (°F)**, **kelvin (K)**
    - Example: `32 celsius to fahrenheit`, `100 kelvin to celsius`

    ### Volume
    - **liter (L)**, **gallon (gal)**, **cubic_meter (m³)**, **cubic_inch (in³)**
    - Example: `1 gallon to liters`, `5 cubic meters to gallons`

    ### Speed
    - **meter_per_second (m/s)**, **kilometer_per_hour (km/h)**, **mile_per_hour (mph)**
    - Example: `60 mph to km/h`, `10 m/s to km/h`

    ### Energy
    - **joule (J)**, **calorie (cal)**, **btu (BTU)**, **electron_volt (eV)**
    - Example: `1000 joules to calories`, `500 BTU to joules`

    ### How It Works
    1. Enter a value.
    2. Select the unit category (e.g., Length, Mass).
    3. Select the source unit (e.g., `feet`).
    4. Select the target unit (e.g., `meters`).
    5. Click **Convert** to see the result.
    """)

st.markdown("""
    <style>
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: #143c8c;
        color: white;
        text-align: center;
        padding: 10px;
        font-size: 16px;
        font-family: 'Arial', sans-serif;
        animation: fadeIn 2s;
    }
    .footer a {
        color: white;
        text-decoration: none;
        font-weight: bold;
    }
    .footer a:hover {
        color:#b3dce8;
    }
    @keyframes fadeIn {
        from { opacity: 0; }
        to { opacity: 1; }
    }
    </style>
    <div class="footer">
        Created By Abdullah Naeem 🙌
    </div>
    """, unsafe_allow_html=True)

