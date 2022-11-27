import psycopg2
import pandas as pd
from sqlalchemy import create_engine, MetaData

# This will be different for you depending on the database server you use. 
DB_HOST = "localhost"
DB_NAME = "DatabaseFinalProject"
DB_USER = "soap"
DB_PASS = "brimstone42" #note: change this back to Notebook!013 before uploading it to github


# postgresql+psycopg2://username:password@host:port/database-name
conn_string = 'postgresql+psycopg2://soap:brimstone42@localhost:5432/DatabaseFinalProject'

db = create_engine(conn_string)
conn = db.connect()

# the keys are the headers and the lists are the info for each row.
data = {'Name': ['Tom', 'dick', 'harry'],
		'Age': [22, 21, 24]}

# literally just dictionaries
voter = {'voter_id': [1, 2, 3],
        'education_id': [4, 5, 7],
        'candidate_id': [9, 10, 8],
        'policy_id': [12, 15, 10],
        'gender': ['male', 'female', 'male'],
        'race': ['black', 'white', 'indian'],
        'name': ['Tom', 'dick', 'harry'],
		'age': [22, 21, 24]}

# Create DataFrame
df = pd.DataFrame(data)
dv = pd.DataFrame(voter)

#converts and sends the data to the tables on sql
df.to_sql(name = 'data', con=conn, if_exists='append', index=False)

dv.to_sql(name = 'voter', con=conn, if_exists='append', index=False)

conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)
conn.autocommit = True
cursor = conn.cursor() #the cursor is to perform database operations and queries

# this just checks if the data was uploaded correctly to the database
sql1 = "SELECT * FROM public.voter;"
sql2 = "SELECT * FROM public.data;"
cursor.execute(sql1) #executes the query
for i in cursor.fetchall(): #fetchall () is used to retrieve the query results
	print(i)

cursor.execute(sql2) #executes the query
for f in cursor.fetchall(): #fetchall () is used to retrieve the query results
	print(f)

# conn.commit()
conn.close()