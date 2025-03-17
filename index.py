import streamlit as st

st.title("Home")
st.write('## BI Developer WIKI')
st.write('Find solutions to common problems BI developers face')
st.divider()
st.write('#### SQL')
st.page_link("pages/sql_merge.py", label = "MERGE")
st.write('#### Snowflake')
st.page_link("pages/test.py", label = "Test")
