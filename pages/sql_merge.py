import streamlit as st

st.write('### Update values, add new ones and delete')
st.write('In 2016 SQL introduced the MERGE function allowing you to update values, add new ones and delete. This is a powerful all in one function which minimises and simplifies your code.')
st.write('### Set up code:')

code_block_1 = (
"DECLARE @source AS TABLE (country VARCHAR(50), region_code VARCHAR(2))\n"
"INSERT INTO @source VALUES (\'United Kingdom\', \'GB\')\n"
"INSERT INTO @source VALUES (\'France\', \'FR\')")

st.code(code_block_1, language="SQL")

st.write('### Solution:')

code_block_2 = (

"- Would suggest writing a CTE to transform or filter any source data you wish to asses:\n"
"\n"
"WITH source_data AS (\n"
"\n"
"SELECT\n"
"country,\n"
"region_code\n"
"FROM\n"
"countries\n"
")\n"
"\n"
"- Join your CTE to the table you wish to modify\n"
"\n"
"MERGE INTO mapping.countries AS tgt\n"
"USING source_data AS src ON src.country = tgt.country\n"
"\n"
"- Update fields where there is a match\n"
"\n"
"WHEN MATCHED THEN UPDATE\n"
"\n"
"SET tgt.region_code = src.region_code\n"
"\n"
"- Add values which do not appear in your destination table\n"
"\n"
"WHEN NOT MATCHED THAN INSERT VALUES (src.country)\n"
"\n"
"- Remove values in your destination table which do not appear at source\n"
"\n"
"WHEN NOT MATCHED BY SOURCE THEN DELETE\n"
"\n"
"- All merged statements must be terminated by a semi colon\n"
"\n"
";"


st.code("another line of code", language="SQL")

