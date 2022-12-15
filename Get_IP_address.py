import socket
hostname = input("Ptease enter website address: \n")

# IP lookup from hostname
print (f'The {hostname} IP Address is {socket.gethostbyname(hostname)}')

