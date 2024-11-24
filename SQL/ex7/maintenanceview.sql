CREATE VIEW MaintenanceInfo AS
SELECT 
    maintenancerequest.Maintenance_Request_Number,
    maintenancerequest.Maintenance_Type,
    maintenancerequest.Status,
    maintenancerequest.Student_ID
FROM 
    maintenancerequest