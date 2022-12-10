from abc import *

from app.model.Protocol.Protocol import Protocol


class IReceiver(metaclass=ABCMeta):
    @abstractmethod
    def doAction(self):
        ...


class ProtocolReceiver(IReceiver):
    
    protocol : Protocol = None
    
    def __init__(self, _protocol : Protocol) -> None:
        super().__init__()
        self.protocol = _protocol

    def doAction(self):
        

        print("TCPReceiver")
