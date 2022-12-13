def HoE(a):
    b=False
    if a<150:
        b=True
        return b


cim=input("Add meg a könyv címét:")
while(cim!=""):
    oldal=int(input("Adja meg az oldalak számát:"))
    old=HoE(oldal)
    if old:
        print("A(z)",cim , "rövid terjedelmű könyv")
    else:
        print("A(z)",cim , "hosszú terjedelmű könyv")
    cim=(input("Add meg a könyv címét:"))

