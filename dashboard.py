# Import necessary libraries
import streamlit as st
import boto3
import pandas as pd
import numpy as np
import datetime

# Initialize Boto3 client for CloudWatch
cloudwatch = boto3.client('cloudwatch', region_name='us-west-2')

# Function to get CloudWatch metrics
def get_cloudwatch_metrics(metric_name, namespace, period=300, start_time=None, end_time=None):
    """
    Retrieve metrics from AWS CloudWatch.

    Args:
        metric_name (str): Name of the metric to retrieve.
        namespace (str): CloudWatch namespace.
        period (int): Time period for each data point.
        start_time (datetime): Start time for the metric data.
        end_time (datetime): End time for the metric data.

    Returns:
        List[Dict]: List of datapoints containing metric statistics.
    """
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

# Get and display metrics data
st.write(f'Displaying {metric_name} metrics from {namespace}:')
data = get_cloudwatch_metrics(metric_name, namespace)

if data:
    # Convert the data to a DataFrame
    df = pd.DataFrame(data)
    df['Timestamp'] = pd.to_datetime(df['Timestamp'])

    # Sort the DataFrame by Timestamp
    df = df.sort_values(by='Timestamp')

    # Display the metrics in a line chart
    st.line_chart(df[['Timestamp', 'Average']].set_index('Timestamp'))

    st.write('Metrics data:')
    st.write(df)
else:
    st.write('No data available. Please ensure the metric name and namespace are correct.')

# Explanatory Comments and Guidance for Users
st.sidebar.header('Instructions for Real-Time Data Integration:')
st.sidebar.write("""
1. **Connect to Real-Time Data:** Ensure that your AWS CloudWatch metrics are correctly configured and that the selected metric has data.
2. **Namespace:** The namespace should be set to match your AWS CloudWatch configuration. Common namespaces include 'AWS/SageMaker' for SageMaker metrics.
3. **Metric Selection:** Choose the metric that you want to visualize from the dropdown menu.
4. **Customization:** For real projects, update the metric names and namespaces to match your specific use case. Ensure that the IAM role associated with your SageMaker and CloudWatch has the necessary permissions.
5. **Further Integration:** If needed, connect this dashboard with your AWS Lambda or other services to trigger updates and monitor model performance in real-time.
""")
