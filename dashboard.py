# Import necessary libraries
import streamlit as st
import pandas as pd
import numpy as np
import time

# Mock data generation function
def generate_mock_data():
    timestamps = pd.date_range(start='2024-01-01', periods=50, freq='H')
    values = np.random.rand(50) * 100  # Random values
    data = pd.DataFrame({'Timestamp': timestamps, 'Average': values})
    return data

# Streamlit app layout
st.title('ZenFlow AI Monitoring Dashboard (Mock Data)')

# Sidebar for metrics selection (not functional in mock)
st.sidebar.header('Metrics Selection')
metric_name = st.sidebar.selectbox("Select Metric", ["Latency", "InvocationErrors", "ErrorCount"])

# Generate mock data
df = generate_mock_data()
df = df.sort_values(by='Timestamp')

# Display the metrics in a line chart
st.line_chart(df.set_index('Timestamp'))

# Display the mock metrics data
st.write('Metrics data (mock):')
st.write(df)

# Simulate live update of the dashboard
st.write('Refreshing data...')
time.sleep(2)  # Simulate a delay for data update
