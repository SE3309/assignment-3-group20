DELETE FROM CafInventory 
WHERE Category IN ('Produce', 'Protein', 'Dairy') 
AND Quantity > 500; 