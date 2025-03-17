import streamlit as st

st.write('## BI Developer WIKI')
st.write('Find solutions to common problems BI developers face')
st.divider()
st.write('#### SQL')
pages = [
  st.Page(page:"bi_developer_wiki/app_pages/sql/sql_merge.py", title = "MERGE")
]

pg = st.navigation(pages, position="sidebar", expanded=True)

pg.run()
