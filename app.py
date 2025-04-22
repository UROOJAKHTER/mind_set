import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

st.title("Growth Mindset Journey")

# Introduction to Growth Mindset
st.subheader("What is Growth Mindset?")
st.write("Growth mindset is the belief that abilities can be developed through dedication and hard work.")

# Self-assessment quiz
st.subheader("Self-Assessment Quiz")
mindset_score = st.slider("How much do you agree with the following statement? 'I believe I can improve my abilities over time.'", 1, 10, 5)

st.write(f"Your mindset score is: {mindset_score}")

# Visualizing progress with a simple line chart
st.subheader("Your Growth Progress Over Time")

# Sample DataFrame to simulate growth
data = pd.DataFrame({
    'Week': np.arange(1, 11),
    'Progress': np.random.randint(60, 100, size=10)
})

st.line_chart(data.set_index('Week'))

# Growth Tips
st.subheader("Growth Mindset Tip of the Day")
st.write("Focus on effort, not talent! Embrace challenges and learn from criticism.")

