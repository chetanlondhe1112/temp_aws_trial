import streamlit as st
from sqlalchemy import create_engine
import pandas as pd

_="""

    Database credentials 

"""  
# fetching from .streamlit folder
# connection credentials
user=st.secrets["mysql"]["user"]
password=st.secrets["mysql"]["password"]
host=st.secrets["mysql"]["host"]
port=st.secrets["mysql"]["port"]
database=st.secrets["mysql"]["database"]
# Equity tables credentials
admin = st.secrets["admin_ch"]["admin_ch"]
master_table = st.secrets["db_table"]["master_table"]
filter_table = st.secrets["db_table"]["filter_table"]
query_table = st.secrets["db_table"]["query_table"]
user_table = st.secrets["db_table"]["user_table"]
portfolio_table = st.secrets["db_table"]["portfolio_table"]
news_table = st.secrets["db_table"]["news_table"]
sentiment_table = st.secrets["db_table"]["sentiment_table"]
# Mutual Fund table credentials
mf_sheet_table=st.secrets["db_table"]["mf_sheet_table"]
mf_filter_table=st.secrets["db_table"]["mf_filter_table"]
mf_rolling_return_table=st.secrets["db_table"]["mf_rolling_return_table"]


def sqlalchemy_connection():
    connect_string = "mysql://{}:{}@{}:{}/{}".format(user,password,host,port,database)
    return create_engine(connect_string)


st.title("Database Viewer:")

sq_conn=sqlalchemy_connection()
sq_cur=sq_conn.connect()

st.write("Connection:{}| Connection Cursor:{}".format(sq_conn,sq_cur))

st.subheader(database+":")
q="SHOW TABLES FROM'"+ database+"'"

tables=pd.read_sql_query(q,sq_conn)
st.subheader("Tables:")
st.write(tables)

selected_table=st.selectbox("Select table",options=tables.to_list())

t_q="SELECT * FROM '"+selected_table+"'"
table_df=pd.read_sql_query(t_q,sq_conn)
st.subheader(selected_table+":")
st.write(table_df)
  

"""

        MySQL
    The MySQL dialect uses mysql-python as the default DBAPI. There are many MySQL DBAPIs available, such as MySQL-connector-python as follows −

    # default
    engine = create_engine('mysql://scott:tiger@localhost/foo')

    # mysql-python
    engine = create_engine('mysql+mysqldb://scott:tiger@localhost/foo')

    # MySQL-connector-python
    engine = create_engine('mysql+mysqlconnector://scott:tiger@localhost/foo')

"""

"""
    Streamlit error to connect mysql
    streamlit only requires mysql-connector-python and mysql_client No need to mysql_connector
    
    Hide nysql connector in requirements.txt
    #mysql-connector==2.2.9
    mysql-connector-python==8.0.29
    mysqlclient


"""