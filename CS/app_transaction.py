import hashlib



def generate_sha256(input_string):
    sha256_hash = hashlib.sha256()
    sha256_hash.update(input_string.encode('utf-8'))
    return sha256_hash.hexdigest()


def transaction(trade):
    start = "SHARE/" + "1.txt"
    text=[1,2,3,4,5,6,7]
    while len(text) == 7 :
        try:
            p = open(start)
            content = p.read()
            p.close
        except FileNotFoundError:
            sha256_result = str(generate_sha256(content))
            num=str(int(next[0])+1)
            n = open(start,'a') 
            n.write("Sha256 of previous block: "+sha256_result)
            n.write('\n')
            n.write("Next block: "+num+".txt")
            n.write('\n')
            n.write(trade)
            break

        f = open(start) 
        text = []
        for line in f:
            text.append(line)
        if len(text) != 7:
            n=open(start,'a')
            n.write('\n')
            n.write(trade)
            n.close
        next = text[1][12:-1]
        start = "SHARE/" + next

