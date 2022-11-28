# csc4710Team3Project

NOTE: BEFORE YOU DO ANYTHING PLEASE CHANGE THE CONNECTION INFO IN THE PYTHON FILES. I COMMENTED THEM SO JUST SEARCH UP "NOTE" AND YOU SHOULD SEE THEM

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
