SELECT e.Equipment_ID AS equipID, e.Equipment_Name AS equipName, es.Equipment_Signout_Number AS signoutID, es.Student_Full_Name AS studentName 
FROM Equipment e 
NATURAL JOIN EquipmentSignout es 
WHERE e.Category = 'Cleaning' 
OR e.Category = ‘Sports’; 