SELECT s.Last_Name AS lastName, s.First_Name AS firstName, s.Student_ID AS studentNo, hp.Room_Type AS preference, ha.Room_Number AS currentRm, ha.Residence_Name AS currentRes, ht.Desired_Room_Number AS requestedRm, ht.Desired_Residence_Building AS requestedRes, ht.Application_Date AS appDate, ht.Status AS appStatus  
FROM Student s 
LEFT JOIN housingpreferences hp ON s.Student_ID = hp.Student_ID 
LEFT JOIN HousingAssignment ha ON s.Student_ID = ha.Student_ID 
LEFT JOIN HousingTransfer ht ON s.Student_ID = ht.Student_ID  
WHERE hp.Room_Type IS NOT NULL 
AND ha.Room_Number IS NOT NULL 
AND ha.Floor_Number IS NOT NULL 
AND ha.Residence_Name IS NOT NULL 
AND ht.Desired_Room_Number IS NOT NULL 
AND ht.Desired_Residence_Building IS NOT NULL 
AND ht.Status IS NOT NULL 
AND ht.Application_Date IS NOT NULL  
ORDER BY s.Last_Name; 