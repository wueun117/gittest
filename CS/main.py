from Functions import transaction, checkLog, checkMoney, checkChain, checkAllChains

import socket
import threading

class P2PNode:
    def __init__(self, port, peers):
        self.port = port
        self.peers = peers
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
        # 設置 IPv4地址（AF_INET）和 UDP協議（SOCK_DGRAM）
        self.sock.bind(('192.168.1.110', self.port)) 
        # 設置此client節點IP
    
    def start(self):
        threading.Thread(target=self._listen).start()
        threading.Thread(target=self._send_messages).start()
    
    def _listen(self):
        while True:
            data, addr = self.sock.recvfrom(1024)
            print(f"Received {data.decode('utf-8')} from {addr}")
            # 做transaction 更新本地帳本
    
    def _send_messages(self):
        while True:
            message = input("Enter a message: ")
            for peer in self.peers:
                self.sock.sendto(message.encode('utf-8'), peer)
                # 把帳本更動(轉帳 跟 獎勵機制??)發出去

    

if __name__ == "__main__":
    port = 8001 #此client節點的port
    peers= ["192.168.1.110"] #其他client節點的IP
    node = P2PNode(port, peers)




command = input("Enter a command (checkLog checkMoney checkChain transaction): ")

if command == "checkLog":
    checkLog(input("Who are you: "))
elif command == "checkMoney":
    checkMoney(input("Who are you: "))


elif command == "checkChain":
    who=input("Who are you: ")
    if print(checkChain(who)) != False:
        node.start()
        # 把十元小獎勵傳出去 agale, who, 10
elif command == "transaction":
    transaction(input("Input the record: "))
    node.start()
elif command == "checkAllChains":
    print(checkAllChains(input("Who are you: ")))
    node.start()
    # 大家都做checkAllChains 回傳的sha拿來比較
    # if一樣 再來做transaction
else:
    print("Do not support")