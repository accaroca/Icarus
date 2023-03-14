import pandas as pd
import streamlit as st
#import base64
import sqlite3
import psycopg2
#import time
#from sqlalchemy import create_engine
import os
#Funciones: algunas son opcionales
def init_connection():
    return psycopg2.connect(**st.secrets["postgres"]) 
#Unica funcion Streamlit
def upload_data():
    upload_file = st.sidebar.file_uploader('Cargar archivo de datos')
    if upload_file is not None and upload_file.endswith('.json'):
        df = pd.read_json(upload_file)
        return df

def save_uploadedfile(uploadedfile):
     with open(os.path.join("tempDir",uploadedfile.name),"wb") as f:
         f.write(uploadedfile.getbuffer())
     return st.success("Tabla Guardada en:{} to tempDir".format(uploadedfile.name))
 
def convert_df_to_csv(df):
   return df.to_csv(index=False).encode('utf-8')

def convert_df_to_json(df):
   return df.to_json(orient='table',index=False).encode('utf-8')

#Crear conexion con la bd
def create_connection(db_file):
    """ create a database connection to the SQLite/postgreSQL database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Exception as e:
        print(e)

    return conn

def data_summary(df):
    print('Resumen de los datos')
    print(df.describe())
#Crear funcion de subida de datos

#Crear funcion de descarga de datos

#Conectamos la Base de Sample

def connect_sample_db():
    conn = sqlite3.connect('sample_DB') 
    c = conn.cursor()
    c.execute('''SELECT order_id,quantity,product_id FROM orders''')
    df = pd.DataFrame(c.fetchall(), columns=['order_id','quantity','product_id'])
    print (df)
    return conn,c,df

#def generate_dataframe(c,query):
    
#%%




