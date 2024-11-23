CREATE TABLE HousingAssignment ( 

Student_ID INT NOT NULL AUTO_INCREMENT,  

Housing_Transfer_Number INT, 

Room_Number INT, 

Floor_Number INT, 

Residence_Name VARCHAR(20), 

PRIMARY KEY(Student_ID), 

FOREIGN KEY(Housing_Transfer_Number) REFERENCES HousingTransfer(Housing_Transfer_Number) 

); 