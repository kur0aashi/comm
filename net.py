from networkk import Server
from networkk import Party
import threading
print("welcome please choose if you want to host or join")
print("\n1.PRESS -H- FOR HOST")
print("\n2.PRESS -J- FOR JOIN")
choice=input('>>')
if choice=='h' or choice=='H':
    sv=Server()
    print("waiting for client to message first:")
    name=sv.receive()
    print(f'connected with {name}')
    myname=input("set your name: ")
    sv.send(myname)
    def printMsg():
        while True:
            msg=sv.receive()
            if msg:
                print(name+':'+msg)
                print('*'*50)
    showMessages=threading.Thread(target=printMsg)
    showMessages.start()
    while True:

        tosend=input()
        print('*'*50)
        if tosend:
            sv.send(tosend)
elif choice=='j' or choice=="J":
    cl=Party()
    ip=input('Enter Ip of the host:')
    port=9999
    cl.setaddr(ip.strip(),port)
    myname=input("Your name:")
    cl.send(myname)
    name=cl.receive()
    print('conected with '+name)
    def printMsg():
        while True:
            msg=cl.receive()
            if msg:
                print(name+':'+msg)
                print('*'*50)
    showMessages=threading.Thread(target=printMsg)
    showMessages.start()
    while True:
        
        tosend=input()
        print('*'*50)
        cl.send(tosend)
else:
    print("Invalid choice")
