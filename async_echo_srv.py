import asyncore
import socket
import threading

class EchoHandler(asyncore.dispatcher_with_send):
	def handle_read(self):
		data = self.recv(1024)
		if len(data) > 0:
			com = data.decode()
			print(com)
			self.sendall(data)
			if str(com) == 'close':
				print('close connection')
				self.close()
		else:
			print('close connection')
		

class EchoServer(asyncore.dispatcher):
 
    def __init__(self, host, port):
        asyncore.dispatcher.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.set_reuse_addr()
        self.bind((host, port))
        self.listen(10)
 
    def handle_accept(self):
        pair = self.accept()
        if pair is None:
            pass
        else:
            sock, addr = pair
            print ('connection from host: %s' % repr(addr))
            handler = EchoHandler(sock)
             
class AsyncEventLoop (threading.Thread):
 
    def run(self):
        asyncore.loop()

server = EchoServer('127.0.0.1', 2222)
evLoop = AsyncEventLoop()
evLoop.start()