CREATE TABLE RoommateRequest ( 

Roommate_Request_Number INT NOT NULL AUTO_INCREMENT, 

Student_ID INT, 

Requested_Roommate VARCHAR(50), 

Requst_Date DATE, 

Request_Status VARCHAR(20), 

Approval_Date DATE, 

Status VARCHAR(20), 

PRIMARY KEY(Roommate_Request_Number), 

FOREIGN KEY(Student_ID) REFERENCES Student(Student_ID) 

); 