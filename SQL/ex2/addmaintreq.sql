CREATE TABLE MaintenanceRequest ( 

Maintenance_Request_Number INT NOT NULL AUTO_INCREMENT, 

Student_ID INT, 

Maintenance_Type VARCHAR(20), 

Residence_Building VARCHAR(20), 

Room_Number INT, 

Request_Date DATE, 

Completion_Date DATE, 

Status VARCHAR(20), 

PRIMARY KEY(Maintenance_Request_Number), 

FOREIGN KEY(Student_ID) REFERENCES Student(Student_ID) 

); 