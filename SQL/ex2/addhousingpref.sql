CREATE TABLE HousingPreferences ( 

Housing_Preference_Number INT NOT NULL AUTO_INCREMENT, 

Student_ID INT,  

Room_Type VARCHAR(20), 

Community_Preference VARCHAR(20), 

Roommate_Preference VARCHAR(20), 

PRIMARY KEY(Housing_Preference_Number), 

FOREIGN KEY(Student_ID) REFERENCES Student(Student_ID) 

); 