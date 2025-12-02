#!/usr/bin/env python3
# Code to test the UNIX-domain socket communication

import socket
import time
from pathlib import Path


SOCKET_PATH = Path("/tmp/gc9a01_socket")


def wait_for_socket(path: Path, timeout: float = 20.0, interval: float = 0.25) -> None:
    """Block until the server creates the UNIX DGRAM socket file."""
    deadline = time.monotonic() + timeout
    while not path.exists():
        if time.monotonic() > deadline:
            raise FileNotFoundError(f"Socket path not found within {timeout}s: {path}")
        time.sleep(interval)


def send_garbage() -> None:
    wait_for_socket(SOCKET_PATH)
    sock = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)
    try:
        # send an initial probe, then keep streaming until interrupted
        sock.sendto(b"random garbage", str(SOCKET_PATH))
        while True:
            sock.sendto(b"random garbage", str(SOCKET_PATH))
            time.sleep(1)
    finally:
        sock.close()


if __name__ == "__main__":
    send_garbage()

