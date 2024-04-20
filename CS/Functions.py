import hashlib



def generate_sha256(input_string):
    sha256_hash = hashlib.sha256()
    sha256_hash.update(input_string.encode('utf-8'))
    return sha256_hash.hexdigest()

def transaction(trade):
    start = "dbdata/" + "1.txt"
    text=[1,2,3,4,5,6,7]
    while len(text) == 7 :
        try:
            p = open(start)
            content = p.read()
            p.close
        except FileNotFoundError:
            sha256_result = str(generate_sha256(content))
            temp=next.split('.')
            num=str(int(temp[0])+1)
            n = open(start,'a')
            n.write("Sha256 of previous block: "+sha256_result)
            n.write('\n')
            n.write("Next block: "+num+".txt")
            n.write('\n')
            n.write(trade)
            n.write('\n')
            break

        f = open(start)
        text = []
        for line in f:
            text.append(line)
        if len(text) != 7:
            n=open(start,'a')
            n.write(trade)
            n.write('\n')
            n.close
        next = text[1][12:-1]
        start = "dbdata/" + next

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
                return False
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

def checkAllChains(person):
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
                return False
            f.close
        except FileNotFoundError:
            print("Done")
            return sha256_result
    n = open(start)
    content = n.read()
    sha256_result = generate_sha256(content)
    n.close
    print("Done")
    return sha256_result
    # 回傳最後一個BLOCK的sha256

def getAllChains(person):
    start =  "dbdata/" + "1.txt"
    text=[1,2,3,4,5,6,7]
    alltext=[]
    while len(text) == 7 :
        #print("NOW: ",start)
        p = open(start)
        content = p.read()
        alltext.append(content)
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
                return False
            f.close
        except FileNotFoundError:
            print("Done")
            return alltext
    n = open(start)
    content = n.read()
    alltext.append(content)
    sha256_result = generate_sha256(content)
    n.close
    print("Done")
    return alltext
    # 回傳最後一個BLOCK的sha256


def checkMoney(person):
    start = "dbdata/" + "1.txt"
    text=[1,2,3,4,5,6,7]
    num=1
    beg=0
    while len(text) == 7 :
        try:
            f = open(start)
            text = []
            for line in f:
                text.append(line)
            next = text[1][12:-1]
            for i in range(2,len(text)):
                temp = text[i].split(", ")
                if(text[i][-1]=='\n'):
                    text[i]=text[i]
                else:
                    text[i]=text[i]+'\n'
                if temp[0] == person:
                    beg=beg-int(temp[2])
                    print(text[i][:-1])
                elif temp[1] == person:
                    beg=beg+int(temp[2])
                    print(text[i][:-1])
            f.close
            print("Block",num,beg)
            print()

            num+=1
            start = "dbdata/" + next
        except FileNotFoundError:
                break

def checkLog(person):
    start = "dbdata/" + "1.txt"
    text=[1,2,3,4,5,6,7]
    num=1
    while len(text) == 7 :
        try:
            f = open(start)
            text = []
            for line in f:
                text.append(line)
            next = text[1][12:-1]
            for i in range(2,len(text)):
                temp = text[i].split(", ")
                if text[i][-1]=='\n':
                    text[i]=text[i]
                else:
                    text[i]=text[i]+'\n'
                if temp[0] == person:
                    print(text[i][:-1])
                elif temp[1] == person:
                    print(text[i][:-1])
            f.close
            print("Block",num)
            print()
            num+=1
            start = "dbdata/" + next
        except FileNotFoundError:
                break
    
    