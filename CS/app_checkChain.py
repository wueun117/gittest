import hashlib
from app_transaction import transaction

def generate_sha256(input_string):
    sha256_hash = hashlib.sha256()
    sha256_hash.update(input_string.encode('utf-8'))
    return sha256_hash.hexdigest()

def checkChain(person):
    start =  "SHARE/" + "1.txt"
    text=[1,2,3,4,5,6,7]
    while len(text) == 7 :
        #print("NOW: ",start)
        p = open(start)
        content = p.read()
        sha256_result = generate_sha256(content)
        p.close
        p2 = open(start)
        text = []
        for line in p2:
            text.append(line)
        next = text[1].split(": ")
        #print("NEXT: ",next[1],end="")
        start = "SHARE/" + next[1][:-1]
        p2.close
        try:
            f = open(start)
            text = []
            for line in f:
                text.append(line)
            hash=text[0].split(": ")
            #if hash[1][:-1] == sha256_result:
                #print("NO PROBLEM")
            if hash[1][:-1] != sha256_result:
                print("ERROR: "+str(int(start[6])-1)+start[7:])    
                #transaction("angle, "+person+", 10")
                return
            f.close
        except FileNotFoundError:
            print("Done")
            transaction("angle, "+person+", 10")
            return
    print("Done")
    transaction("angle, "+person+", 10")


checkChain(input("輸入當前對象: "))


