import socket
from flask import Flask
from threading import Thread

HOST = "127.0.0.1"
PORT = 8000

def socketStuff():

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST,PORT))
        while True:
            dataToSend = input()
            if(dataToSend == ""):
                pass
            else:
                if(dataToSend != "x"):
                    encoded_string = dataToSend. encode()
                    byte_array = bytearray(encoded_string)
                    s.sendall(byte_array)
        
                else:
                    s.close()
                    break

                data = s.recv(1024)
                print('Received', repr(data))


def main():
    Thread(target = socketStuff).start()

if(__name__ == '__main__'):
    main()