#!/usr/bin/python

import socket
import os
import sys

def help():
    print('Usage: grabber.py [ip address] [port]')
    sys.exit(1)

def main():
    sock = socket.socket()

    if len(sys.argv) < 3:
        help()

    ip = sys.argv[1]
    try:
        port = int(sys.argv[2])
    except ValueError as err:
        print(f'Error port must be a valid number! {err}')
        sys.exit(1)

    try:
        sock.connect((ip, port))
        banner = sock.recv(1024)
        print(f'{ip}: {banner}')
    except ConnectionRefusedError:
        print(f'[-] {ip}:{port}: Connection refused')
        sys.exit(1)

if __name__ == '__main__':
    main()
