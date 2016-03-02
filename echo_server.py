import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 2222))
s.listen(1)
while  True:
	conn, addr = s.accept()
	print 'connection from: ' , addr 
	while True:
		data = conn.recv(1024)
		print data
		if data == 'close':break
		if not data: break
		conn.send(data)
	print 'connection closed'
	conn.close() 