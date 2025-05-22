from typing import List, Optional
from pydantic import BaseModel, Field


class FTTHLinkInfo(BaseModel):
    """
    Model representing a single FTTH link service's detailed information.
    """
    serviceID: str = Field(..., description="Unique identifier of the service")
    serviceType: str = Field(..., description="Type of the service")
    serviceStatus: str = Field(..., description="Current status of the service")
    TBNo: str = Field(..., description="Terminal-box number")
    TBCLLI: str = Field(..., description="CLLI code of the terminal-box")
    TBLattitude: str = Field(..., description="Latitude of the terminal-box")
    TBLongitude: str = Field(..., description="Longitude of the terminal-box")
    TBPort: str = Field(..., description="Port on the terminal-box")
    TBOutputPort: str = Field(..., description="Output port on the terminal-box")
    TBFreePorts: List[str] = Field(..., description="List of free ports on the terminal-box")
    TBUtilizedPorts: List[str] = Field(..., description="List of utilized ports on the terminal-box")
    FDTNo: str = Field(..., description="FDT number")
    FDTSPlitterNo: str = Field(..., description="Splitter number at the FDT")
    FDTCLLI: str = Field(..., description="CLLI code of the FDT")
    FDTSPlitterOutputPort: str = Field(..., description="Splitter output port on the FDT")
    FDTLattitude: str = Field(..., description="Latitude of the FDT")
    FDTLongitude: str = Field(..., description="Longitude of the FDT")
    OLTName: str = Field(..., description="Name of the OLT")
    OLTModel: str = Field(..., description="Model of the OLT")
    OLTSLot: str = Field(..., description="Slot of the OLT")
    OLTUplinkPort: str = Field(..., description="Uplink port of the OLT")
    OLTPONPort: str = Field(..., description="PON port on the OLT")
    OLTIP: str = Field(..., description="IP address of the OLT")
    OLTAggregator: str = Field(..., description="Aggregator device connected to the OLT")
    OLTAggregatorIP: str = Field(..., description="IP address of that aggregator")
    OLTAggregatorPrimaryPort: str = Field(..., description="Primary port on the aggregator")
    OLTAggregatorStandbyPort: str = Field(..., description="Standby port on the aggregator")
    OLTDistrict: Optional[str] = Field(None, description="District of the OLT")
    OLTRegion: Optional[str] = Field(None, description="Region of the OLT")
    OLTVendor: Optional[str] = Field(None, description="Vendor of the OLT")
    OLTUpPort: Optional[str] = Field(None, description="Upstream port of the OLT")
    OLTSite: str = Field(..., description="Site code of the OLT")
    ODFID: str = Field(..., description="Identifier of the ODF")
    ODFInputPort: str = Field(..., description="Input port on the ODF")
    ODFOutputPort: str = Field(..., description="Output port on the ODF")
    ONTSerialNumber: str = Field(..., description="Serial number of the ONT")
    ONTModel: str = Field(..., description="Model of the ONT")
    ONTLastModifyDate: Optional[str] = Field(None, description="Last modification date of the ONT record")
    ONTID: str = Field(..., description="Identifier of the ONT")
    ONTDistrict: Optional[str] = Field(None, description="District of the ONT")
    ONTRegion: Optional[str] = Field(None, description="Region of the ONT")
    ONTDownStreamBandwidth: Optional[str] = Field(None, description="Downstream bandwidth of the ONT")
    ONTUpStreamBandwidth: Optional[str] = Field(None, description="Upstream bandwidth of the ONT")
    businessUnit: str = Field(..., description="Business unit responsible for the service")
    circuitPathName: str = Field(..., description="Name of the circuit path")
    EBUCircuitID: Optional[str] = Field(None, description="EBU circuit identifier")
    telephoneNumber: str = Field(..., description="Associated telephone number")

    class Config:
        schema_extra = {
            "example":             
            {
                "serviceID": "MRSTRD01-NZHARDU1568-1-FTTH_LINK 001",
                "serviceType": "FTTH_LINK",
                "serviceStatus": "LIVE",
                "TBNo": "NZHARDU1568",
                "TBCLLI": "NZHARDU1568",
                "TBLattitude": "24.7529548",
                "TBLongitude": "46.6991209",
                "TBPort": "BUILTIN-01",
                "TBOutputPort": "01",
                "TBFreePorts": ["28", "31"],
                "TBUtilizedPorts": ["01", "02", "03"],
                "FDTNo": "NZHARDU1568-1",
                "FDTSPlitterNo": "ESUL F121-1-6",
                "FDTCLLI": "NZHARDJ1173",
                "FDTSPlitterOutputPort": "ESUL F121-6-18-6-18",
                "FDTLattitude": "24.7519",
                "FDTLongitude": "46.7028",
                "OLTName": "116-00_MRSTRD00OLG",
                "OLTModel": "MA5680T",
                "OLTSLot": "01",
                "OLTUplinkPort": "2",
                "OLTPONPort": "1",
                "OLTIP": "10.72.96.131",
                "OLTAggregator": "PE-AggX16A-Wadi-789-31-2",
                "OLTAggregatorIP": "192.168.111.202",
                "OLTAggregatorPrimaryPort": "0-4",
                "OLTAggregatorStandbyPort": "0-6",
                "OLTDistrict": "",
                "OLTRegion": "",
                "OLTVendor": "",
                "OLTUpPort": "",
                "OLTSite": "SABDRR02",
                "ODFID": "00/02.03/07",
                "ODFInputPort": "15RX",
                "ODFOutputPort": "16TX",
                "ONTSerialNumber": "485754431FB29D11",
                "ONTModel": "HG8245",
                "ONTLastModifyDate": "",
                "ONTID": "MRSTRD00OLG",
                "ONTDistrict": "",
                "ONTRegion": "",
                "ONTDownStreamBandwidth": "",
                "ONTUpStreamBandwidth": "",
                "businessUnit": "hbu__domain",
                "circuitPathName": "MRSTRD01-NZHARDU1568-1-FTTH_LINK 001",
                "EBUCircuitID": "BISH09-BISH09 IP165",
                "telephoneNumber": "114554101"
            }
        }
