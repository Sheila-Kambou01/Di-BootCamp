from django import views
from django.urls import path,include
from .views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [

    path('',home, name='home'),
    path('location',locations, name='locations'),
    path('chambre_ajoute',ajoutech, name='chambre_ajoute'),
    path('inscrire',inscrire, name='inscrire'),
    path('inscrire_client',ajoutercli, name='inscriree'),
    path('avis',ajoutervehi, name='inscrirer'),
    path('location<int:id>/',afficher , name='afficher' ),
    path('client<int:id>/',modifier , name='modifier_cl' ),
    path('modifloc<int:id>/',modifierloc , name='modifier_loc' ),
    path('client',listclient , name='liste' ),
    path('personel_index',administration , name='administration' ),
    path('personel_chambre',liste_ch , name='liste_ch' ),
    path('personel_commentaire',commentaire , name='liste_commentaire' ),
    path('delete/<int:id>/',supprimer, name='supprimer' ),
    path('login',connecter , name='connecter' ),
    path('logout',deconnecter , name='deconnecter' ),
    path('personel',inscrireuser , name='inscrire' ),
    path('personelajout',registerch , name='ajout_cha' ),
    path('logout/', logout_user, name='logout'),
   
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)