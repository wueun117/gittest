person=input("輸入查詢對象: ")
start = "SHARE/" + "1.txt"
text=[1,2,3,4,5,6,7]
num=1
while len(text) == 7 :
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
    start = "SHARE/" + next
    

    




