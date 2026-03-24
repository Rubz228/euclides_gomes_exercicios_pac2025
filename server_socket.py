import socket

servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

servidor.bind(('127.0.0.1',12340))

servidor.listen(1)

print("Servidor pronto. À espera do cliente...")

