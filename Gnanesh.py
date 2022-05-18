n=12
num=718
def DectoNBase(n,num):
    q=num
    output=""
    dict={}
    for i in range(9):
        dict[i]=i
    count=65
    for i in range(10,36):
        dict[i]=chr(count)
        count+=1
    while q>0:
        temp=q
        q=q//n
        r=temp%n
        output+=str(dict[r])
    return num
