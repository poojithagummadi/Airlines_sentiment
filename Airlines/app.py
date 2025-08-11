import streamlit as st
from transformers import AutoModelForSequenceClassification, AutoTokenizer, pipeline

# ✅ Load model and tokenizer
model_name = "cardiffnlp/twitter-roberta-base-sentiment-latest"
model = AutoModelForSequenceClassification.from_pretrained(model_name, trust_remote_code=True, use_safetensors=True)
tokenizer = AutoTokenizer.from_pretrained(model_name)
classifier = pipeline("sentiment-analysis", model=model, tokenizer=tokenizer)

# ✅ Streamlit UI
st.title("✈️ Airline Tweet Sentiment Classifier")
st.write("Enter an airline-related tweet below and classify its sentiment.")

user_input = st.text_area("Enter a tweet:", placeholder="e.g., I love this product!")

if st.button("Analyze"):
    if user_input.strip():
        result = classifier(user_input, truncation=True)[0]
        st.markdown(f"**Sentiment:** `{result['label']}`")
        st.markdown(f"**Confidence:** `{result['score']:.2f}`")
    else:
        st.warning("Please enter some text.")
