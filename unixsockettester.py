# Code to test the UNIX-domain socket communication

import socket
import time

sock = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)

sock.sendto(b"random garbage", "/tmp/gc9a01_socket")

time.sleep(500)

sock.sendto(b"more random garbage", "/tmp/gc9a01_socket")

# send random garbage every half second for 20 seconds

for _ in range(40):
    sock.sendto(b"random garbage", "/tmp/gc9a01_socket")
    time.sleep(0.5)
sock.close()



