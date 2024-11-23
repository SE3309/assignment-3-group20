UPDATE HousingAssignment ha 
JOIN HousingTransfer ht ON ha.Student_ID = ht.Student_ID 
SET ha.Room_Number = ht.Desired_Room_Number, ha.Floor_Number = LEFT(ht.Desired_Room_Number, 1), ha.Residence_Name = ht.Desired_Residence_Building 
WHERE ht.Status = 'Submitted'; 