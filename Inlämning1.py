# sten sax påse spel
import random
import os
motståndarens_val = ["sten", "sax", "påse"]
igång = True
spelare_poäng = 0
motståndare_poäng = 0
resultat = " "
antal_omgångar = 3



    
def Clear():
    os.system('cls')

def Vinst():
    resultat = "Du fick poäng"
    return resultat
    

def Förlust():
    resultat = "Motståndaren fick poäng "
    return resultat
    

Clear()
print("Hej välkommen till Sten sax och påse spelet!\nFörst till 3 poäng vinner \nLycka till!!")


while  igång:
    
    motståndare = random.choice(motståndarens_val)
    
    val = input("Var god välj nåt av alternativen: \n1:Sten \n2:Sax \n3:Påse \n> ").lower().strip()
    Clear()
    
    #Vid oavgjort
    if val == motståndare:
         resultat = "Oavgjort"

    # vid vinst
    elif (val == "sten" and motståndare == "sax") or  (val == "sax" and motståndare == "påse") or ( val == "påse" and motståndare == "sten"):
        resultat = Vinst()
        
        spelare_poäng +=1

    #Vid förlust
    elif (val == "sten" and motståndare == "påse") or (val == "sax" and motståndare == "sten") or (val == "påse" and motståndare == "sax"):
        resultat = Förlust()
        motståndare_poäng += 1
      
       
    else:
        print("Felaktig inmatning!!!!")

    print("\n")
    print(f"Du: {val} ")
    print(f"motståndaren: {motståndare}")
    print(resultat)
    print("Ditt poäng " + str(spelare_poäng))
    print("Motståndarens poäng " + str(motståndare_poäng))

    if spelare_poäng == antal_omgångar: # Om spelaren vinner
        print("Du Vann!!")
        


        spela_igen = input("Vill du spela igen\nJa/Nej\n>").lower().strip()
        
        if spela_igen == "ja":
            motståndare_poäng = 0
            spelare_poäng = 0
            Clear()
        else:
            Clear()
            print("Tack för den här gången!")
            igång = False
        
    elif motståndare_poäng == antal_omgångar: # Om moståndaren vinner
        print("Du Förlorade!!")
        spela_igen = input("Vill du spela igen\nJa/Nej\n>").lower().strip()
        
        if spela_igen == "ja":
            motståndare_poäng = 0
            spelare_poäng = 0
            Clear()
        else:
            Clear()
            print("Tack för den här gången!")
            igång = False
        
        
    
        
    
        
    





