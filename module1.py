#1-Lisage veel mõned inimesed ja palgad (numbri ütleb kasutaja)
def lisa(i:list,p:list,n=1)->any:
    """Funktsioon tagastab loendid, kus lisatud inimesi ja palka
    :param List i: inimeste järjend
    :param List p: palkada järjend
    :param Int n: inimeste arv
    rtype: List,List
    """
    if n>0:
        for j in range(n):
            nimi=input("Sisesta nimi: ").capitalize()
            palk=int(input("Sisesta palki arv: "))
            i.append(nimi)
            p.append(palk)
    return i,p
#19
def andmed_veerudes(i:list,p:list):
    """Funktsioon kuvab ekranile kahe järjendite andmed veerudes
    :param List i: inimeste järjend
    :param List p: palkada järjend
    """
    for j in range(len(i)):
        print(i[j],"-",p[j])


#2-Kustutage inimene ja tema palk (sisestage nimi),
def kustuta(i:list,p:list)->any:
    """Funktsioon kustuda andmeid ja tagastab listid
    :param List i: inimeste järjend
    :param List p: palkada järjend
    """
    nimi=input("Sisesta nimi: ")
    for j in range(0,len(i)-1):
         if nimi in i:
           i.remove(nimi)
           p.pop(j)
    return


#3-Suurim palk ja kes seda saab
def maxPalk(i:list,p:list)->any:
    """
    """
    nimed=[]
    max_palk=max(p)
    ind=-1
    for palk in p:
        if palk==max_palk:
            ind+=1
            nimi=i[p.index(palk,ind)]
            nimed.append(nimi)
    return nimed,max(p)

#4-Kes saab kõige väiksemat palka ja mida täpselt?
def minPalk(i:list,p:list)->any:
    """
    """
    nimed=[]
    min_palk=min(p)
    ind=-1
    for palk in p:
        if palk==min_palk:
            ind+=1
            nimi=i[p.index(palk,ind)]
            nimed.append(nimi)
    return nimed,min(p)
