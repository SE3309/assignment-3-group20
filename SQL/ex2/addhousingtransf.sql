CREATE TABLE HousingTransfer ( 

Housing_Transfer_Number INT NOT NULL AUTO_INCREMENT, 

Student_ID INT, 

Desired_Room_Number VARCHAR(3), 

Desired_Residence_Building VARCHAR(20), 

Status VARCHAR(20), 

Application_Date DATE, 

PRIMARY KEY(Housing_Transfer_Number), 

FOREIGN KEY(Student_ID) REFERENCES Student(Student_ID) 

); 