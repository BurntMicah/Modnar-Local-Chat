import thread
import socket
import time
#Client sends
#Server Recieves  
localip=([(s.connect(('8.8.8.8', 80)), s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]][0][1])           
nodes=[]
blockednodes=[]
begip=localip.split(".")[0]+"."+localip.split(".")[1]+"."
endip=localip.split(".")[2]+"."+localip.split(".")[3]
print "Modnar 2.0"
print "Connected to Local Network "+begip
print "You are Computer " + endip


def server():#Looks for inoming TCP connections and prints message along with computer
 s = socket.socket()         # Create a socket object
 s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
 s.bind(("", 12233))
 while 1:
   s.listen(1)
   conn, addr = s.accept()
   data = conn.recv(1024)
   if not(addr[0] in blockednodes):
    print "\nComputer "+addr[0].split(".")[2]+"."+addr[3].split(".")[3]+": "+data
   conn.close()

def client():#Sends message to all ip addresses in nodes[]
 localip=([(s.connect(('8.8.8.8', 80)), s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]][0][1])     
 begip=localip.split(".")[0]+"."+localip.split(".")[1]
 endip=localip.split(".")[2]+"."+localip.split(".")[3]
 while 1:
  message = raw_input()
  if message[0]=='/':
   command = message.split(" ")[0][1:]
   if command=="block":
    blockednodes.append(begip+'.'+message.split(" ")[1])
    Else:
   time.sleep(0.1)
   for i in range(0, len(nodes)):
    s = socket.socket()         # Create a socket object
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    try:
     s.connect((nodes[i], 12233))
     s.sendall(message)
    except:
     try:
      print nodes[i].split(".")[2]+"."+nodes[i].split(".")[3]+" has gone offline"
      nodes.remove(nodes[i])
    s.close()


def handserver():#Accepts incoming handshakes; stores ipaddress and responds with ipaddress
 UDP_IP = socket.gethostname()
 UDP_PORT = 12333
 sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
 sock.bind(("", UDP_PORT))
 localip=([(s.connect(('8.8.8.8', 80)), s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]][0][1])
 while 1:
  data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
  if not(data in nodes) and data!=localip:
   print data+" discovered you!"
   nodes.append(data)
   handclient(data)

def handclient(value):#Searches for computers by spitting out ipaddresss via UDP to a range of ipaddress
 localip= ([(s.connect(('8.8.8.8', 80)), s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]][0][1])           
 begip=localip.split(".")[0]+"."+localip.split(".")[1]+"."
 if(value==False):
  while 1:
   for j in range(0,5):
    for i in range(1,255):
     sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
     sock.sendto(localip, (begip+str(j)+"."+str(i), 12333))
   time.sleep(4)
 else:
  UDP_IP = value
  UDP_PORT = 12333
  sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
  sock.sendto(localip, (UDP_IP, UDP_PORT))


thread.start_new_thread(handclient, (False,))
thread.start_new_thread(handserver, ())
thread.start_new_thread(server, ())
#while 1:
client()
