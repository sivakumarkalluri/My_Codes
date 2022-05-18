class marreddy: 
    global vehicles,array,output,payment
    output=[]
    vehicles={}
    array=[]
    payment=0
    def __init__(self):
        self.payment=0
    def serviceId(self,Id,state,name,manuf,dist,ins):
        vehicles[id]=self.state
        self.Id=Id
        self.name=name
        self.manuf=manuf
        self.dist=dist
        self.ins=ins
        self.state=state
        array.append([self.Id,self.name,self.manuf,self.dist,self.ins,self.state]) 
    def result(self,array,value):
        self.array=array
        self.value=value
        for  i in self.array:
            if i[3]>5000 and i[5]==self.value:
                if i[4]=="yes":
                    self.payment=1750
                else:
                    self.payment=1000
                output.append([i[0],i[1],i[2],self.payment])
    def set(self,Id,name,manuf,dist,ins,state):
        self.Id=Id
        self.name=name
        self.manuf=manuf
        self.dist=dist
        self.ins=ins
        self.state=state
        self.serviceId(Id,self.state,self.name,self.manuf,self.dist,self.ins)  
data=int(input())
ServiceCenter=marreddy()
for i in range(data):
    ServiceCenter.set(int(input()),input(),input(),int(input()),input(),input())
value=input()
calculate=marreddy()
calculate.result(array,value)
if len(output)>0:   
    for i in output:
        result=""
        for j in i:
            result+=str(j)+" "
        print(result)
else:
    print("No car found with given criteria")
