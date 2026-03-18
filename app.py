import streamlit as st
import boto3
from botocore.exceptions import BotoCoreError, ClientError


st.set_page_config(page_title="AI Support Knowledge Assistant")

st.title("AI Support Knowledge Assistant")
st.write("Ask a support question and get answers from your knowledge base.")

user_input = st.text_input("Ask a question:")

if st.button("Submit"):
    if user_input.strip():
        st.info("Searching knowledge base and generating response...")

        try:
            client = boto3.client(
                "bedrock-agent-runtime",
                region_name="us-east-1"
            )

            response = client.retrieve_and_generate(
                input={
                    "text": user_input
                },
                retrieveAndGenerateConfiguration={
                    "type": "KNOWLEDGE_BASE",
                    "knowledgeBaseConfiguration": {
                        "knowledgeBaseId": "Y9TZSGOVB2",
                        "modelArn": "arn:aws:bedrock:us-east-1::foundation-model/amazon.nova-lite-v1:0"
                    }
                }
            )

            answer = response["output"]["text"]

            st.success("Answer:")
            st.write(answer)

        except (BotoCoreError, ClientError) as e:
            st.error(f"Error: {e}")

    else:
        st.warning("Please enter a question.")
