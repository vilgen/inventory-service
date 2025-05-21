-- Create schema (if not exists)
CREATE SCHEMA IF NOT EXISTS inventory_db;

-- Table creation
CREATE TABLE inventory_db.inventory_cross_connection (
    a_site_equipment_name VARCHAR(3100),
    a_site_equipment_type VARCHAR(30),
    a_site_equipment_vendor VARCHAR(40),
    a_site_ctp_id VARCHAR(30),
    a_site_shelf VARCHAR(12),
    a_site_slot VARCHAR(30),
    a_site_port VARCHAR(50),
    z_site_equipment_name VARCHAR(3100),
    z_site_equipment_type VARCHAR(30),
    z_site_equipment_vendor VARCHAR(40),
    z_site_ctp_id VARCHAR(30),
    z_site_shelf VARCHAR(12),
    z_site_slot VARCHAR(30),
    z_site_port VARCHAR(50),
    last_mod_ts TIMESTAMP,
    type VARCHAR(30)
);

-- Index creation
CREATE INDEX inventory_cross_connection_ix1 
ON inventory_db.inventory_cross_connection (
    last_mod_ts DESC,
    type
);
