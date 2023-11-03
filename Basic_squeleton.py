import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt  # Added this line


st.title('Mi app testing')
st.header('encabezado')
st.write('Esqueleto ejemplo')

# Initialize data variable
data = None

# Data source selection
data_source = st.selectbox("Select Data Source", ["Local File", "Google Drive", "Microsoft Drive", "API"])

if data_source == "Local File":
    # File upload section
    uploaded_file = st.file_uploader("Upload File", type=["csv", "txt", "xls", "xlsx"])

    if uploaded_file is not None:
        # Read the data from the uploaded file based on file type
        if uploaded_file.type == 'application/vnd.ms-excel':
            excel_file = pd.ExcelFile(uploaded_file)
            # Assuming there is only one sheet in the Excel file
            sheet_name = excel_file.sheet_names[0]
            data = pd.read_excel(excel_file, sheet_name)
        elif uploaded_file.type == 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet':
            data = pd.read_excel(uploaded_file)
        elif uploaded_file.type in ['text/csv', 'text/plain']:
            data = pd.read_csv(uploaded_file)
        else:
            st.error(f"Unsupported file type: {uploaded_file.type}")
            st.stop()

        st.write("Data loaded from uploaded file:")
        st.write(data)

        # User chooses the number of rows to preview
        preview_limit = st.slider("Select Rows to Preview", 0, len(data), 10)

        # Display a warning if the dataset is large
        if len(data) > 1000:
            st.warning("Warning: Large dataset. Consider selecting a lower preview limit for better performance.")

        # Display a preview of the data
        st.write("Data Preview:")
        st.write(data.head(preview_limit))

        # Prompt message
        st.info("Please prepare your data.")

elif data_source == "Google Drive":
    # Google Drive section
    google_drive_link = st.text_input("Google Drive Link (CSV, TXT, XLS, XLSX)")
    if st.button("Load from Google Drive"):
        # Assuming the link is a shareable link to a CSV, TXT, or XLS/XLSX file
        if google_drive_link.endswith((".csv", ".txt")):
            data = pd.read_csv(google_drive_link)
        elif google_drive_link.endswith((".xls", ".xlsx")):
            data = pd.read_excel(google_drive_link)
        st.write("Data loaded from Google Drive:")
        st.write(data)

        # Prompt message
        st.info("Please prepare your data.")

        # User chooses the number of rows to preview
        preview_limit = st.slider("Select Rows to Preview", 0, len(data), 10)

        # Display a warning if the dataset is large
        if len(data) > 1000:
            st.warning("Warning: Large dataset. Consider selecting a lower preview limit for better performance.")

        # Display a preview of the data
        st.write("Data Preview:")
        st.write(data.head(preview_limit))

        # Prompt message
        st.info("Please prepare your data.")

elif data_source == "Microsoft Drive":
    # Microsoft Drive section (Assuming you have a direct link to the file)
    microsoft_drive_link = st.text_input("Microsoft Drive Link (CSV, TXT, XLS)")
    if st.button("Load from Microsoft Drive"):
        # Assuming the link is a shareable link to a CSV, TXT, or XLS file
        if microsoft_drive_link.endswith((".csv", ".txt")):
            data = pd.read_csv(microsoft_drive_link)
        elif microsoft_drive_link.endswith((".xls", ".xlsx")):
            data = pd.read_excel(microsoft_drive_link)
        st.write("Data loaded from Microsoft Drive:")
        st.write(data)

        # Prompt message
        st.info("Please prepare your data.")
        
        # User chooses the number of rows to preview
        preview_limit = st.slider("Select Rows to Preview", 0, len(data), 10)

        # Display a warning if the dataset is large
        if len(data) > 1000:
            st.warning("Warning: Large dataset. Consider selecting a lower preview limit for better performance.")

        # Display a preview of the data
        st.write("Data Preview:")
        st.write(data.head(preview_limit))

elif data_source == "API":
    # API connection section
    api_url = st.text_input("API URL")
    # Additional parameters for API connection if needed
    api_params = st.text_input("API Parameters (if any)")
    if st.button("Connect to API"):
        # Use the appropriate code to connect to the API and fetch data
        # For example, you can use the requests library
        # api_response = requests.get(api_url, params=api_params)
        # data = pd.DataFrame(api_response.json())  # Assuming the API returns JSON data
        st.write("Data loaded from API:")
        st.write(data)

        # User chooses the number of rows to preview
        preview_limit = st.slider("Select Rows to Preview", 0, len(data), 10)

        # Display a warning if the dataset is large
        if len(data) > 1000:
            st.warning("Warning: Large dataset. Consider selecting a lower preview limit for better performance.")

        # Display a preview of the data
        st.write("Data Preview:")
        st.write(data.head(preview_limit))

# Display message if no data source selected
if data is None:
    st.warning("Please Upload your Data or Connect to an API")

# User input section
user_input = st.text_input('Escribe algo:', 'Escribe aqui...')
st.write('Escribiste:', user_input)