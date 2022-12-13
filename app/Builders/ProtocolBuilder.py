from abc import *
import struct

from model.Protocol import Protocol


class IProtocolBuilder(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self, payload: list[bytes]):
        ...

    @abstractmethod
    def build(self):
        ...

    @abstractmethod
    def Validate(self) -> bool:
        ...

class ProtocolBuilder(IProtocolBuilder):
    def __init__(self, payload: bytes):
        
        self.stx = payload[0]
        self.data = payload[1:-1]
        self.etx = payload[-1]

    def build(self):
        return Protocol(self.stx, self.data, self.etx)

    def Validate(self) -> bool:
        if self.stx == struct.unpack("<b", b"\x02")[0] and self.etx == struct.unpack("<b", b"\x03")[0]:
            return True
        return False