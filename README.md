AI Support Knowledge Assistant (RAG Application)

A Streamlit-based application that answers support questions using a custom Amazon Bedrock knowledge base.

This project implements Retrieval-Augmented Generation (RAG) by connecting a Streamlit user interface to an Amazon Bedrock Knowledge Base. User questions are sent to the knowledge base, relevant content is retrieved, and a foundation model generates a context-aware response.

## Features

- Ask support related questions in a simple web app
- Retrieve answers from a custom Amazon Bedrock knowledge base
- Generate responses using the Amazon Bedrock foundation model Nova Lite 1.0
- Built with Python, Streamlit, boto3, and AWS Bedrock

## Tech Stack

- Python
- Streamlit
- AWS Bedrock
- boto3

## How It Works

1. User enters a question in the Streamlit app
2. The app sends the request to Amazon Bedrock
3. The Knowledge Base retrieves relevant information
4. The model generates a response
5. The answer is displayed to the user


##Screenshots 

### Example Response: Password Reset
![Password Reset](ai-support-knowledge-assistant-qa-password-reset.png)

### Example Response: Payment Issue
![Payment Issue](ai-support-knowledge-assistant-qa-payment-issue.png)

### Example Response: Account Security
![Account Security](ai-support-knowledge-assistant-qa-account-security.png)

## AWS Setup (How It Was Built)

### Data Preparation

#### S3 File Upload
![S3 Upload](s3-files-upload.png)

#### Indexed Documents
![Indexed Documents](indexed-documents.png)

---

### Knowledge Base Setup

#### Knowledge Base Overview
![Knowledge Base Overview](knowledge-base-overview.png)

#### Data Source Configuration
![Data Source Configuration](data-source-config.png)

#### Knowledge Base Configuration
![Knowledge Base Configuration](knowledge-base-config.png)

---

### Retrieval Configuration

#### Embeddings Configuration
![Embeddings Configuration](embeddings-config.png)

#### Vector Store Setup
![Vector Store](vector-store.png)

#### Model Selection
![Model Selection](model-selection.png)

---

### Testing

#### Retrieval Test Output
![Retrieval Test](retrieval-test-output.png)
