# ICMP Large Text Sender

This repository contains a Python program for sending large texts segmented into ICMP packets, with data encryption using `cryptography.fernet`.

## Description

The program takes a large text and splits it into segments, each of which is encrypted and sent as the payload of an ICMP packet. This can be useful for securely transmitting data over a network using ICMP packets.

## Requirements

- Python 3.x
- Scapy
- Cryptography

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/icmp-large-text-sender.git
   cd icmp-large-text-sender
2. Install the dependencies:
   ```bash
   pip install -r requirements.txt

## Usage

   Modify the shared key in the code to ensure it is the same on both the sending and receiving programs.

   Run the program:

   ### python icmp_sender.py

## Code

```python
from scapy.all import IP, ICMP, Raw, send
from cryptography.fernet import Fernet
import time

# Shared key (must be the same on both programs)
key = b'+tL+tvH+OM9GF8l9f4BVEguX4EOG8Q7W42A3zHDyPmI='

def encrypt_data(data, key):
    fernet = Fernet(key)
    return fernet.encrypt(data)

def build_icmp_packet(data, key, seq):
    encrypted_data = encrypt_data(data, key)
    packet = IP(dst="127.0.0.1") / ICMP(type=8, seq=seq) / Raw(load=encrypted_data)
    return packet

def send_large_text(text, key):
    max_payload_size = 1400  # Maximum payload size for each ICMP packet
    seq = 1
    for i in range(0, len(text), max_payload_size):
        chunk = text[i:i+max_payload_size]
        icmp_packet = build_icmp_packet(chunk.encode(), key, seq)
        send(icmp_packet)
        print(f"ICMP packet sent with seq {seq}")
        seq += 1
        time.sleep(0.1)  # Add a short delay to avoid network issues

if __name__ == "__main__":
    large_text = "This is a very large text that needs to be sent in segments via ICMP packets.DHIAIAIAIAIIAI"
    send_large_text(large_text, key)


