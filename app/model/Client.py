import socket
import time
from dataclasses import dataclass
from queue import Queue
from threading import Thread

from Builders.ProtocolBuilder import IProtocolBuilder, ProtocolBuilder
from model.Protocol import Protocol


@dataclass
class ClientSocket:

    id : int = 0
    sock : socket.socket = None
    addr : tuple = None
    __value_queue : Queue = Queue()
    __handler : IProtocolBuilder = ProtocolBuilder

    def start(self) -> None:
        t1 = Thread(target=self.recv_handler)
        t2 = Thread(target=self.send_handler)
        t1.start()
        t2.start()

    def parse_handler(self, payload: bytes) -> str:
        
        # 데이터를 빌더에 연결
        _protocol_builder = self.__handler(payload)
        # 빌더에서 프로토콜 생성
        _protocol : Protocol = _protocol_builder.build()
        # 프로토콜 리턴 값
        return _protocol.get_data()

    def recv_handler(self) -> None:
        try:
            while True:
                # message = self.sock.recv(1024).decode()
                _message = self.sock.recv(1024)
                _value = self.parse_handler(_message)
                self.__value_queue.put(_message)
                if _message:
                    print(f"receive from cl ient{self.id}: {_message}, value: {_value}")
        except ConnectionAbortedError as e:
            print(f"Client{self.id} has disconnected")
            self.sock.close()

    def send_handler(self) -> None:
        try:
            while True:
                time.sleep(1) 
                self.sock.send(f"Hello Client{self.id}".encode())
        except OSError as e:
            print(f"Client{self.id} has disconnected")
            self.sock.close()