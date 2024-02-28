from module1 import *
#1
palgad=[1200,2500,750,395,1200]
inimesed=["Anton","Boris","Conan","Den","Erik"]

while True:
    print("1-andmete lisamine\n")
    valik=int(input())
    if valik==1:
        inimesed,palgad=lisa(inimesed,palgad,int(input("Mitu inimest lisame?")))
        andmed_veerudes(inimesed,palgad)
    elif valik==0:
        andmed_veerudes(inimesed,palgad)
    elif valik==2:
        kustuta(inimesed,palgad)
        andmed_veerudes(inimesed,palgad)
    elif valik==3:
        palgad=maxPalk(inimesed,palgad)
        print(palgad)
    elif valik==4:
        palgad=minPalk(inimesed,palgad)
        print(palgad)
       
     