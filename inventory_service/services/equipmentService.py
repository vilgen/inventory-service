# services/equipment_service.py
from datetime import datetime
from uuid import UUID

from ..models.getEquipmentListResponse import Equipment, EquipmentType, Port, Slot


class EquipmentService:
    """
    Service for equipment-related operations.
    """

    async def get_equipment_list(
        self,
        equipment_type: EquipmentType,
        start_time: datetime,
        end_time: datetime,
        client_msg_ref: UUID,
        correlation_ref: UUID
    ) -> list[Equipment]:
        """
        Fetch equipment list based on type and time range.
        """
        # Mock implementation
        mock_port1 = Port(portNumber="00", portStatus="Available")
        mock_port2 = Port(portNumber="01", portStatus="Available")

        mock_slot1 = Slot(
            slotNo="02",
            cardType="IPMB",
            cardStatus="ASSIGNED",
            ports=[mock_port1]
        )

        mock_slot2 = Slot(
            slotNo="03",
            cardType="IPMB",
            cardStatus="ASSIGNED",
            ports=[mock_port2]
        )

        mock_equipment = Equipment(
            equipmentName=f"108-00-310-{equipment_type.value} MATB 1",
            shelfNumber="1",
            equipmentType=equipment_type.value,
            equipmentStatus="INSTALLED",
            equipmentVendor="HUAWEI",
            equipmentModel="UA5000",
            lastModifiedTime="18-APR-2023",
            inBandIP="10.11.10.1",
            siteNumber="101-00-000",
            siteCLLI="MURBRD00",
            slots=[mock_slot1, mock_slot2]
        )



        return [mock_equipment]
