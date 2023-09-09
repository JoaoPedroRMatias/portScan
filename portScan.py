#!/usr/bin/python3

import pyfiglet
import socket
from ports import PORTS
from tqdm import tqdm

ascii_banner = pyfiglet.figlet_format("PORT SCAN", font='slant')
print(ascii_banner)

host=input("IP / DOMAIN: ")


def port_scan(host):
    ports = PORTS

    for p in tqdm(ports):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)

        if s.connect_ex((host,p)) == 0:
            print(f"Porta {p} [TCP] aberta")


try:
    port_scan(host)

except:
    print("ERRO: cheque se os argumentos estão corretos")