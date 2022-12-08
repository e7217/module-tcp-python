@dataclass 
class Protocol:
    stx : str = "\x02"
    data : str = ""
    etx : str = "\x03"