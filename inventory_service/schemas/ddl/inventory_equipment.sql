-- Create schema (if not exists)
CREATE SCHEMA IF NOT EXISTS inventory_db;

-- Table creation
CREATE TABLE inventory_db.inventory_equipment (
    last_mod_ts TIMESTAMP,
    type VARCHAR(30),
    port_status VARCHAR(20),
    port_number VARCHAR(50),
    card_status VARCHAR(20),
    card_type VARCHAR(50),
    slot_no VARCHAR(30),
    site_clli VARCHAR(100),
    site_number VARCHAR(30),
    inband_ip VARCHAR(3100),
    last_modified_time TIMESTAMP,
    equipment_model VARCHAR(30),
    equipment_vendor VARCHAR(40),
    status VARCHAR(20),
    equipment_type VARCHAR(30),
    shelf_number VARCHAR(20),
    equipment_name VARCHAR(200),
    equip_inst_id BIGINT,
    p_last_mod_ts TIMESTAMP
);

-- Index creation
CREATE INDEX inventory_equipment_ix1 
ON inventory_db.inventory_equipment (
    last_mod_ts DESC,
    p_last_mod_ts DESC,
    equipment_type
);
