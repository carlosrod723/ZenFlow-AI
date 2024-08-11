# Import necessary libraries and packages
import streamlit as st
import boto3
import pandas as pd
import datetime

# Initialize Boto3 client for CloudWatch
cloudwatch = boto3.client('cloudwatch', region_name='us-west-2')

# Function to get CloudWatch metrics
def get_cloudwatch_metrics(metric_name, namespace, period=300, start_time=None, end_time=None):
    if start_time is None:
        start_time = datetime.datetime.utcnow() - datetime.timedelta(hours=1)
    if end_time is None:
        end_time = datetime.datetime.utcnow()

    response = cloudwatch.get_metric_statistics(
        Namespace=namespace,
        MetricName=metric_name,
        StartTime=start_time,
        EndTime=end_time,
        Period=period,
        Statistics=['Average']
    )
    return response['Datapoints']

# Streamlit app layout
st.title('ZenFlow AI Monitoring Dashboard')

st.sidebar.header('Metrics Selection')
metric_name = st.sidebar.selectbox("Select Metric", ["Latency", "InvocationErrors", "ErrorCount"])
namespace = st.sidebar.text_input("Namespace", value="AWS/SageMaker")

# Get metrics data
st.write(f'Displaying {metric_name} metrics:')
data = get_cloudwatch_metrics(metric_name, namespace)
df = pd.DataFrame(data)

# Display the DataFrame columns to see what we are working with
st.write("DataFrame Columns:", df.columns.tolist())

# Attempt to sort by 'Timestamp' or skip if it doesn't exist
if 'Timestamp' in df.columns:
    df = df.sort_values(by='Timestamp')
else:
    st.write("'Timestamp' column not found. Skipping sorting.")

# Display the metrics in a line chart if available
if 'Average' in df.columns:
    st.line_chart(df[['Average']])
else:
    st.write("'Average' column not found. Unable to display chart.")

st.write('Metrics data:')
st.write(df)
