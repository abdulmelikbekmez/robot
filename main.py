from socket import socket, AF_INET, SOCK_STREAM
import sys
import json

class App:
    def __init__(self) -> None:
        self.ip = "172.20.19.43"
        self.port = 5000
        self.socket = None

    def __del__(self):
        self.socket = None
    
    def send(self, jsonn:dict):
        if not self.socket:
            return
        req = json.dumps(jsonn)
        self.socket.sendall(bytes(req, encoding="utf-8"))
        print("sended data => ", req)

    def start(self):
        req = {"Introduce": 1}

        with socket(AF_INET, SOCK_STREAM) as s:
            try:
                s.connect((self.ip, self.port))
            except ConnectionError as e:
                print(e)
                print("Aborting the program...")
                sys.exit()
            self.socket = s
            self.send(req)

            while True:
                data = s.recv(1024)
                if not data:
                    break

                print(f"\nreceived byte {data}\n")
                data = json.loads(data)
                print(f"\nreceived json {data}\n")

                if data["Action"] == 0:
                    print("ileri")

                elif data["Action"] == 1:
                    print("geri")

                elif data["Action"] == 2:
                    print("sol")
                elif data["Action"] == 3:
                    print("sağ")

                elif data["Action"] == 4:
                    print("dur")
                else:
                    print("data => ", data)




App().start()
