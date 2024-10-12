# Set up and run this Streamlit App
import streamlit as st
import pandas as pd
# from helper_functions import llm
from helper_functions.utility import check_password  
# from  import pandas_tool from ./logics/ask_hdb_data_agent.py file
from logics.ask_hdb_data_agent import pandas_tool
import json

st.set_page_config(
    page_title="HDB Resale Data Explorer MVP",
    page_icon="🎃",
)


# Include Font Awesome
st.markdown("""
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
    """, unsafe_allow_html=True)

# Define the title with a house icon
title_html = """
<h1 style="background: linear-gradient(to right, red, orange, yellow, green, blue, indigo, violet);
            -webkit-background-clip: text;
            color: transparent;"> 
            <i class="fas fa-home"></i> HDB Resale Data Explorer
</h1>
"""


# Check if the password is correct.  
if not check_password():  
    st.stop()

    
# Sidebar navigation
page = st.sidebar.radio("SELECT A PAGE", 
                            ["Home", "Transactions Map", "Methods", "About This App"])

# Home page content
if page == "Home":

        df = pd.read_csv('./data/hdb_2024.csv')
        
        df['transaction_date'] = pd.to_datetime(df['tranc_year_month'])
        
        # Get the unique transaction dates
        available_dates = df['transaction_date'].dt.strftime('%Y-%m').unique()

        # Convert the dates to a comma-separated string
        dates_str = ', '.join(available_dates)
        
        # Display the title in Streamlit
        st.markdown(title_html, unsafe_allow_html=True)

        st.markdown(
            f"""
            Explore and discover with the HDB Resale Data Explorer!!

            This MVP app helps you explore and analyze HDB resale transaction data easily by asking questions.
            
            Due to token limits and low budget, we limit transactions to these year-months {dates_str}

        """, unsafe_allow_html=True
        )
              


        # Custom CSS to change the color of the expander
        st.markdown("""
            <style>
            .stExpander {
                background-color:  #8B4513;  /* Change this to your desired color */
                border: 2px solid #ff6347;  /* Optional: Add a border */
                border-radius: 4px;  /* Optional: Add rounded corners */
            }

            </style>
            """, unsafe_allow_html=True)



        with st.expander("👀IMPORTANT NOTICE: PLEASE READ"):
            st.write("""
            This web application is a prototype developed for educational purposes only. The information provided here is NOT intended for real-world usage and should not be relied upon for making any decisions, especially those related to financial, legal, or healthcare matters.
            Furthermore, please be aware that the LLM may generate inaccurate or incorrect information. You assume full responsibility for how you use any generated output.
            Always consult with qualified professionals for accurate and personalized advice.
            """)


        form = st.form(key='form')
        form.subheader('Ask Data')
        


        user_prompt = form.text_area(   "Enter your prompt", 
                                        value="Example: What is the max price of 5-room flats in Clementi?", 
                                        height=200, 
                                        max_chars = 250,
                                        key="custom-text-area"
                                    )

        # Add the submit button
        submit_button = form.form_submit_button(label="Submit")

             
        if submit_button and user_prompt:
            with st.spinner("Please wait ☕..."):          
                #Run the user_prompt through the ask_HDB
                result = pandas_tool.func(user_prompt)
                
                # Parse the JSON response
                result_text = result.get("output", "")
                
                #Display result
                st.write(result_text)
               

# Methods page content
elif page == "Methods":
    try:
        with open('methods.py', 'r') as f:
            exec(f.read())
    except FileNotFoundError:
        st.error("The file 'Methods.py' was not found. Please check the file path and try again.")  
    

# View All Flats page content
elif page == "Transactions Map":
    try:
        with open('2_Map_Transactions.py', "r") as f:
            exec(f.read())
    except FileNotFoundError:
        st.error("The file '2_Map_Transactions.py' was not found. Please check the file path and try again.")        
       
# About This App page content
elif page == "About This App":
    try:
        with open('3_About_This_App.py', "r", encoding='utf-8') as f:
            exec(f.read())
    except FileNotFoundError:
        st.error("The file '3_About_This_App.py' was not found. Please check the file path and try again.")
        


