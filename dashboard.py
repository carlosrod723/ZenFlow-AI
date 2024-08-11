# Import necessary libraries
import streamlit as st
import pandas as pd
import datetime

# Mock data with custom timestamps
mock_data = [
    {"Time": datetime.datetime.utcnow() - datetime.timedelta(minutes=10), "Average": 0.25},
    {"Time": datetime.datetime.utcnow() - datetime.timedelta(minutes=5), "Average": 0.30},
    {"Time": datetime.datetime.utcnow(), "Average": 0.20},
]

# Convert mock data into a DataFrame
df = pd.DataFrame(mock_data)

# Streamlit app layout
st.title('ZenFlow AI Monitoring Dashboard')

st.sidebar.header('Metrics Selection')
metric_name = st.sidebar.selectbox("Select Metric", ["Latency", "InvocationErrors", "ErrorCount"])

# Sort the DataFrame by Time
df = df.sort_values(by='Time')

# Display the metrics in a line chart
st.line_chart(df[['Time', 'Average']].set_index('Time'))

st.write('Metrics data:')
st.write(df)
