SELECT ra.Employee_ID, ra.First_Name, ra.Last_Name, ra.Residence_Name 
FROM ResidenceAdmin ra 
NATURAL JOIN residence r 
WHERE r.Residence_Group = 'Traditional' 
ORDER BY ra.Last_Name ASC; 