# Import python packages
import streamlit as st


#st.title(":material/vpn_key: Day 1: Connect to Snowflake")

st.title(":material/cloud: ❄️ Snowflake Connection")



try:
    from snowflake.snowpark.context import get_active_session
    session = get_active_session()
except:
    from snowflake.snowpark import Session
    session = Session.builder.configs(st.secrets["connections"]["snowflake"]).create()

    # Query and display Snowflake version
version = session.sql("SELECT CURRENT_VERSION()").collect()[0][0]
st.success(f"Successfully connected! Snowflake Version: {version}")