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
