import streamlit as st
import pandas as pd
import plotly.express as px

st.title("📈 Model Performance")

accuracy = 0.94
loss = 0.12

col1,col2=st.columns(2)

col1.metric("Accuracy","94%")
col2.metric("Loss","0.12")

history = pd.DataFrame({
    "Epoch":[1,2,3,4,5],
    "Accuracy":[0.62,0.74,0.82,0.89,0.94]
})

fig = px.line(history,x="Epoch",y="Accuracy",markers=True)

st.plotly_chart(fig,use_container_width=True)

st.subheader("Observations")

st.write("""
- Model successfully classifies IT incidents.
- Network and Hardware incidents achieve higher accuracy.
- Chatbot improves first-level IT support experience.
""")