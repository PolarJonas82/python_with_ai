# sten sax påse spel
import random
import os
spel = ["Sten", "Sax", "Påse"]
playing = True
spelare_Poäng = 0
motståndare_Poäng = 0
resultat = " "
antal_Omgångar = 3

def Vinst():
    resultat = "Grattis, du vann!!"
    spelare_Poäng = +1

def Förlust():
    resultat = "Tyvärr du förlorade!!"
    motståndare_Poäng = +1


os.system('cls')
print("Hej välkommen till Sten sax och påse spelet!")


while  playing:
    
    motståndare = random.choice(spel)

    val = input("Var god välj nåt av alternativen: \n1:Sten \n2:Sax \n3:Påse \n> ")

    if val == "Sten" and motståndare == "Sax":
        #Vinst()
        #resultat = "Grattis, du vann!!"
        spelare_Poäng +=1

    elif val == "Sten" and motståndare == "Påse":
        #Förlust()
       # resultat = "Tyvärr du förlorade!!"
        motståndare_Poäng += 1

    elif val == "Sax" and motståndare == "Sten":
        #Förlust()
        #resultat = "Tyvärr du förlorade!!"
        motståndare_Poäng += 1

    elif val == "Sax" and motståndare == "Påse":
        #Vinst()
        #resultat = "Grattis, du vann!!"
        spelare_Poäng  += 1

    elif val == "Påse" and motståndare == "Sten":
       # Vinst()
        #resultat = "Grattis, du vann!!"
        spelare_Poäng += 1

    elif val == "Påse" and motståndare == "Sax":
       # Förlust()
        #resultat = "Tyvärr du förlorade!!"
        motståndare_Poäng +=1

    elif val == motståndare:
         resultat = "Oavgjort"
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



