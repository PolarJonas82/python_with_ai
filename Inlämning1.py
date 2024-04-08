# sten sax påse spel
import random
import os
spel = ["sten", "sax", "påse"]
playing = True
spelare_Poäng = 0
motståndare_Poäng = 0
resultat = " "
antal_Omgångar = 3

def Vinst():
    resultat = "Du fick poäng"
    spelare_Poäng = +1

def Förlust():
    resultat = "Motståndaren fick poäng "
    motståndare_Poäng = +1


os.system('cls')
print("Hej välkommen till Sten sax och påse spelet!")


while  playing:
    
    motståndare = random.choice(spel)
    
    val = input("Var god välj nåt av alternativen: \n1:Sten \n2:Sax \n3:Påse \n> ")
    os.system('cls')
    if val == motståndare:
         resultat = "Oavgjort"
    elif val.lower() == "sten" and motståndare == "sax":
        #Vinst()
        resultat = " "
        spelare_Poäng +=1

    elif val.lower() == "sten" and motståndare == "påse":
        #Förlust()
        resultat = " "
        motståndare_Poäng += 1

    elif val.lower() == "sax" and motståndare == "sten":
        #Förlust()
        resultat = " "
        motståndare_Poäng += 1

    elif val.lower() == "sax" and motståndare == "påse":
        #Vinst()
        resultat = " "
        spelare_Poäng  += 1

    elif val.lower() == "påse" and motståndare == "sten":
       # Vinst()
        resultat = " "
        spelare_Poäng += 1

    elif val.lower() == "påse" and motståndare == "sax":
       # Förlust()
        resultat = " "
        motståndare_Poäng +=1

    
    else:
        print("Felaktig inmatning!!!!")

    print("\n")
    print(val)
    print(motståndare)
    print(resultat)
    print("Ditt poäng " + str(spelare_Poäng))
    print("Motståndarens poäng " + str(motståndare_Poäng))

    if spelare_Poäng == antal_Omgångar:
        print("Du Vann!!")
        playing = False

    elif motståndare_Poäng == antal_Omgångar:
        print("Du Förlorade!!")
        playing = False



