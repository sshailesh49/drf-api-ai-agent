import streamlit as st
import requests

st.set_page_config(page_title="💱 AI Agent DRF API  - weather and search tools  ", layout="centered")

st.title("💱 AI Agent DRF API  - weather and search tools")
st.caption("Powered by Shailesh Sharma - LangChain + Groq + DRF")

user_query = st.text_input(
    "Enter your request",
    placeholder="Find the capital of Madhya Pradesh, then find it's current weather condition,then population of the capital."
)

if st.button("Search"):
    with st.spinner("Thinking..."):
        res = requests.post(
            "http://backend:8000/api/convert/",
            json={"query": user_query}
        )

        if res.status_code == 200:
            st.success(res.json()["answer"])
        else:
            st.error("Backend error")

##  run cmd : streamlit run app.py
# cd frontend
# streamlit run app.py