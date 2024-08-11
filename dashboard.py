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
        st.write("CloudWatch API Response:", response)  # Debug: Print full API response
        return response.get('Datapoints', [])
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

st.write("Raw data from CloudWatch:")
st.write(data)

if not data:
    st.warning("No data returned from CloudWatch. Please check your metric name, namespace, and AWS credentials.")
    st.stop()

df = pd.DataFrame(data)

st.write("DataFrame info:")
st.write(df.info())

st.write("DataFrame head:")
st.write(df.head())

# Check for required columns
required_columns = ['Timestamp', 'Average']
missing_columns = [col for col in required_columns if col not in df.columns]

if missing_columns:
    st.error(f"Missing required columns: {', '.join(missing_columns)}")
    st.write("Available columns:", df.columns)
    st.stop()

# If we reach here, we have the required columns
df['Timestamp'] = pd.to_datetime(df['Timestamp'])
df = df.sort_values(by='Timestamp')
st.line_chart(df.set_index('Timestamp')['Average'])

st.write('Metrics data:')
st.write(df)
