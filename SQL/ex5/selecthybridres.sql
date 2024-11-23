SELECT Residence_Name AS residence, Capacity AS capacity 
FROM Residence 
WHERE Residence_Group = 'Hybrid-Style' 
ORDER BY Capacity DESC;