""" a quick demo of daytime service """
import time
import socket
import commands
HOST = socket.gethostname()  # Symbolic name meaning the local host
PORT = 32132

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to address - the socket becomes access able  
s.bind((HOST, PORT))
s.listen(5)   
# Listen for connections made to the socket, 
# Its argumnets specifies the maximum number of queued connections (0, 5)
# Accept a connection   
while 1:
#creating the socket object 
  try:
    conn, addr = s.accept()
    # here 
    #	conn - client socket object 
    #   addr - (ip-addr, port of the client socket) 
    print 'Connected by', addr, ":", conn 
    #conn.send(commands.getoutput('date'))
    conn.send(time.ctime())
    conn.close()
  except Exception ,e :
    #conn.close()
    print e

