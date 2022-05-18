w=int(input())
web=[]
for i in range(w):
    web.append(int(input()))
a=int(input())
app=[]
for i in range(a):
    app.append(int(input()))
if min(web)<min(app):
    small=web
    big=app
else:
    small=app
    big=web
large=max(web+app)
count=0
current=small
other=big
for j in range(min(small)+1,large+1):
    if j in other:
        other,current=current,other
        count+=1
print(count)

