def freq(str1):
    dup=[]
    str1=str1.lower()
    li=list(str1)
    for i in li:
        if i not in dup:
            dup.append(i)
    print(dup)
    for i in dup:
        print(i,":",str1.count(i))

str1="ROhitt"
print(freq(str1))