import streamlit as st
import random

st.markdown("""
    <style>
        .stApp {
            background-color: transparent !important;
        }
        h1 {
            text-align: center;
            font-family: 'Arial Black', sans-serif;
            color: #ffffff;
            text-shadow: 3px 3px 10px rgba(255, 255, 255, 0.2);
        }
        .circle {
            position: fixed;
            border-radius: 50%;
            opacity: 0.8;
            animation: float 8s infinite alternate ease-in-out;
        }
        @keyframes float {
            0% { transform: translateY(0) translateX(0); }
            100% { transform: translateY(-30px) translateX(30px); }
        }
        .neon-button {
            background: linear-gradient(45deg, #ff007f, #ff00ff);
            border: none;
            color: white;
            padding: 12px 20px;
            font-size: 18px;
            border-radius: 10px;
            cursor: pointer;
            box-shadow: 0 4px 20px rgba(255, 0, 127, 0.7);
        }
        .neon-button:hover {
            background: linear-gradient(45deg, #ff00ff, #ff007f);
            box-shadow: 0 6px 25px rgba(255, 0, 127, 1);
        }
    </style>
""", unsafe_allow_html=True)

def generate_shapes():
    shape_html = ""
    for _ in range(15):  
        size = random.randint(40, 100)
        top = random.randint(5, 95)
        left = random.randint(5, 95)
        color = f"rgba({random.randint(100,255)}, {random.randint(0,255)}, {random.randint(100,255)}, 0.8)"  
        
        shape_html += f"""
            <div class='circle' style='
                width: {size}px; height: {size}px;
                top: {top}%; left: {left}%;
                background: {color};
                position: fixed;'>
            </div>
        """
    return shape_html

st.markdown(generate_shapes(), unsafe_allow_html=True)

st.title("🌟Unit Converter 🚀")

category = st.selectbox("🎯 Choose a Category:", ["Length", "Weight", "Temperature"])

st.markdown("<hr style='border: 1px dashed white;'>", unsafe_allow_html=True)

if category == "Length":
    unit = st.radio("📏 Select Conversion:", ["Meters to Feet", "Feet to Meters", "Centimeters to Inches", "Inches to Centimeters"])
    value = st.number_input("🔢 Enter value:", min_value=0.0, format="%.2f")
    
    if unit == "Meters to Feet":
        result = value * 3.28084
    elif unit == "Feet to Meters":
        result = value / 3.28084
    elif unit == "Centimeters to Inches":
        result = value / 2.54
    elif unit == "Inches to Centimeters":
        result = value * 2.54

    if st.button("🔄 Convert", key="length_btn"):
        st.success(f"🎯 Converted Value: {result:.2f}")

elif category == "Weight":
    unit = st.radio("⚖️ Select Conversion:", ["Kilograms to Pounds", "Pounds to Kilograms"])
    value = st.number_input("🔢 Enter value:", min_value=0.0, format="%.2f")

    if unit == "Kilograms to Pounds":
        result = value * 2.20462
    elif unit == "Pounds to Kilograms":
        result = value / 2.20462

    if st.button("🔄 Convert", key="weight_btn"):
        st.success(f"🎯 Converted Value: {result:.2f}")

elif category == "Temperature":
    unit = st.radio("🌡 Select Conversion:", ["Celsius to Fahrenheit", "Fahrenheit to Celsius"])
    value = st.number_input("🔢 Enter value:", format="%.2f")

    if unit == "Celsius to Fahrenheit":
        result = (value * 9/5) + 32
    elif unit == "Fahrenheit to Celsius":
        result = (value - 32) * 5/9

    if st.button("🔄 Convert", key="temp_btn"):
        st.success(f"🎯 Converted Value: {result:.2f}")

st.markdown("<hr style='border: 1px dashed white;'>", unsafe_allow_html=True)
st.markdown("""
    <p style='text-align:center; font-size: 18px; color: white;'>✨ Made with 💖 in Streamlit ✨</p>
""", unsafe_allow_html=True)
