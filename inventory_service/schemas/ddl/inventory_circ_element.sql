-- Create schema (if not exists)
CREATE SCHEMA IF NOT EXISTS inventory_db;

-- Table creation
CREATE TABLE inventory_db.inventory_circ_element (
    circuit_id VARCHAR(100),
    sequence_id VARCHAR(500),
    category VARCHAR(30),
    card_name VARCHAR(30),
    card_port VARCHAR(81),
    card_description VARCHAR(100),
    port_access VARCHAR(100),
    a_site VARCHAR(100),
    a_node_name VARCHAR(3100),
    a_ne_type VARCHAR(30),
    a_port_bandwidth VARCHAR(30),
    a_port_name VARCHAR(30),
    a_slot_number VARCHAR(30),
    a_shelf_number VARCHAR(12),
    z_site VARCHAR(100),
    z_node_name VARCHAR(3100),
    z_ne_type VARCHAR(30),
    z_port_bandwidth VARCHAR(30),
    z_port_name VARCHAR(30),
    z_slot_number VARCHAR(30),
    z_shelf_number VARCHAR(12),
    connectivity VARCHAR(30),
    circ_path_inst_id BIGINT,
    element_inst_id BIGINT
);

-- Index creation
CREATE INDEX inventory_circ_element_ix1 
ON inventory_db.inventory_circ_element (
    circuit_id
);
