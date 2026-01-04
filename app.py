import streamlit as st
from evaluate import run

st.title("Prompt Evaluation System")

question = st.text_input("Enter a question")

if question:
    for p in ["prompts/base.yaml", "prompts/v1.yaml"]:
        output, score = run(p, question)
        st.subheader(p)
        st.write(output)
        st.metric("BLEU score", round(score, 3))
