# First, import the necessary libraries and modules

from dotenv import load_dotenv  # Used to load environment variables from a .env file

import os  # Used for working with operating system-related functionalities

import streamlit as st  # Used for creating a Streamlit web app

import pandas as pd  # Used for working with tabular data

from pandasai import PandasAI  # A tool for generating code to analyze pandas DataFrames

from pandasai.llm.openai import OpenAI  # A module to interact with OpenAI's language model

import matplotlib  # A library for creating data visualizations

 

# Set the backend for matplotlib to 'TkAgg'

matplotlib.use('TkAgg')

 

# Load environment variables from a .env file (for security, such as API keys)

load_dotenv()

 

# Retrieve the OpenAI API key from the environment variables

API_KEY = os.environ['OPENAI_API_KEY']

 

# Initialize an OpenAI instance with the provided API key

llm = OpenAI(api_token=API_KEY)

 

# Initialize the PandasAI tool with the OpenAI instance

pandas_ai = PandasAI(llm)

 

# Create a Streamlit web app and set the title

st.title("Prompt-driven Analysis with PandasAI")

 

# Allow the user to upload a CSV file for analysis

uploaded_file = st.file_uploader("Upload a CSV file for analysis", type=['csv'])

 

# If a CSV file is uploaded

if uploaded_file is not None:

    # Read the CSV file into a pandas DataFrame

    df = pd.read_csv(uploaded_file)

    # Display the first 3 rows of the DataFrame

    st.write(df.head(3))

 

    # Allow the user to enter a prompt for analysis

    prompt = st.text_area('Enter your prompt:')

 

    # If the "Generate" button is clicked

    if st.button("Generate:"):

        # Check if a prompt is provided

        if prompt:

            # Display a spinner to indicate that the analysis is in progress

            with st.spinner("Generating response..."):

                # Use PandasAI to analyze the DataFrame using the provided prompt

                st.write(pandas_ai.run(df, prompt=prompt))

        else:

            # Display a warning if no prompt is entered

            st.warning("Please enter your prompt.")