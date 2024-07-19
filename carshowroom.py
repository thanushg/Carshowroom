class car_show_room:
    def __init__(self):
        self.cgst=5555
        self.sgst=4444
        self.insurance=6666
        
    def company(self,name):
        while True:
            name=input("select the company : ") 
            if name=="audi":
                print("welcome to ",name,"company")
                self.f=name
                break
            elif name=="tata":
                self.f=name
                print("welcome to ",name,"company")
                break
            elif name=="mahendhra":
                self.f=name
                print("welcome to ",name,"company")
                break
            else:
                print(" try again , choose the above companies")
            
        
        
    def model(self,m):
       
            models=[["ax","bx"],["crystal","inova"],["thar","xuv"]]
        
            if m=="audi":
                print("select the model in ",m,"company")
                print(models[0])
                
            
            elif m=="tata":
                print("select the model in ",m,"company")
                print(models[1])
                
            
            elif m=="mahendhra" :
                print("select the model in ",m,"company")
                print(models[2])
                
            
            else:
                print("sorry , it is not available ")
                
    def price(self,p):
        while True:
            p = input("enter  model : ")
            
            if p=="ax":
                ax=250000
                print("ax price is ",ax)
                tprice=self.cgst+self.sgst+self.insurance+ax
                print("the onroad price of ax is : ",tprice)
                break
                
            elif p=="bx":
                bx=40000000
                print("bx price is ",bx)
                tprice=self.cgst+self.sgst+self.insurance+bx
                print("the onroad price of bx is : ",tprice)
                break
                
            elif p=="crystal":
                crystal=5666778
                print("crystal price is ",crystal)
                tprice=self.cgst+self.sgst+self.insurance+crystal
                print("the onroad price of crystal is : ",tprice)
                break
            
            elif p=="inova":
                inova=6000000
                print("inova price is ",inova)
                tprice=self.cgst+self.sgst+self.insurance+inova
                print("the onroad price of inova is : ",tprice)
                break
                
            elif p=="thar" :
                
                thar=999999
                print("thar price is ",thar)
                tprice=self.cgst+self.sgst+self.insurance+thar
                print("the onroad price of thar is : ",tprice)
                break
                
            elif p=="xuv":
                xuv=8899000
                print("xuv price is ",xuv)
                tprice=self.cgst+self.sgst+self.insurance+ax
                print("the onroad price of xuv is : ",tprice)
                break
                
            else:
                print("enter the correct model")
            
companies=["audi","tata","mahendhra"]
print(companies)      
n=input("select the company : ") 
o=car_show_room()
o.company(n)
o.model(n)
p=input("select the model : ")
o.price(p)
