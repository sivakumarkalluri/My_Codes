def String_count(a,count=0,i=0):
    if i>=len(a):
        return count
    if type(a[i])==str:
        count+=1
    return String_count(a,count,i+1)
print(String_count(["hai",1,"py",2,"hello","king","how"]))