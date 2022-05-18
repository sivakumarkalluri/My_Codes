statement="hi hello how are you"
# >>>>>>>>>>>>>>>splitting the satement in reverse<<<<<<<<<<<<<<<<<<

# statement=statement.split()
# output=" ".join(statement[::-1])
# print(output)

# >>>>>>>>>>>>>>>splitting the satement in reverse WITHOUT SPLIT AND JOIN FUNCTIONS<<<<<<<<<<<<<<<<<<

# l=[""]
# output=""
# for i in statement:
#     if i==" ":
#         l.append('')
#     else:
#         l[-1]+=i
# for i in range(1,len(l)+1):
#     output+=l[-i]

#     if i!=len(l):
#         output+=" "
# print(output)

# >>>>>>>>>>>>>>>splitting the every word in satement in reverse<<<<<<<<<<<<<<<<<<

statement=statement.split()
l=[]
for i in statement:
    l.append(i[::-1])
print(' '.join(l))