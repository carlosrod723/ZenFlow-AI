import streamlit as st
import boto3
import pandas as pd
import datetime

# Initialize Boto3 client for CloudWatch
try:
    cloudwatch = boto3.client('cloudwatch', region_name='us-west-2')
except Exception as e:
    st.error(f"Failed to initialize CloudWatch client: {str(e)}")
    st.stop()

# Function to get CloudWatch metrics
def get_cloudwatch_metrics(metric_name, namespace, period=300, start_time=None, end_time=None):
    if start_time is None:
        start_time = datetime.datetime.utcnow() - datetime.timedelta(hours=1)
    if end_time is None:
        end_time = datetime.datetime.utcnow()
    try:
        response = cloudwatch.get_metric_statistics(
            Namespace=namespace,
            MetricName=metric_name,
            StartTime=start_time,
            EndTime=end_time,
            Period=period,
            Statistics=['Average']
        )
        return response['Datapoints']
    except Exception as e:
        st.error(f"Error fetching CloudWatch metrics: {str(e)}")
        return []

# Streamlit app layout
st.title('ZenFlow AI Monitoring Dashboard')
st.sidebar.header('Metrics Selection')
metric_name = st.sidebar.selectbox("Select Metric", ["Latency", "InvocationErrors", "ErrorCount"])
namespace = st.sidebar.text_input("Namespace", value="AWS/SageMaker")

# Get metrics data
st.write(f'Displaying {metric_name} metrics:')
data = get_cloudwatch_metrics(metric_name, namespace)

# Debug: Print raw data
st.write("Raw data from CloudWatch:")
st.write(data)

df = pd.DataFrame(data)

# Debugging: Check the DataFrame
st.write("DataFrame info:")
st.write(df.info())

st.write("DataFrame head:")
st.write(df.head())

# Try to sort and plot only if 'Timestamp' and 'Average' exist and DataFrame is not empty
if not df.empty and 'Timestamp' in df.columns and 'Average' in df.columns:
    df['Timestamp'] = pd.to_datetime(df['Timestamp'])
    df = df.sort_values(by='Timestamp')
    st.line_chart(df.set_index('Timestamp')['Average'])
else:
    st.write("No data available or required columns 'Timestamp' or 'Average' not found in the data.")

st.write('Metrics data:')
st.write(df)
