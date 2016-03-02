import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost', 2222))
for x in xrange(1,10):
	s.send('q')
data = s.recv(1024)
s.send('close')
for y in xrange(x):
	s.send('hello')
s.close()
print data