#============================== IMPORTS

import socket
from threading import Thread
import os
from flask import Flask, render_template

#============================== SETTING THE HOST AND THE PORT
HOST = "127.0.0.1"
PORT = 8000

#============================== PROCEDURES NEEDED

def appendToFile(fname,stringToAppend):
    with open(fname, 'a+') as f:
        f.write(stringToAppend)
    f.close()

def socketStuff(host):
    #Code for listening on a certain port
    with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
        #Bind is used to associate the port with a specific network interface and port number
        s.bind((HOST,PORT))
        #This enables the server to accept connections (listening socket)
        s.listen()
        conn, addr = s.accept()
        with conn:
            print('Connected by', addr)
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                decoded_data = data.decode("utf-8")

                print(decoded_data)
                try:
                    appendToFile('log.txt',decoded_data + " " + host + '\n')
                except Exception as e:
                    print("An error occured: ",e)

                conn.sendall(data)



def webServerStuff():
    app = Flask('app')
    @app.route('/')
    def run():
        return render_template('main.html')

    app.run(host = '0.0.0.0', port = 8080)


#============================== RUN THE CODE

def main():
    #Thread(target=socketStuff, args=(HOST)).start()
    Thread(target=webServerStuff).start()
    socketStuff(HOST)

if(__name__=='__main__'):
    main()