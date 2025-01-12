import streamlit as st

st.write('### Update values, add new ones and delete')
st.write('In 2016 SQL introduced the MERGE function allowing you to update values, add new ones and delete. This is a powerful all in one function which minimises and simplifies your code.')
st.write('### Set up code:')
st.write('It doesnt seem to be updating')
code_block_1 = (
"DECLARE @source AS TABLE (country VARCHAR(50), region_code VARCHAR(2))\n"\n
"INSERT INTO @source VALUES (\'United Kingdom\', \'GB\')\n"
"INSERT INTO @source VALUES (\'France\', \'FR\')")

st.code(code_block_1, language="SQL")
st.code("another line of code", language="SQL")
