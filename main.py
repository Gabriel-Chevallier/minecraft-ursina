import socket
s = socket.socket(); s.bind(('0.0.0.0', 12345)); s.listen(2); c1, c2 = s.accept(), s.accept()
while True: c2[0].send(c1[0].recv(1024)); c1[0].send(c2[0].recv(1024))
