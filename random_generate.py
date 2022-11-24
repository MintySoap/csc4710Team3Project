
import psycopg2
import pandas as pd
from sqlalchemy import create_engine

# This will be different for you depending on the database server you use. 
DB_HOST = "database-3.cpob8oy95cbv.us-east-2.rds.amazonaws.com"
DB_NAME = "ElectionHistory"
DB_USER = "postgres"
DB_PASS = "Notebook!013"


# postgresql+psycopg2://username:password@host:port/database-name
conn_string = 'postgresql+psycopg2://postgres:Notebook!013@database-3.cpob8oy95cbv.us-east-2.rds.amazonaws.com:5432/ElectionHistory'

db = create_engine(conn_string)
conn = db.connect()


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
