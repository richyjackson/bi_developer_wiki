import streamlit as st

st.write('### Update values, add new ones and delete')
st.write('In 2016 SQL introduced the MERGE function allowing you to update values, add new ones and delete. This is a powerful all in one function which minimises and simplifies your code.
I frequently use this for performing mapping exercises between two systems and keeping them in sync with each other.')
st.write('### Set up code:')
-- st.code('DECLARE @source AS TABLE (country VARCHAR(50), region_code VARCHAR(2))
-- INSERT INTO @source VALUES (United Kingdom, GB)
-- INSERT INTO @source VALUES (France, FR)', language = "SQL")
