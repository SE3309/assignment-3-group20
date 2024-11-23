CREATE TABLE Equipment ( 

Equipment_ID INT NOT NULL AUTO_INCREMENT, 

Equipment_Name VARCHAR(20), 

Category VARCHAR(20), 

Availability_Status VARCHAR(20), 

Residence_Name VARCHAR(20), 

Equipment_Condition VARCHAR(20), 

PRIMARY KEY(Equipment_ID), 

FOREIGN KEY(Residence_Name) REFERENCES Residence(Residence_Name) 

); 