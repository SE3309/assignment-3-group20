CREATE VIEW InventorySummaryByResidence AS
SELECT 
    Residence_Name,
    Category,
    SUM(Quantity) AS Total_Quantity
FROM 
    cafinventory
GROUP BY 
    Residence_Name, Category;