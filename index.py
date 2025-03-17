import streamlit as st

st.write('## BI Developer WIKI')
st.write('Find solutions to common problems BI developers face')
st.divider()
st.write('#### SQL')
pages = [
  st.page(page:"app_pages/sql/sql_merge.py", title = "MERGE")
]

pg = st.navigation(pages, position = "sidebar", expanded = True)

pg.run
