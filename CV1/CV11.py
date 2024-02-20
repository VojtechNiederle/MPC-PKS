import struct
import socket
import time
#adresa a port prijemce (zada vyucujici)
host = "147.229.150.101"
port = 50000
#vytvoreni socketu
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#zaslani zpravy
for i in range(5):
    time.sleep(0.5)
    data = struct.pack("!LLL", i, 221342, 81)
    n = udp_socket.sendto(data,(host, port))     
    print("Odeslano {} byte\n".format(n))
#uzavreni socketu
udp_socket.close()