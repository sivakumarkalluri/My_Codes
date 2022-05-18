packetData="10101010000001011110001011001111110001101100011011000101"
bytes=[packetData[i:i+8] for i in range(0, len(packetData), 8)]
size=int(bytes[1],2)
def xor(a, b, n):
    ans = ""
    for i in range(n):
        if (a[i] == b[i]):
            ans += "0"
        else:
            ans += "1"
    return ans
   
if size==len(bytes)-2:
    res=""
    for i in bytes[2:]:
        output=xor(bytes[0],i,len(bytes[0]))
        output=chr(int(output,2))
        res+=output
    print(res)

else:
    print("Invalid packet")