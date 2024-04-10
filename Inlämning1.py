# sten sax påse spel
import random
import os
Motståndarens_val = ["sten", "sax", "påse"]
igång = True
spelare_poäng = 0
motståndare_poäng = 0
resultat = " "
antal_omgångar = 3
spela_igen = ""

def Spela_Igen():
    spela_igen = input("Vill du spela igen\nJa/Nej\n>").lower()
        
    if spela_igen == "ja":
        motståndare_poäng = 0
        spelare_poäng = 0
        Clear()
    else:
        Clear()
        print("Tack för den här gången!")
        igång = False
        
    
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
    
    motståndare = random.choice(Motståndarens_val)
    
    val = input("Var god välj nåt av alternativen: \n1:Sten \n2:Sax \n3:Påse \n> ").lower()
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

    if spelare_poäng == antal_omgångar:
        print("Du Vann!!")
       #Spela_Igen()


        spela_igen = input("Vill du spela igen\nJa/Nej\n>").lower()
        
        if spela_igen == "ja":
            motståndare_poäng = 0
            spelare_poäng = 0
            Clear()
        else:
            Clear()
            print("Tack för den här gången!")
            igång = False
        
    elif motståndare_poäng == antal_omgångar:
        print("Du Förlorade!!")
        #Spela_Igen()

        spela_igen = input("Vill du spela igen\nJa/Nej\n>").lower()
        
        if spela_igen == "ja":
            motståndare_poäng = 0
            spelare_poäng = 0
            Clear()
        else:
            Clear()
            print("Tack för den här gången!")
            igång = False
        
        
    
        
    
        
    





