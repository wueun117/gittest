
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
        if temp[0] == person:
            print(text[i],end='')
        elif temp[1] == person:
            print(text[i],end='')
    f.close
    print('\n',end='')
    print("Block",num)
    print()
    num+=1
    start = "SHARE/" + next
    

    




