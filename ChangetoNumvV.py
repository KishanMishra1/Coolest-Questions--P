def chartonum(ch):
    res=0
    for char in ch:
        res*=26
        res+=(1+ord(char)-ord("A"))

    return res

def numtochar(n):
    str=""
    while n!=0:
        n=n-1
        temp=n%26
        str+=chr(temp+ord("A"))
        n//=26
    return str[::-1]

print(numtochar(28))
print(chartonum("aa"))
