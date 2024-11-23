CREATE TABLE EquipmentSignout ( 

Equipment_Signout_Number INT NOT NULL AUTO_INCREMENT, 

Student_ID INT, 

Student_Full_Name VARCHAR(50), 

Room_Number INT, 

Contact_Information VARCHAR(20), 

Equipment_ID INT, 

Equipment_Name VARCHAR(20), 

Signout_Date DATE, 

Return_Date DATE, 

Status VARCHAR(20), 

PRIMARY KEY(Equipment_Signout_Number), 

FOREIGN KEY(Student_ID) REFERENCES Student(Student_ID) 

); 