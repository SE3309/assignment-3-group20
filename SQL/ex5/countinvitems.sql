SELECT category, COUNT(*) AS count 
FROM CafInventory 
WHERE Category IN ('Beverage', 'Dairy', 'Carbohydrate', 'Protein', 'Produce', 'Condiment') 
GROUP BY Category 
ORDER BY Count DESC;