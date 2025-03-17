import streamlit as st

st.write('## BI Developer WIKI')
st.write('Find solutions to common problems BI developers face')
st.divider()
st.write('#### SQL')

st.sidebar.page_link("app_pages/sql/sql_merge.py", label="Merge")
