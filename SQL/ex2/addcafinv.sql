CREATE TABLE CafInventory ( 

Item_ID INT NOT NULL AUTO_INCREMENT, 

Item_Name VARCHAR(20), 

Category VARCHAR(20), 

Quantity VARCHAR(20), 

Residence_Name VARCHAR(20), 

Last_Update_Date DATE, 

PRIMARY KEY(Item_ID), 

FOREIGN KEY(Residence_Name) REFERENCES Residence(Residence_Name)

); 