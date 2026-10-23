import os
from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import load_prompt
from langchain_google_genai import ChatGoogleGenerativeAI

# Load .env file
load_dotenv()

# Gemini model setup (API key auto-pick from env)
model = ChatGoogleGenerativeAI(
    model="gemini-1.5-pro",
    api_key=os.getenv("GOOGLE_API_KEY")   # yahan se key lega
)

st.header('Research Assistant')

paper_input = st.selectbox("Select a research paper", [
    "Attention is all you Need",
    "BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding",
    "GPT-3",
    "OLAMA"
])

style_input = st.selectbox("Select a style", [
    "Summary", "Key Points", "Detailed Analysis", "Comparison", "Critique",
    "Implicationst", "Technical Explanation", "Layman's Explanation",
    "Practical Applications", "Future Directions", "Ethical Considerations",
    "Historical Context", "Interdisciplinary Connections", "Policy Implications",
    "Experimental Design", "Data Interpretation", "Theoretical Frameworks",
    "Methodological Approaches", "Limitations and Challenges",
    "Recommendations for Further Research"
])

length_input = st.selectbox("Select a length", [
    "Short", "Medium", "Long", "Very Long", "Extremely Long", "Concise",
    "Detailed", "Comprehensive", "In-depth", "Thorough", "Extensive",
    "Elaborate", "Succinct", "Brief", "Expanded", "Condensed", "Summarized",
    "Full-length", "Abbreviated"
])

# Load prompt template
template = load_prompt('template.json')

if st.button('Summarize'):
    chain = template | model
    result = chain.invoke({
        'paper_input': paper_input,
        'style_input': style_input,
        'length_input': length_input
    })
    st.write(result.content)

  