import socket


conn_udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

conn_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


conn_tcp.bind((socket.gethostname(), 9000))

print(conn_tcp.recvfrom(1024))