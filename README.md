# csc4710Team3Project

Files:
ERD.png - our ERD diagram
Project_ER_Diagram.PGERD - The file that PGAdmin opens up to show the ERD
create_tables.py - The python script that we programmed to create the tables for us
populate_tables.py - The python script that we programmed to fill our tables with randomly generated data that still fits our schema
create_insert.sql - holds all of the sql statements for creating the table and inserting each and every row

NOTE: BEFORE YOU DO ANYTHING PLEASE CHANGE THE CONNECTION INFO IN THE PYTHON FILES. I COMMENTED THEM SO JUST SEARCH UP "NOTE" AND YOU SHOULD SEE THEM
NOTE: Because our database is randomly generated with our python scripts, if you try to run our python scripts with the steps lined out below, you will get a different output than create_insert.sql. However, they should both make sense. This is simply due to the fact that each new generation is unique.

Steps:
1. run python3 create_tables.py
2. Navigate to populate_tables.py file and make sure that line 384 (find_winners()) is commented out, and make sure 
   lines 386-388 (if __name__ == "__main__":    
                  generate_data = GenerateData()   
                  generate_data.create_data()) are NOT commented out. 
3. run "python3 populate_tables.py [insert_table_name_here] [insert_number_of_rows_here]" in this order of table names:  
   A. python3 populate_tables.py location [insert_number_of_rows_here]  
   B. python3 populate_tables.py issue [insert_number_of_rows_here]  
   ----a. No more than 177 as we only have 177 issues  
   C. python3 populate_tables.py election [insert_number_of_rows_here]  
   D. python3 populate_tables.py demographic [any number]  
   ----a. I have it set so that it will always populate 192 rows  
   E. python3 populate_tables.py platform [insert_number_of_rows_here]  
   F. python3 populate_tables.py polling_location [insert_number_of_rows_here]  
   G. python3 populate_tables.py party 50  
   ----a. yes I know that we need 100 rows, but just trust me. I made it so we'll have 50 rows for democrat party and 50 rows for republican party based on state  
   H. python3 populate_tables.py policy [insert_number_of_rows_here]  
   I. python3 populate_tables.py candidate [insert_number_of_rows_here]  
   J. python3 populate_tables.py voter [insert_number_of_rows_here]  
   K. python3 populate_tables.py candidate_Policy [insert_number_of_rows_here]  

4. Navigate to populate_tables.py file and make sure that line 384 (find_winners()) is NOT commented out, and make sure 
   lines 386-388 (if __name__ == "__main__":    
                  generate_data = GenerateData()   
                  generate_data.create_data()) are commented out.
   Then run the populate_tables.py file normally: python3 populate_tables.py.

5. Don't run the file again because it will mess up the number of winners in the database and you will have to regenerate new data!


![alt text](https://github.com/MintySoap/csc4710Team3Project/blob/main/ERD.png?raw=true)
