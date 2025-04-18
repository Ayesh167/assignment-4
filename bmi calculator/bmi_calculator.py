import streamlit as st

# -------------------------------
# Function to calculate BMI
# -------------------------------
def calculate_bmi(weight, height_cm):
    height_m = height_cm / 100
    bmi = weight / (height_m ** 2)
    return round(bmi, 2)

# -------------------------------
# Function to interpret BMI
# -------------------------------
def get_bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight", "⚠️"
    elif 18.5 <= bmi < 25:
        return "Normal weight", "✅"
    elif 25 <= bmi < 30:
        return "Overweight", "⚠️"
    else:
        return "Obese", "❗"

# -------------------------------
# Streamlit App Layout
# -------------------------------
st.set_page_config(page_title="BMI Calculator", page_icon="📊", layout="centered")

st.title("📊 BMI Calculator Web App")
st.write("Enter your height and weight to calculate your Body Mass Index (BMI).")

# Input fields
col1, col2 = st.columns(2)

with col1:
    height = st.number_input("Height (cm):", min_value=50, max_value=300, value=170)

with col2:
    weight = st.number_input("Weight (kg):", min_value=10, max_value=300, value=70)

# Calculate button
if st.button("Calculate BMI"):
    bmi = calculate_bmi(weight, height)
    category, emoji = get_bmi_category(bmi)

    st.success(f"Your BMI is **{bmi}**")
    st.info(f"Category: **{category}** {emoji}")

    # Optional advice
    if category == "Underweight":
        st.warning("You might need to gain some healthy weight. Consult a nutritionist.")
    elif category == "Overweight" or category == "Obese":
        st.warning("Consider adopting a healthier lifestyle. Regular exercise and diet monitoring help.")
    else:
        st.balloons()

# Footer
st.markdown("""
---
Made with ❤️ using [Streamlit](https://streamlit.io)
""")
