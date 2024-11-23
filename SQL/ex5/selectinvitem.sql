SELECT Item_ID AS itemID, Item_Name AS name, Quantity AS quant 
FROM CafInventory 
WHERE Residence_Name = (SELECT Residence_Name 
	FROM CafInventory 
	GROUP BY Residence_Name 
	ORDER BY SUM(Quantity) DESC LIMIT 1);