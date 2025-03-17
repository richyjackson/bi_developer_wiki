import streamlit as st

st.write('## BI Developer WIKI')
st.write('Find solutions to common problems BI developers face')
st.divider()
st.write('#### SQL')

pg = st.navigation([
    st.Page("app_pages/sql/sql_merge.py", title="MERGE", icon="🔥")
], position="sidebar", expanded=False)

pg.run()
