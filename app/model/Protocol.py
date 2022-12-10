from dataclasses import dataclass, field


@dataclass 
class Protocol:
    stx : bytes = hex(2).encode()
    data : list[bytes] = field(default_factory=list)
    etx : bytes = hex(3).encode()

    def get_string(self) -> str:
        return self.data.decode()