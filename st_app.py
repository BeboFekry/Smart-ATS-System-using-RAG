import streamlit as st
import os
from Retriever import retriever


st.columns([1,1,1,1,1])[2].image("images/recruitment.png")
st.columns([1.17,1,1])[1].header("ATS System")
st.info("Find new candidates in seconds.")
st.write("---")

if "retriever" not in st.session_state:
    API = st.secrets("API")
    st.session_state.search = retriever(API)
# search = retriever()

st.subheader("Try Using a Sample:")

samples = {}
path = 'Data/job description'
files = os.listdir(path)
for file in files:
    with open(os.path.join(path,file), 'r', encoding='utf-8') as f:
            content = f.read().strip()
            samples[file.split('.')[0]]=content

tabs = st.tabs([" ","AI Engineer","ML Engineer","Data Scientist","Data Analyst","Accountant","HR"])

with tabs[1]:
    st.write(samples["AIEngineer"])
    st.write("Apply These job description now:")
    if st.button("AI Engineer"):
        with st.spinner("Scanning, Please wait..."):
            response = st.session_state.search.find(samples["AIEngineer"])
            st.write(response)
    st.write("---")
with tabs[2]:
    st.write(samples["MLEngineer"])
    st.write("Apply These job description now:")
    if st.button("ML Engineer"):
        with st.spinner("Scanning, Please wait..."):
            response = st.session_state.search.find(samples["MLEngineer"])
            st.write(response)
    st.write("---")
with tabs[3]:
    st.write(samples["DataScientist"])
    st.write("Apply These job description now:")
    if st.button("Data Scientist"):
        with st.spinner("Scanning, Please wait..."):
            response = st.session_state.search.find(samples["DataScientist"])
            st.write(response)
    st.write("---")
with tabs[4]:
    st.write(samples["DataAnalyst"])
    st.write("Apply These job description now:")
    if st.button("Data Anlyst"):
        with st.spinner("Scanning, Please wait..."):
            response = st.session_state.search.find(samples["DataAnlyst"])
            st.write(response)
    st.write("---")
with tabs[5]:
    st.write(samples["Accountant"])
    st.write("Apply These job description now:")
    if st.button("Accountant"):
        with st.spinner("Scanning, Please wait..."):
            response = st.session_state.search.find(samples["Accountant"])
            st.write(response)
    st.write("---")
with tabs[6]:
    st.write(samples["HR"])
    st.write("Apply These job description now:")
    if st.button("HR"):
        with st.spinner("Scanning, Please wait..."):
            response = st.session_state.search.find(samples["HR"])
            st.write(response)
    st.write("---")

message = st.chat_input("Job description...")

if message is None:
    pass
else:
    response = st.session_state.search.find(message)
    st.write(response)
