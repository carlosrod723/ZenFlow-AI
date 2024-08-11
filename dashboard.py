import streamlit as st
import pandas as pd
import numpy as np
import datetime

# Generate mock data
def generate_mock_data(num_points=100):
    timestamps = [datetime.datetime.utcnow() - datetime.timedelta(minutes=5 * i) for i in range(num_points)]
    values = np.random.normal(loc=50, scale=10, size=num_points)  # Example metric values
    return pd.DataFrame({'Timestamp': timestamps, 'Average': values})

# Streamlit app layout
st.title('ZenFlow AI Monitoring Dashboard')

st.sidebar.header('Metrics Selection')
metric_name = st.sidebar.selectbox("Select Metric", ["Latency", "InvocationErrors", "ErrorCount"])

# Get mock data
df = generate_mock_data()

# Sort by Timestamp
df = df.sort_values(by='Timestamp')

# Display the metrics in a line chart
st.line_chart(df[['Timestamp', 'Average']].set_index('Timestamp'))

st.write('Metrics data:')
st.write(df)
