from django.db import models

class type_chambre(models.Model):
    nom = models.CharField(max_length=30)
    
    

class type_chambre(models.Model):
    nom = models.CharField(max_length=30)



class client(models.Model):
    nom = models.CharField(max_length=40)
    prenom = models.CharField(max_length=50)
    adresse = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    ville =models.CharField(max_length=20)
    pays = models.CharField(max_length=20)
    
class avis(models.Model):
    avis = models.CharField(max_length=30)
    client_id = models.ForeignKey(client, default=0, on_delete=models.CASCADE)
    
    
class chambre(models.Model):
    date_creation = models.DateTimeField()
    cout = models.IntegerField()
    taille = models.IntegerField()
    type_chambre_id = models.ForeignKey(type_chambre, default=0, on_delete=models.CASCADE)
    photo = models.ImageField(verbose_name='photo de chambre' , default='img_chambre/default.jpg', upload_to='img_chambre') 
    
    def photoUrl(self ):
        try:
            url=self.photo.url 
        except : 
            url="img_chambre/default.jpg"
        return url
    
class location(models.Model):
    date_location = models.DateTimeField(auto_now_add=0)
    date_retour = models.DateTimeField()
    cout = models.IntegerField()
    statu = models.BooleanField(default=0)
    client_id = models.ForeignKey(client, default=0, on_delete=models.CASCADE)
    chambre_id = models.ForeignKey(chambre, default=0, on_delete=models.CASCADE)
    

    