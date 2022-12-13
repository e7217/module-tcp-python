import struct
from dataclasses import dataclass, field


@dataclass 
class Protocol:

    """
    str : 1 byte
    data : little endian 4 byte
    etx : 1 byte
    """

    stx : bytes = b"\x02"
    data : bytes = b"\x00\x00\x00\x00"
    etx : bytes= b"\x03"
    
    def get_data(self) -> str:
        return struct.unpack('<i', self.data)[0]