
import psycopg2
import pandas as pd
from sqlalchemy import create_engine

# This will be different for you depending on the database server you use. 
DB_HOST = "localhost"
DB_NAME = "DatabaseFinalProject"
DB_USER = "postgres"
DB_PASS = "Notebook!013"


# postgresql+psycopg2://username:password@host:port/database-name
conn_string = 'postgresql+psycopg2://postgres:Notebook!013@localhost:5432/DatabaseFinalProject'

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
        'Name': ['Tom', 'dick', 'harry'],
		'Age': [22, 21, 24]}

# Create DataFrame
df = pd.DataFrame(data)
dv = pd.DataFrame(voter)
df.to_sql('data', con=conn, if_exists='replace',
		index=False)

dv.to_sql('voter', con=conn, if_exists='replace',
		index=False)

conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)
conn.autocommit = True
cursor = conn.cursor()

# this just checks if the data was uploaded correctly to the database
sql1 = '''select * from voter;'''
cursor.execute(sql1)
for i in cursor.fetchall():
	print(i)

# conn.commit()
conn.close()
