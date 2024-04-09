import hashlib
from Uapp_transaction import transaction

def generate_sha256(input_string):
    sha256_hash = hashlib.sha256()
    sha256_hash.update(input_string.encode('utf-8'))
    return sha256_hash.hexdigest()

def checkChain(person):
    start =  "dbdata/" + "1.txt"
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
        start = "dbdata/" + next[1][:-1]
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
                temp=start.split(".")
                temp2=temp[0].split('/')
                print(temp2)
                print("ERROR: "+str(int(temp2[1])-1)+temp[1])
                #transaction("angle, "+person+", 10")
                return
            f.close
        except FileNotFoundError:
            print("Done")
            transaction("angle, "+person+", 10")
            return sha256_result
    n = open(start)
    content = n.read()
    sha256_result = generate_sha256(content)
    n.close
    print("Done")
    transaction("angle, "+person+", 10")
    return sha256_result
    # 回傳最後一個BLOCK的sha256


    