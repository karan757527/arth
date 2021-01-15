import socket
import threading
import os

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

me=input("Your Name:")
ip=input("Enter your ip:")
name=input("Chat with:")
ip2=input(f"Enter {name}'s ip:")


s.bind((ip,2345))

os.system("cls")
print("-"*60)
print("SecureGram".center(60))
print(f"This is {me}'s Screen".center(60))
print("-"*60)


def send():
    while True:
        x=bool(input())
        msg="x"
        if x==False:
            msg=input(f'{me}-->'.rjust(55,' '))
            s.sendto(msg.encode() , (ip2 , 1234) )
            x=None
        if msg.lower()=='bye':
            break


def recv():
    
    while True:
        x=s.recvfrom(1024)
        data=x[0].decode()
        print(f'\n{name}-->{data}\n')
        if data=='bye':
            break
            #quit()
        
            

     
        
x1 = threading.Thread(target=send)
x2 = threading.Thread(target=recv)

x1.start()
x2.start()


