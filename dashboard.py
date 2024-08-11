# Import necessary libraries
import streamlit as st
import pandas as pd
import datetime

# Mock data to simulate CloudWatch metrics
mock_data = [
    {"Timestamp": datetime.datetime.utcnow() - datetime.timedelta(minutes=10), "Average": 0.25},
    {"Timestamp": datetime.datetime.utcnow() - datetime.timedelta(minutes=5), "Average": 0.30},
    {"Timestamp": datetime.datetime.utcnow(), "Average": 0.20},
]

# Convert mock data into a DataFrame
df = pd.DataFrame(mock_data)

# Streamlit app layout
st.title('ZenFlow AI Monitoring Dashboard')

st.sidebar.header('Metrics Selection')
metric_name = st.sidebar.selectbox("Select Metric", ["Latency", "InvocationErrors", "ErrorCount"])

# Sort the DataFrame by Timestamp
df = df.sort_values(by='Timestamp')

# Display the metrics in a line chart
st.line_chart(df[['Timestamp', 'Average']].set_index('Timestamp'))

st.write('Metrics data:')
st.write(df)
