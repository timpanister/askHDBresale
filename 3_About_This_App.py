import streamlit as st


# Include Font Awesome
st.markdown("""
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
    """, unsafe_allow_html=True)

# Define the title with a house icon
title_html = """
<h1 style="background: linear-gradient(to right, red, orange, yellow, green, blue, indigo, violet);
            -webkit-background-clip: text;
            color: transparent;"> 
            <i class="fas fa-home"></i> About the HDB Resale Data Explorer App
</h1>
"""


# Display the title in Streamlit
st.markdown(title_html, unsafe_allow_html=True)


ThisApp_Text = """

This interactive web application is designed to help you explore and analyze HDB resale transaction data with ease. Here’s what you can do with our app:

**<span style="color: yellow;">Ask Questions:</span>**: Simply type in your questions about the data, and our app will provide you with insightful answers. For example, you can ask, “What is the median price for flats in Clementi?” and get an accurate response based on the latest data.

Whether you’re a homebuyer, homeseller, a property analyst, or just curious about the HDB resale market, our app is here to provide you with the information you need in a user-friendly and interactive way.

Feel free to explore and discover valuable insights with the HDB Resale Data Explorer!
"""


st.markdown(

ThisApp_Text, unsafe_allow_html=True
)

