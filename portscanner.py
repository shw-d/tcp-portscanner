import socket

host = str(input("Enter the host to be scanned: ")) #hostname(www)
ip = socket.gethostbyname(host)     

print(ip)  #prints IP address of the host

while 1:
	port = int(input("Enter the port: "))	#port no to be scanned
	
	try:
		sock = socket.socket()			
		res = sock.connect((ip, port))
		print("Port {}: Open")
		sock.close()
	except:
		print("Port {}: Closed")
	
print("Port scanning complete")