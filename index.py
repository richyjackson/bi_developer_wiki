import streamlit as st

st.write('## BI Developer WIKI')
st.write('Find solutions to common problems BI developers face')
st.divider()
st.write('#### SQL')
st.sidebar(expanded=True)
pages = [
  st.Page(page:"app_pages/sql/sql_merge.py", title="MERGE")
]

pg = st.navigation(pages, position="sidebar", expanded=True)

pg.run()
