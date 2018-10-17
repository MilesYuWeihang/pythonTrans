import socket
port = 5555
host = '10.0.1.26'
print (host)
# port = 5000
address = (host, port)

socket01 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

socket01.bind(address)
socket01.listen(1)  # listen(backlog)
print('Socket Startup')
pic = ["a0.jpg","a1.jpg","a2.jpg"]
count = 0;
while True:
	conn, addr = socket01.accept() 
	print('Connected by', addr)

##################################################

	print('begin write image file '+ pic[count])
	imgFile = open(pic[count], 'w')
	while True:
		imgData = conn.recv(512) 
		if not imgData:
			break 
		imgFile.write(imgData)
	imgFile.close()
	print('image save')
##################################################

	conn.close() 
	count = count+1;
socket01.close()
print('server close')