from pymodbus.client import ModbusTcpClient

with ModbusTcpClient('127.0.0.1', port=5000) as client :
    # client.write_coil(1, True)
    result = client.read_holding_registers(3, 1)
    print(result.bits[0])
    client.close()