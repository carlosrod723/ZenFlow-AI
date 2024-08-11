# ZenFlow AI

## Tagline
"Streamline Your AI Model Lifecycle with ZenFlow AI"

## Overview
ZenFlow AI automates the MLOps process by integrating ZenML with AWS SageMaker for seamless deployment of Hugging Face models. This project provides a comprehensive solution for managing the entire AI model lifecycle, from data preparation to model deployment, ensuring consistency, scalability, and efficiency.

## Background & Context
ZenML is an open-source MLOps framework that automates the lifecycle of machine learning models, making it easier to create reproducible pipelines. MLOps practices ensure that models are consistently trained, deployed, and monitored, reducing errors and accelerating innovation. Hugging Face offers advanced NLP models, and by automating their deployment to production environments with ZenFlow AI, teams can maintain high standards of reliability and scalability.

## Features
- **ZenML Pipeline Integration:** Automates the entire MLOps process, including data ingestion, model training, and deployment.
- **AWS SageMaker Deployment:** Seamlessly deploys models to AWS SageMaker, leveraging its robust infrastructure.
- **End-to-End Model Management:** Provides comprehensive tools for managing the AI model lifecycle from start to finish.
- **Real-Time Model Updating:** Continuously checks for new data and updates models accordingly.
- **Custom Monitoring Dashboard:** Integrates with AWS CloudWatch to provide real-time monitoring of model performance.

## Project Structure
- **ZenFlow_AI.ipynb:** Jupyter Notebook containing the full implementation of the ZenFlow AI pipeline.
- **dashboard.py:** Streamlit app for real-time monitoring and visualization of deployed models.
- **requirements.txt:** List of dependencies required to run the project.
- **LICENSE:** MIT License file.

## Getting Started
1. **Clone the Repository:**
   ```bash
   git clone https://github.com/carlosrod723/ZenFlow-AI.git
   cd ZenFlow-AI
   ```

2. **Set Up AWS Credentials:**
   Configure your AWS credentials either by setting environment variables or using AWS CLI.

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the ZenML Pipeline:**
   Execute the Jupyter Notebook (`ZenFlow_AI.ipynb`) in Google Colab or your local environment to run the full pipeline, including data ingestion, model training, and deployment.

5. **Deploy the Monitoring Dashboard:**
   Run the Streamlit app to monitor the performance of your deployed models in real-time:
   ```bash
   streamlit run dashboard.py
   ```

## Monitoring and Alerts
- **CloudWatch Metrics:** Integrated with AWS CloudWatch to monitor key metrics like latency and errors.
- **Custom Alerts:** Set up CloudWatch alerts to notify you of any significant changes in model performance.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributions
Contributions are welcome! Please open an issue or submit a pull request for any improvements or suggestions.
