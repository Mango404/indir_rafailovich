import socket

server_address = ('192.168.1.35', 5400)#CompudahterArseniya

while True:
    msg = input('-')
    bin_msg = bytes(msg, 'utf-8')

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client.connect(server_address)
        client.sendall(bin_msg)
        data = client.recv(1024)
        print(data.decode('utf-8'))
    except:
        print('not connected')
    finally:
        client.close()
