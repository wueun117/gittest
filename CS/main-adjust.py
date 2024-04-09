from Functions import transaction, checkLog, checkMoney, checkChain, checkAllChains

import socket
import threading

class P2PNode:
    def __init__(self, port, peers):
        self.port = port
        self.peers = peers
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
        # 設置 IPv4地址（AF_INET）和 UDP協議（SOCK_DGRAM）
        self.sock.bind(('127.0.0.1', self.port)) 
        self.re = "0"
        # 設置此client節點IP
    
    def start(self, message=None):
        threading.Thread(target=self._listen).start()
        if message is not None:
            threading.Thread(target=self._send_messages, args=(message,)).start()
    
    def _listen(self):
        while True:
            data, addr = self.sock.recvfrom(1024)
            print(f"Received {data.decode('utf-8')} from {addr}")
            mess=data.decode('utf-8').split(",")
            if len(mess) == 3:
                transaction(data.decode('utf-8'))
                # 一般的轉帳紀錄 # 做transaction 更新本地帳本
                print("aaaaa")
            elif len(mess[0]) >= 20:
                self.re = data.decode('utf-8')
                print(self.re)
                print("bbbbb")
            else:
                self._send_messages(checkAllChains(data.decode('utf-8')))
                # 檢查節點的指令
                # 大家都做checkAllChains 回傳的sha拿來比較
                # if一樣 再來做transaction
                print("ccccc")
    
    def _send_messages(self, message):
        for peer in self.peers:
            self.sock.sendto(message.encode('utf-8'), (peer, self.port))



    

if __name__ == "__main__":
    port = 8001 #此client節點的port
    peers= ["127.0.0.1"] #其他client節點的IP
    node = P2PNode(port, peers)




command = input("Enter a command (checkLog checkMoney checkChain transaction): ")

if command == "checkLog":
    checkLog(input("Who are you: "))
elif command == "checkMoney":
    checkMoney(input("Who are you: "))

#把要加的帳本紀錄傳給大家
elif command == "transaction":
    record=input("Input the record: ")
    transaction(record)
    node.start(record)

elif command == "checkChain":
    who=input("Who are you: ")
    if print(checkChain(who)) != False:
        node.start("agale, " + who + ", 10")



##############################################################



#叫大家去做檢查
elif command == "checkAllChains":
    who=input("Who are you: ")
    node.start("checkAllChains "+who)
    node.start()
    print(node.re)
    if print(checkAllChains(who)+"OUT") == node.re:
        transaction("angle, " + who + ", 100")
    print("end")
   
else:
    print("Do not support")





print(node.re)

