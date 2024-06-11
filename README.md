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
   Modify the `large_text` variable to contain the text you want to send.

   1. Run the program:
      ```bash
      pyhton3 icmp_reciver.py
      python icmp_sender.py

## Code Explanation

1. The program imports necessary modules: `scapy.all`, `cryptography.fernet`, and `time`.
2. It defines a function `encrypt_data(data, key)` to encrypt the data using the Fernet symmetric encryption algorithm.
3. The `build_icmp_packet(data, key, seq)` function constructs an ICMP packet with the encrypted data.
4. The `send_large_text(text, key)` function sends the large text in segments via ICMP packets.
5. A short delay is added between packet transmissions to avoid network issues.

**Note**: It is not necessary to use a specific receiver, as you can use the tcpdump -X command to view the encrypted output.
