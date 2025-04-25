--- the 1 task
CREATE TABLE phonebook(
    ID SERIAL PRIMARY KEY, 
    username VARCHAR(100) NOT NULL , 
    phonenumber VARCHAR(100) NOT NULL UNIQUE
); 



