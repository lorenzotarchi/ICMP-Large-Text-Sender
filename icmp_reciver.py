from scapy.all import sniff, IP, ICMP, Raw
from cryptography.fernet import Fernet

# Shared key (must be the same on both programs)
key = b'+tL+tvH+OM9GF8l9f4BVEguX4EOG8Q7W42A3zHDyPmI='

def decrypt_data(encrypted_data, key):
    fernet = Fernet(key)
    return fernet.decrypt(encrypted_data)

def packet_callback(packet):
    global received_data
    if IP in packet and ICMP in packet and packet[ICMP].type == 8:
        if Raw in packet:
            encrypted_payload = packet[Raw].load
            try:
                payload = decrypt_data(encrypted_payload, key)
                seq = packet[ICMP].seq
                if seq not in received_data:
                    received_data[seq] = payload
                    print(f"Received packet with seq {seq} and decrypted payload: {payload}")
            except Exception as e:
              print(f"Error decrypting payload: {e}")
        else:
            print("Received ICMP packet without payload")

if __name__ == "__main__":
    received_data = {}
    print("Listening for ICMP Echo Request...")
    sniff(filter="icmp and icmp[icmptype] == icmp-echo", prn=packet_callback, iface="lo")

    # Wait for all packet
    time.sleep(5)

    full_text = b"".join([received_data[seq] for seq in sorted(received_data)])
    print(f"Recived Text : {full_text.decode()}")

    with open("received_text.txt", "wb") as file:
        file.write(full_text)
