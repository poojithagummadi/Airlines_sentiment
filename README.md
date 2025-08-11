📌 Overview

The **Airline Tweet Sentiment Classifier** is a **Streamlit web application** that uses a **pre-trained NLP model** to classify the sentiment of airline-related tweets as **Positive**, **Neutral**, or **Negative**.

It leverages the **[`cardiffnlp/twitter-roberta-base-sentiment-latest`](https://huggingface.co/cardiffnlp/twitter-roberta-base-sentiment-latest)** model from Hugging Face, which has already been fine-tuned on large-scale Twitter data for sentiment analysis.

This project focuses on:
- Integrating a pre-trained model into a **user-friendly web interface**.
- Providing **real-time sentiment analysis** without needing to train a model.
- Demonstrating how to use **Hugging Face Transformers** with **Streamlit**.

 🚀 Features

- **Real-time Sentiment Classification** – Instantly predicts sentiment as **Positive**, **Neutral**, or **Negative**.
- **Pre-trained Model Integration** – Uses the powerful RoBERTa-based model from Hugging Face.
- **Simple & Intuitive UI** – Built with Streamlit for easy interaction.
- **Lightweight Deployment** – Can run locally or be hosted on Streamlit Cloud/Hugging Face Spaces.
 

pip install -r requirements.txt
4️⃣ Run the Streamlit app

streamlit run app.py
5️⃣ Open in browser
Once Streamlit starts, open the provided local URL (default: http://localhost:8501) in your web browser.
Here’s how the **Airline Tweet Sentiment Classifier** looks in action:
<img width="1920" height="900" alt="Screenshot (14)" src="https://github.com/user-attachments/assets/335e1cc0-ed01-4e05-b15a-6b3bc02acb34" />

<img width="1920" height="897" alt="Screenshot (13)" src="https://github.com/user-attachments/assets/e055b934-cf85-4ee8-9f50-6f6ad74071b9" />

