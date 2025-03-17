import streamlit as st

pages = {
  "SQL": [
    st.Page("pages/sql_merge.py", title="MERGE")],
  "Snowflake": [
    st.Page("pages/test.py", title="My Test")]
}

pg = st.navigation(pages)
pg.run()

st.set_page_config(page_title="home", layout="centered")

st.write('## BI Developer WIKI')
st.write('Find solutions to common problems BI developers face')
st.divider()
st.write('#### SQL')
st.page_link("pages/sql_merge.py", label = "MERGE")
st.write('#### Snowflake')
st.page_link("pages/test.py", label = "Test")
