#Exercice1
my_fav_numbers=[1,2,3,4,5]
my_fav_numbers.append(6)
my_fav_numbers.append(7)
print(my_fav_numbers)
my_fav_numbers.remove(5)
my_friend_fav_numbers=[6,7,8,9]
our_fav_numbers=my_fav_numbers+my_friend_fav_numbers
print(our_fav_numbers)

#Exercice2
#Non il est imposible d'ajouter plus d'entiers au tuple

#Exercice3
basket = ["Banana", "Apples", "Oranges", "Blueberries"];
basket.remove("Banana")
basket.remove("Blueberries")
basket.append("Kiwi")
basket.insert(0,"Apples")
a=0
for i in basket:
    if i=="Apples":
        a=a+1
print("il y'a ",a," pommes dans le panier")
print(basket)
basket.clear()
print(basket)


#Exercice4
#un float un type de données qui inclu les nombre à virgule et les approximations
#une autre façon de générer un float serait de faire la concatenation de int avec un point séparant deux partie distinste
1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5


#Exercice5
i=0
for i in range(0,21):
    print(i)

for i in range(0,21):
    if i%2==0:
        print(i)


#Exercice6
name="Sheila"
name1=input("Entrez votre nom")
while name1!=name:
    name1=input("Entrez votre nom")


#Exercice7
l=[]
i=int(input("combien de fruits voulez vous entrez? "))
for j in range(1,i+1):
    f=input("Entrez un fruit ")
    l.append(f)
print(l)
for i in l:
    fruit=input("votre fruit")
    if fruit==i:
        print("Vous avez choisi l'un de vos fruits préférés ! Prendre plaisir!")
    else:
        print("Vous avez choisi un nouveau fruit. J'espère que tu apprécies")


#Exercice8
somme=10
f=""
while f!="quitter":
    f=input("Entrez votre garniture: ")
    print("Nous avons ajouté ",f," à votre pizza")
    somme=somme+2.5
print("Le total est: ",somme)



#Exercice9
i=int(input("combien de membres comptent votre famille? "))
for j in range(1,i+1):
    f=int(input("Entrez les ages"))
    somme=0
    if f<=3:
        i=0
        somme=somme+i
    if 3<f>=12:
        j=10
        somme=somme+j
    if f>12:
        k=15
        somme=somme+k
print(somme)
#####################
l=["Alice","Victoire","Lena","Astrid"]
print("J'aurais besoin de vos ages svp")
for j in l:
    print(j," Quel age as tu?")
    f=int(input(":"))
    if f<16:
        l.remove(j)
    if f>21:
        l.remove(j)
print(l)


#Exercice10









#########
num=0
while num <= 10:    
    print(num)   
    num += 1

for i in range(10):
    print(i)

liste=["Armand", "Rolant", "Pacome", "Salif", "Fanta", "Sali", "Armel"]
for i in liste:
    print(i)

Liste=["Armand", "Rolant", "Pacome", "Salif", "Fanta", "Sali", "Armel"]
Liste=[{x**2:Liste[x]} for x in range(len(Liste))]
print(Liste)

Liste=["Armand", "Rolant", "Pacome", "Salif", "Fanta", "Sali", "Armel"]
diction={}
for i in range(len(Liste)):
    diction[i**2]=Liste[i]
print(diction)
for i in diction:
    print(i,diction[i])

