UPDATE MaintenanceRequest mr 
JOIN Student s ON mr.Student_ID = s.Student_ID 
JOIN residence r ON mr.Residence_Building = r.Residence_Name 
SET mr.Completion_Date = CURRENT_DATE(), mr.Status = 'Completed' 
WHERE r.Residence_Group = 'Suite-Style' 
OR r.Residence_Group = 'Hybrid-Style' 
AND s.Gender = 'Female'; 