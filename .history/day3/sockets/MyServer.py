import SocketServer
from time import ctime

class RequestHandler(SocketServer.BaseRequestHandler):

    def handle(self):
        self.data = ''
	while 1:
	    temp =  self.request.recv(8).strip()
	    if len(temp) < 8:
                self.data += temp
                break
	    elif len(temp):
                self.data += temp
            else:
		break

        print "%s %s %s" % (ctime(), self.client_address[0], self.data)
        #self.request.sendall(self.data.upper())
        self.request.sendall('aaa'.upper())

if __name__ == "__main__":
    HOST, PORT = "localhost", 9999
    server = SocketServer.TCPServer((HOST, PORT), RequestHandler)
    server.serve_forever()
