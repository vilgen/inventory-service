from pydantic import Field, RootModel
from inventory_service.models.dto.copper import Copper


class CopperListResponse(RootModel):
    root: list[Copper] = Field(default_factory=list, description="List of copper service information items")

    class Config:
        schema_extra = {
            "example": 
                 [
                    {
                        "pathname": "MNAREAAT-FSLY 076:0146-COPPER_LINK 5116307",
                        "category": "COPPER_LINK",
                        "voiceEquipmentType": "MSAN",
                        "voiceExchangeID": "MNAREAAT-MSAN FSY9A/00001-0",
                        "voiceEquipmentCLLI": "Area PP#699/1 (E076)",
                        "voiceSlot": "06",
                        "voicePort": "19",
                        "voiceAccessPortID": "MNAREAAT-MSAN FSY9A/00001-0",
                        "voiceEN": "N0000100019",
                        "voiceNodeName": "M302-32-306_AFSY9",
                        "voiceNodeUpSlot": "",
                        "voiceNodeUpPort": "",
                        "voiceNodeIPAddress": "",
                        "voiceV5ID": "",
                        "voiceSwitchID": "FSY9A",
                        "voiceHostExchangeSwitch": "FSY11",
                        "voiceSwitchType": "NGN Huawei MSAN",
                        "voiceSwitchName": "NGN PRINCE MOHD__302-32-306",
                        "voiceNMSJVCode": "",
                        "voiceSwitchModel": "",
                        "voiceAggName": "",
                        "voiceAggCLLI": "",
                        "voiceAggIP": "",
                        "voiceAggPrimaryPort": "",
                        "voiceAggStandbyPort": "",
                        "dataEquipmentType": "MDF",
                        "dataNodeName": "FSY9A-001",
                        "dataNodeUpSlot": "",
                        "dataNodeUpPort": "",
                        "dataNodeIPAddress": "",
                        "dataEquipmentCLLI": "MNAREAAT",
                        "dataSlot": "001",
                        "dataPort": "015",
                        "dataAccessPortID": "",
                        "dataEN": "",
                        "dataEL": "",
                        "copperCabinet": ["P-1-10", "S-145-154"],
                        "cabinetStripPairDPPair": "",
                        "primaryStripCable": "FSY9A E01-00002",
                        "secondaryStripCable": "FSLY 076:0146",
                        "dataV5ID": "",
                        "dataExchangeID": "",
                        "dataHostExchangeSwitch": "",
                        "dataSwitchID": "",
                        "dataSwitchType": "",
                        "dataSwitchName": "",
                        "dataNMSJVCode": "",
                        "dataAggName": "",
                        "dataAggCLLI": "",
                        "dataAggIP": "",
                        "dataAggPrimaryPort": "",
                        "dataAggStandbyPort": "",
                        "copperPlateID": "FSLY 076:0146",
                        "plateLatitude": "",
                        "plateIDLongitude": "",
                        "domainName": "hbu__domain",
                        "plateDistrict": "",
                        "plateRegion": "",
                        "plateExchange": "",
                        "treatmentPriority": "",
                        "MDFName": "",
                        "MDFSlot": "",
                        "MDFPort": "",
                        "classA": "",
                        "telephoneNumber": "138110554"
                    }
                ]
            }