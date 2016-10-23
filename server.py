import socket               # Import socket module

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

localHost = socket.gethostname()
port = 12345

s.bind((localHost,port))

s.listen(5)

while True:
    conn,add = s.accept()
    print('Got connection from ', add)
    conn.send(b'Thanks for connectiong')
    conn.close()
            # Close the connection
