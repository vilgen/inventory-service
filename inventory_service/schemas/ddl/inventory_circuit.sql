-- Create schema (if not exists)
CREATE SCHEMA IF NOT EXISTS inventory_db;

-- Table creation
CREATE TABLE inventory_db.inventory_circuit (
    name VARCHAR(100) NOT NULL,
    revision INTEGER,
    category VARCHAR(30) NOT NULL,
    status VARCHAR(20),
    topology CHAR(1),
    bandwidth VARCHAR(30),
    a_site VARCHAR(100),
    a_ne_type VARCHAR(30),
    a_node_name VARCHAR(3100),
    a_port_bandwidth VARCHAR(30),
    a_port_name VARCHAR(50),
    a_slot_number VARCHAR(30),
    a_shelf_number VARCHAR(12),
    z_site VARCHAR(100),
    z_ne_type VARCHAR(30),
    z_node_name VARCHAR(3100),
    z_port_bandwidth VARCHAR(30),
    z_port_name VARCHAR(50),
    z_slot_number VARCHAR(30),
    z_shelf_number VARCHAR(12),
    last_mod_ts TIMESTAMP
);
