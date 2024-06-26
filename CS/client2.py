from Functions import transaction, checkLog, checkMoney, checkChain, checkAllChains, getAllChains

import socket
import threading
import time

class P2PNode:
    def __init__(self, port, peers):
        self.port = port
        self.peers = peers
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
        # 設置 IPv4地址（AF_INET）和 UDP協議（SOCK_DGRAM）
        self.sock.bind(('172.17.0.6', self.port)) 
        self.re = [""]
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
            elif len(mess[0]) >= 20:
                self.re.append(data.decode('utf-8'))
            else:
                self._send_messages(checkAllChains(data.decode('utf-8')))
                # 檢查節點的指令
                # 大家都做checkAllChains 回傳的sha拿來比較
                # if一樣 再來做transaction
    
    def _send_messages(self, message):
        for peer in self.peers:
            self.sock.sendto(message.encode('utf-8'), (peer, self.port))



    

if __name__ == "__main__":
    port = 8001 #此client節點的port
    peers= ["172.17.0.5","172.17.0.7"] #其他client節點的IP
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


#叫大家去做檢查
elif command == "checkAllChains":
    who=input("Who are you: ")
    node.start("checkAllChains "+who)
    node.start()
    time.sleep(5)
    # print(node.re)


    
    wrong=1000
    for i in range(0,len(node.re)-1):
        if str(checkAllChains(who)) != node.re[i]:
            wrong=i
            break
    if wrong == 1000:
        transaction("angle, " + who + ", 100")       
    else:
        count = [0,0,0]
        for i in range(0,len(node.re)-1):
            for j in range(0,len(node.re)-1):
                if node.re[i] == node.re[j] and i!=j:
                    count[i] +=1
                    if count[i] == 2:
                        node.start("getAllChains "+who)
                        node.start()
                        time.sleep(5)
                    else:
                        print("Do not trust me")                              
        # 如果不是都相同 要做共享機制
        # 再跑一次迴圈看哪種sha256 result最多
        # 多做一個if看有沒有超過50%
else:
    print("Do not support")





