#!/usr/bin/env python3
import re
from pathlib import Path

# Mapping from export SQL file to the correct field names (from DDL)
EXPORT_TO_FIELDS = {
    'circ_elem_export.sql': [
        'circuit_id', 'sequence_id', 'category', 'card_name', 'card_port', 'card_description', 'port_access',
        'a_site', 'a_node_name', 'a_ne_type', 'a_port_bandwidth', 'a_port_name', 'a_slot_number', 'a_shelf_number',
        'z_site', 'z_node_name', 'z_ne_type', 'z_port_bandwidth', 'z_port_name', 'z_slot_number', 'z_shelf_number',
        'connectivity', 'circ_path_inst_id', 'element_inst_id'
    ],
    'circuit_export.sql': [
        'name', 'revision', 'category', 'status', 'topology', 'bandwidth', 'a_site', 'a_ne_type', 'a_node_name',
        'a_port_bandwidth', 'a_port_name', 'a_slot_number', 'a_shelf_number', 'z_site', 'z_ne_type', 'z_node_name',
        'z_port_bandwidth', 'z_port_name', 'z_slot_number', 'z_shelf_number', 'last_mod_ts'
    ],
    'copper_export.sql': [
        'path_name', 'category', 'voice_equipment_type', 'voice_exchange_id', 'voice_equipment_clli', 'voice_slot',
        'voice_port', 'voice_access_port_id', 'voice_en', 'voice_node_name', 'voice_node_up_slot', 'voice_node_up_port',
        'voice_node_ip_address', 'voice_v5_id', 'voice_switch_id', 'voice_host_exchange_switch', 'voice_switch_type',
        'voice_switch_name', 'voice_nms_jv_code', 'voice_switch_model', 'voice_agg_name', 'voice_agg_clli',
        'voice_agg_ip', 'voice_agg_primary_port', 'voice_agg_standby_port', 'data_equipment_type', 'data_node_name',
        'data_node_up_slot', 'data_node_up_port', 'data_node_ip_address', 'data_equipment_clli', 'data_slot',
        'data_port', 'data_access_port_id', 'data_en', 'data_el', 'copper_cabinet', 'cabinet_strip_pair_dp_pair',
        'primary_strip_cable', 'secondary_strip_cable', 'data_v5_id', 'data_exchange_id', 'data_host_exchange_switch',
        'data_switch_id', 'data_switch_type', 'data_switch_name', 'data_nms_jv_code', 'data_agg_name', 'data_agg_clli',
        'data_agg_ip', 'data_agg_primary_port', 'data_agg_standby_port', 'copper_plate_id', 'plate_latitude',
        'plate_id_longitude', 'domain_name', 'plate_district', 'plate_region', 'plate_exchange', 'treatment_priority',
        'mdf_name', 'mdf_slot', 'mdf_port', 'class_a', 'telephone_number', 'last_mod_ts', 'circuit_path_name'
    ],
    'cross_conn_export.sql': [
        'a_site_equipment_name', 'a_site_equipment_type', 'a_site_equipment_vendor', 'a_site_ctp_id', 'a_site_shelf',
        'a_site_slot', 'a_site_port', 'z_site_equipment_name', 'z_site_equipment_type', 'z_site_equipment_vendor',
        'z_site_ctp_id', 'z_site_shelf', 'z_site_slot', 'z_site_port', 'last_mod_ts', 'type'
    ],
    'equipment_export.sql': [
        'last_mod_ts', 'type', 'port_status', 'port_number', 'card_status', 'card_type', 'slot_no', 'site_clli',
        'site_number', 'inband_ip', 'last_modified_time', 'equipment_model', 'equipment_vendor', 'status',
        'equipment_type', 'shelf_number', 'equipment_name', 'equip_inst_id', 'p_last_mod_ts'
    ],
    'fttx_export.sql': [
        'service_id', 'service_type', 'service_status', 'tb_no', 'tb_clli', 'tb_lattitude', 'tb_longitude', 'tb_port',
        'tb_output_port', 'tb_free_ports', 'tb_utilized_ports', 'fdt_no', 'fdt_splitter_no', 'fdt_clli',
        'fdt_splitter_output_port', 'fdt_lattitude', 'fdt_longitude', 'olt_name', 'olt_model', 'olt_slot',
        'olt_uplink_port', 'olt_pon_port', 'olt_ip', 'olt_aggregator', 'olt_aggregator_ip', 'olt_aggregator_primary_port',
        'olt_aggregator_standby_port', 'olt_district', 'olt_region', 'olt_vendor', 'olt_up_port', 'olt_site', 'odf_id',
        'odf_input_port', 'odf_output_port', 'ont_serial_number', 'ont_model', 'ont_last_modify_date', 'ont_id',
        'ont_district', 'ont_region', 'ont_downstream_bandwidth', 'ont_upstream_bandwidth', 'business_unit',
        'ebu_circuit_id', 'telephone_number', 'circuit_path_name', 'last_mod_ts'
    ],
}

def build_column_map(field_list):
    """Build a mapping from uppercase/stripped column names to snake_case field names."""
    col_map = {}
    for field in field_list:
        col_map[field.upper().replace('_', '')] = field
    return col_map

def convert_sql_file(file_path, col_map):
    print(f"Converting {file_path}...")
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    new_lines = []
    for line in lines:
        if line.startswith('REM INSERTING') or line.startswith('SET DEFINE OFF;'):
            new_lines.append(line)
        else:
             if not line.strip().startswith('Insert into EXPORT_TABLE'):
                 line = 'Insert into EXPORT_TABLE ' + line
             new_lines.append(line)
    content = ''.join(new_lines)
    def replace_columns(match):
        prefix = match.group(1)
        columns = match.group(2)
        new_columns = []
        for col in columns.split(','):
             orig = col.strip()
             key = orig.upper().replace('_', '')
             new_col = col_map.get(key, orig.lower())
             new_columns.append(new_col)
        return prefix + '(' + ', '.join(new_columns) + ')'
    new_content = re.sub(r'(Insert\s+into\s+[^(]+)\(([^)]+)\)', replace_columns, content)
    with open(file_path, 'w', encoding='utf-8') as f:
         f.write(new_content)
    print(f"Converted {file_path}")

def main():
    sql_dir = Path('data/sql')
    sql_file = sql_dir / 'fttx_export.sql'
    field_list = EXPORT_TO_FIELDS.get('fttx_export.sql')
    if field_list and sql_file.exists():
        col_map = build_column_map(field_list)
        convert_sql_file(sql_file, col_map)
    else:
        print(f"No field mapping or file not found for fttx_export.sql, skipping.")

if __name__ == '__main__':
    main() 