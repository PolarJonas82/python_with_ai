# sten sax påse spel
import random
import os
Motståndarens_val = ["sten", "sax", "påse"]
igång = True
spelare_poäng = 0
motståndare_poäng = 0
resultat = " "
antal_omgångar = 3


def Vinst():
    resultat = "Du fick poäng"
    #spelare_poäng +=1
    

def Förlust():
    resultat = "Motståndaren fick poäng "
    #motståndare_poäng += 1
    

os.system('cls')
print("Hej välkommen till Sten sax och påse spelet!")


while  igång:
    
    motståndare = random.choice(Motståndarens_val)
    
    val = input("Var god välj nåt av alternativen: \n1:Sten \n2:Sax \n3:Påse \n> ")
    val = val.lower()
    os.system('cls')
    if val == motståndare:
         resultat = "Oavgjort"
    elif val == "sten" and motståndare == "sax":
        #Vinst()
        resultat = " "
        spelare_poäng +=1

    elif val == "sten" and motståndare == "påse":
        #Förlust()
        resultat = " "
        motståndare_poäng += 1

    elif val == "sax" and motståndare == "sten":
        #Förlust()
        resultat = " "
        motståndare_poäng += 1

    elif val == "sax" and motståndare == "påse":
        #Vinst()
        resultat = " "
        spelare_poäng  += 1

    elif val == "påse" and motståndare == "sten":
       #Vinst()
        resultat = " "
        spelare_poäng += 1

    elif val == "påse" and motståndare == "sax":
       # Förlust()
        resultat = " "
        motståndare_poäng +=1

    
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
        igång = False

    elif motståndare_poäng == antal_omgångar:
        print("Du Förlorade!!")
        igång = False

    





