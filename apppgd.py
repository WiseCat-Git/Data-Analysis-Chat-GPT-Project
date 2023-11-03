import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
#from chatgpt_module import chat_with_gpt, GPT2LMHeadModel, GPT2Tokenizer # Import GPT2LMHeadModel, GPT2Tokenizer

# problem invoking PyTorch I have used two methods the first by importing torch in the chat
#gpt_module and calling it on apppgd and the second one by creating a requirements.txt that I can use
#to recall PyTorch but none has worked

# Load the pre-trained GPT-2 model and tokenizer
#model = GPT2LMHeadModel.from_pretrained("gpt2")
#tokenizer = GPT2Tokenizer.from_pretrained("gpt2")

st.title('Mi app testing')

st.header('encabezado')

st.write('Esqueleto ejemplo')

# Data source selection
data_source = st.selectbox("Select Data Source", ["Local File", "Google Drive", "Microsoft Drive", "API"])

# Additional buttons for data cleaning and analysis
clean_duplicates = st.button("Clean Duplicates")
remove_nulls = st.button("Remove Null Values")
explore_analysis = st.button("Exploratory Analysis")
format_data_types = st.button("Format Data Types")  # Add button for formatting data types

if data_source == "Local File":
    # File upload section
    uploaded_file = st.file_uploader("Upload File", type=["csv", "txt", "xls", "xlsx"])

    if uploaded_file is not None:
        # Read the data from the uploaded file based on file type
        if uploaded_file.type == 'application/vnd.ms-excel':
            data = pd.read_excel(uploaded_file)
        else:
            data = pd.read_csv(uploaded_file)

        # User chooses the number of rows to preview
        preview_limit = st.slider("Select Rows to Preview", 0, len(data), 10)

        # Display a warning if the dataset is large
        if len(data) > 1000:
            st.warning("Warning: Large dataset. Consider selecting a lower preview limit for better performance.")

        # Display a preview of the data
        st.write("Data Preview:")
        st.write(data.head(preview_limit))

        # Select specific columns for the bar chart
        selected_columns = st.multiselect("Select Columns for Bar Chart", data.columns)
        if selected_columns:
            # Plot bar chart
            st.bar_chart(data[selected_columns])

elif data_source == "Google Drive":
    # Google Drive section
    google_drive_link = st.text_input("Google Drive Link (CSV, TXT, XLS)")
    if st.button("Load from Google Drive"):
        # Assuming the link is a shareable link to a CSV, TXT, or XLS file
        if google_drive_link.endswith((".csv", ".txt")):
            data = pd.read_csv(google_drive_link)
        elif google_drive_link.endswith((".xls", ".xlsx")):
            data = pd.read_excel(google_drive_link)

        # User chooses the number of rows to preview
        preview_limit = st.slider("Select Rows to Preview", 0, len(data), 10)

        # Display a warning if the dataset is large
        if len(data) > 1000:
            st.warning("Warning: Large dataset. Consider selecting a lower preview limit for better performance.")

        # Display a preview of the data
        st.write("Data Preview:")
        st.write(data.head(preview_limit))

        # Select specific columns for the bar chart
        selected_columns = st.multiselect("Select Columns for Bar Chart", data.columns)
        if selected_columns:
            # Plot bar chart
            st.bar_chart(data[selected_columns])

# Repeat the similar logic for "Microsoft Drive" and "API" sections...

# Display message if no data source selected
if 'data' not in locals():
    st.warning("Please Upload your Data or Connect to an API")

# Bar chart section
if 'data' in locals():
    st.bar_chart(data)

# Data Cleaning and Analysis
    if clean_duplicates:
        data.drop_duplicates(inplace=True)
        st.success("Duplicates removed.")

    if remove_nulls:
        data.dropna(inplace=True)
        st.success("Null values removed.")

    if explore_analysis:
        # Perform exploratory analysis (add your analysis code here)
        # For example, you can remove unnecessary columns
        # data = data[['column1', 'column2', ...]]
        st.success("Exploratory analysis completed.")

    if format_data_types:
        # Attempt to automatically detect and transform data types
        data = data.apply(pd.to_numeric, errors='ignore')  # Convert to numeric where possible
        st.success("Data types formatted.")

# User input section
user_input = st.text_input('Escribe algo:', 'Escribe aqui...')
st.write('Escribiste:', user_input)

# ChatGPT panel
#st.sidebar.title("Chat with ChatGPT")

# Create a new chat
#new_chat = st.sidebar.button("New Chat")

#if new_chat:
    #st.session_state.chat_history = []

# Display the last 3 chat messages
#if hasattr(st.session_state, 'chat_history') and st.session_state.chat_history:
    #st.sidebar.subheader("Chat History")
    #for chat_msg in st.session_state.chat_history[-3:]:
        #st.sidebar.text(chat_msg)

# User interacts with ChatGPT
#user_question = st.sidebar.text_area("Ask ChatGPT:")
#if user_question:
    #chat_response_text = chat_with_gpt(user_question, st.session_state.chat_history)
    #st.sidebar.text("ChatGPT: " + chat_response_text)
    #st.session_state.chat_history.append("You: " + user_question)
    #st.session_state.chat_history.append("ChatGPT: " + chat_response_text)
