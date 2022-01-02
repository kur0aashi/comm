from contextlib import nullcontext
import socket
class Server:    
    def __init__(self):
        self.s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        self.port=9999
        self.format='utf-8'
        self.server='localhost'    
        self.s.bind(('localhost',self.port))
        print("server started")
        self.movecount=0
        self.turn='receive'
        self.clientaddr=None
    def setclient(self,addr):
        self.clientaddr=addr
    def getData(self):
        return self.received
    def setData(self,data):
        self.tosend=data

    def receive(self):
        data,addr=self.s.recvfrom(32)
        self.setclient(addr)
        return data.decode(self.format)

    def send(self,msg):
        self.s.sendto(msg.encode(self.format),self.clientaddr)
class Party:
    def __init__(self):
        self.c=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        self.format='utf-8' 
        self.serveraddr=None

    def setaddr(self,ip,port):
        self.serveraddr=(ip,port)
    def send(self,msg):
        self.c.sendto(msg.encode(self.format),self.serveraddr)
    def receive(self):
        msg,addr=self.c.recvfrom(32)
        return msg.decode(self.format)

