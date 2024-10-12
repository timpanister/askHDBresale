 
from langchain.agents import Tool
from langchain.agents.agent_types import AgentType
from langchain_experimental.agents.agent_toolkits import create_pandas_dataframe_agent
from langchain_openai import ChatOpenAI
import pandas as pd
import matplotlib.pyplot as plt
import os
from dotenv import load_dotenv
import streamlit as st

if load_dotenv('.env'):
    # for local development
    OPENAI_KEY = os.getenv('OPENAI_API_KEY')
else:
    # for production to STreamlit, grab key from the Secrets in Streamlit Community Cloud App Advanced Settings
    OPENAI_KEY = st.secrets['OPENAI_API_KEY']


# Initialize the ChatOpenAI with the API key
llm = ChatOpenAI(api_key=OPENAI_KEY, temperature=0, model='gpt-4o-mini')


# Read in resale data file
df = pd.read_csv("./data/hdb_2024.csv")
# Convert to datetime
df['transaction_date'] = pd.to_datetime(df['tranc_year_month'])



llm = ChatOpenAI(temperature=0, model='gpt-4o-mini')

pandas_tool_agent = create_pandas_dataframe_agent(
	llm=llm,
	df=df,
	# agent_type=AgentType.OPENAI_FUNCTIONS,
	agent_type="tool-calling", #<--“tool-calling” is recommended over the legacy “openai-tools” and “openai-functions” types.
	allow_dangerous_code=True, # <-- This is an "acknowledgement" that this can run potentially dangerous code,
	verbose=True, # Enable verbose logging
	return_intermediate_steps=True, 
)


# Create the tool
pandas_tool = Tool(
	name="Manipulate and Analyze tabular data with Code",
	func=pandas_tool_agent.invoke, # <-- This is the function that will be called when the tool is run. Note that there is no `()` at the end
	description="Useful for search-based queries",
)

