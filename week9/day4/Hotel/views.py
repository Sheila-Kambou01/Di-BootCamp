from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib import messages
from .models import *
from .forms import *
from django.contrib.auth.models import User
from django.contrib.auth import *



# Create your views here.
def home(request):
    anim = chambre.objects.all()

    return render(request,'visiteur/index.html', {'voiture' : anim})

def liste_ch(request):
    anim = chambre.objects.all()
    
    
    return render(request,'personel/chambre.html', {'chambre' : anim})


def administration(request):
    anim = chambre.objects.all()
    
    
    return render(request,'personel/index.html', {'avis' : anim})

def commentaire(request):
    anim = avis.objects.all()
    
    
    return render(request,'personel/avis.html', {'avis' : anim})

def locations(request):
    anima = location.objects.all()
    statu = location.objects.all()
    
    return render(request,'personel/location.html', {'locations' : anima, 'statut':statu})

def listclient(request):
    clien = client.objects.all()
    
    return render(request,'personel/client.html', {'clients' : clien})

def afficher(request, id):
    if request.method == 'POST':
        pi = location.objects.get(pk=id)
      
    else:
        pi = location.objects.get(pk=id)
   
    return render(request, 'visiteur/afficher.html', {'info':pi})



def inscrire(request):  
    clien = client.objects.all()
    vhi = chambre.objects.all()
    if request.method == 'POST':
        clie = request.POST['client']
        vehicul = request.POST['voiture']
        date_crea = request.POST['date_crea']
        date_ret= request.POST['date_ret']
        cout = request.POST['cout'] 
        mon_user = location( client_id_id=clie, chambre_id_id=vehicul, date_location=date_crea, date_retour=date_ret, cout=cout)
        mon_user.save()
        messages.success(request, 'votre Location a été Enregistré avec succès')
        return redirect('home')
   
    return render(request, 'visiteur/ajouterloc.html',{'inf':clien, 'voit':vhi} )

def ajoutervehi(request): 
    vhi = client.objects.all() 
    if request.method == 'POST':
        clie = request.POST['client']
        cout = request.POST['avis'] 
        mon_vehi = avis( client_id_id=clie,  avis=cout)
        mon_vehi.save()
        messages.success(request, 'Merci pour votre commentaire')
        return redirect('home')
   
    return render(request, 'visiteur/ajoutervhi.html',{ 'voit':vhi}  )


def ajoutercli(request):  
    if request.method == 'POST':
        nm = request.POST['nom']
        pnm = request.POST['prenom']
        adr = request.POST['adresse']
        em= request.POST['email']
        vil = request.POST['ville'] 
        pay = request.POST['pays'] 
        mon_client = client( nom=nm, prenom=pnm, adresse=adr, email=em, ville=vil, pays=pay)
        mon_client.save()
        messages.success(request, 'client enregistré avec succès')
        return redirect('home')
   
    return render(request, 'visiteur/ajoutercli.html' )

def ajoutech(request): 
    voit = type_chambre.objects.all()  
    if request.method == 'POST':
        tail = request.POST['taille']
        typ = request.POST['type']
        dat = request.POST['date_crea']
        co= request.POST['cout']
        phot = request.POST['imag'] 
        mon_chambr = chambre( taille=tail, type_chambre_id_id=typ, date_creation=dat, cout=co, photo=phot,)
        mon_chambr.save()
        messages.success(request, 'chambre enregistré avec succès')
        return redirect('administration')
   
    return render(request, 'personel/ajoutervhi.html',{ 'voit':voit} )

def registerch(request):
    if request.method == 'POST':
        form = EnregistreChambre(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("administration")
    return render(request, 'personel/ajout_cha.html' )

def modifier(request, id):
    if request.method == 'POST':
        pi = client.objects.get(pk=id)
        fm = EnregistreUser(request.POST, instance=pi )
        if fm.is_valid():
            fm.save()
            messages.success(request, 'Information du client modifié avec succès')
            return redirect('administration')
    else:
        pi = client.objects.get(pk=id)
        fm = EnregistreUser(instance= pi)
    return render(request, 'personel/modifier_client.html', {'form':fm})

def modifierloc(request, id):
    if request.method == 'POST':
        pi = location.objects.get(pk=id)
        fm = ModifierLoc(request.POST, instance=pi )
        if fm.is_valid():
            fm.save()
            messages.success(request, 'Information sur la location modifié avec succès')
            return redirect('administration')
    else:
        pi = location.objects.get(pk=id)
        fm = ModifierLoc(instance= pi)
    return render(request, 'personel/modifier_loc.html', {'form':fm})

def supprimer(request, id):
    if request.method == 'POST':
        pi = location.objects.get(pk=id)
        pi.delete()
        messages.success(request, 'la location a été Supprimer avec succès')
        return redirect('administration')
    
    
def deconnecter(request):
    logout(request)
    messages.success(request, 'votre compte a été deconnecté')
    return render(request, 'personel/inscrire.html')
    
    
def connecter(request):
    if request.method == 'POST':
         username = request.POST['username'],
         passwor = request.POST['password'],
         use= authenticate(username=request.POST['username'], password=request.POST['password'])
         if use is not None:
             login(request, use)
             nom = User.last_name
             return render(request, 'personel/index.html', {'nom':nom})
         else:
             messages.error(request, 'Mauvaise connection')
             return redirect('inscrire')
    return render(request, 'personel/login.html')
    
    

def inscrireuser(request):
     if request.method == 'POST':
         username = request.POST['username']
         lastname = request.POST['last_name']
         firstname = request.POST['first_name']
         email= request.POST['email']
         password = request.POST['password'] 
         mon_user = User.objects.create_user(username, email, password)
         mon_user.first_name = firstname
         mon_user.last_name = lastname
         mon_user.save()
         messages.success(request, 'votre compte personnel a été crée')
         return redirect('inscrire')
   
     return render(request, 'personel/inscrire.html')
 
def logout_user(request):
    logout(request)
    return redirect('personel/index.html')
    



   