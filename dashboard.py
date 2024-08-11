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
        Statistics=['Sum', 'Average']
    )
    return response['Datapoints']

# Streamlit app layout
st.title('ZenFlow AI Monitoring Dashboard')

st.sidebar.header('Metrics Selection')
metric_name = st.sidebar.selectbox("Select Metric", ["Invocations", "InvocationErrors"])
namespace = st.sidebar.text_input("Namespace", value="AWS/SageMaker")

# Get metrics data
st.write(f'Displaying {metric_name} metrics:')
data = get_cloudwatch_metrics(metric_name, namespace)
df = pd.DataFrame(data)

# Display the columns in the DataFrame
st.write("Available columns in the DataFrame:")
st.write(df.columns)

# Display the entire DataFrame content
st.write("DataFrame content:")
st.write(df)

# Display the data without assuming any specific columns
st.write("Displaying raw data in a table:")
st.table(df)
