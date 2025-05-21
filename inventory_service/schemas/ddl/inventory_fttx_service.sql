-- Create schema (if not exists)
CREATE SCHEMA IF NOT EXISTS inventory_db;

-- Table creation
CREATE TABLE inventory_db.inventory_fttx_service (
    service_id VARCHAR(100),
    service_type VARCHAR(30),
    service_status VARCHAR(20),
    tb_no VARCHAR(3100),
    tb_clli VARCHAR(3100),
    tb_lattitude VARCHAR(20),
    tb_longitude VARCHAR(20),
    tb_port VARCHAR(3100),
    tb_output_port VARCHAR(3100),
    tb_free_ports VARCHAR(4000),
    tb_utilized_ports VARCHAR(4000),
    fdt_no VARCHAR(4000),
    fdt_splitter_no VARCHAR(3100),
    fdt_clli VARCHAR(3100),
    fdt_splitter_output_port VARCHAR(3100),
    fdt_lattitude VARCHAR(3100),
    fdt_longitude VARCHAR(3100),
    olt_name VARCHAR(3100),
    olt_model VARCHAR(30),
    olt_slot VARCHAR(3100),
    olt_uplink_port VARCHAR(100),
    olt_pon_port VARCHAR(3100),
    olt_ip VARCHAR(3100),
    olt_aggregator VARCHAR(3100),
    olt_aggregator_ip VARCHAR(3100),
    olt_aggregator_primary_port VARCHAR(4000),
    olt_aggregator_standby_port VARCHAR(4000),
    olt_district VARCHAR(3100),
    olt_region VARCHAR(3100),
    olt_vendor VARCHAR(40),
    olt_up_port VARCHAR(50),
    olt_site VARCHAR(100),
    odf_id VARCHAR(4000),
    odf_input_port VARCHAR(4000),
    odf_output_port VARCHAR(4000),
    ont_serial_number VARCHAR(30),
    ont_model VARCHAR(30),
    ont_last_modify_date TIMESTAMP,
    ont_id VARCHAR(3100),
    ont_district VARCHAR(3100),
    ont_region VARCHAR(3100),
    ont_downstream_bandwidth VARCHAR(3100),
    ont_upstream_bandwidth VARCHAR(3100),
    business_unit TEXT,
    ebu_circuit_id VARCHAR(200),
    telephone_number VARCHAR(255),
    circuit_path_name VARCHAR(100),
    last_mod_ts TIMESTAMP
);

-- Index creation
CREATE INDEX inventory_fttx_service_ix1 
ON inventory_db.inventory_fttx_service (last_mod_ts DESC);
