# -*- coding: utf8 -*-

import socket

host = '10.0.1.26'
# port = 5000
#host = 'localhost' 
port = 5555
address = (host, port)

socket02 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

socket02.connect(address)
print('start send image')
imgFile = open("wtf.jpg", "rb")
while True:
    imgData = imgFile.readline(512)
    if not imgData:
        break  # 
    socket02.send(imgData)
imgFile.close()
print('transmit end')
##################################

socket02.close()  #
print('client close')