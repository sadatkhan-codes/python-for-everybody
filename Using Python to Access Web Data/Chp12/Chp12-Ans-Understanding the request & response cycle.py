import socket     # Get Python's networking tools

# Create a network connection
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the web server
mysock.connect(('data.pr4e.org', 80))

# Create a request saying "Give me intro-short.txt" and convert it to bytes.
cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)           # receive data upto 512 bytes
    if len(data) < 1:                 # when there is 0 data then break the while loop
        break
    print(data.decode(), end='')      
    
# convert bytes into python string and dont add new lines, the data we're receiving already contains its own line breaks.

mysock.close()