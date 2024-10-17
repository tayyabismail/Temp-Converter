import streamlit as st

# Function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Function to convert Fahrenheit to Celsius
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

# Streamlit app setup
st.title("Temperature Converter")

# User input for temperature conversion type
conversion_type = st.radio(
    "Choose the conversion type:",
    ("Celsius to Fahrenheit", "Fahrenheit to Celsius")
)

# Input for the temperature value
temperature_input = st.number_input("Enter the temperature value:")

# Perform the conversion based on the selected type
if conversion_type == "Celsius to Fahrenheit":
    converted_temp = celsius_to_fahrenheit(temperature_input)
    st.write(f"{temperature_input}°C is equal to {converted_temp:.2f}°F")
elif conversion_type == "Fahrenheit to Celsius":
    converted_temp = fahrenheit_to_celsius(temperature_input)
    st.write(f"{temperature_input}°F is equal to {converted_temp:.2f}°C")
