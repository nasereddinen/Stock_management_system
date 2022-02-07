
from django.db import models
from datetime import datetime, date

# Create your models here.
class Familles(models.Model):
    famille = models.CharField(max_length=50)
    class Meta:
        managed = True
        db_table = 'familles'
    def __str__(self):
        return self.famille


class Contact(models.Model):
    fournisseur = models.CharField(max_length=80,unique=True)
    nom = models.CharField(max_length=80)
    adresse = models.CharField(max_length=250,blank=True, null=True)
    tel1 = models.CharField(max_length=50,blank=True, null=True)
    tel2 = models.CharField(max_length=50,blank=True, null=True)
    tel3 = models.CharField(max_length=50,blank=True, null=True)
    fax = models.CharField(max_length=50,blank=True, null=True)
    mail = models.CharField(max_length=80,blank=True, null=True)
    activite = models.CharField(max_length=80,blank=True, null=True)
    obs = models.CharField(max_length=250,blank=True, null=True)
    ville = models.CharField(max_length=20,blank=True, null=True)

    def __str__(self):
        return self.nom
class SousFamille(models.Model):
    choix = (
        ('oui', 'oui'),
        ('non', 'non'),
    )
    choix_ville = (
        ('tunis', 'tunis'),
        ('sousse', 'sousse'),
        ('nice','nice'),
    ),
    id_famille = models.ForeignKey(Familles,verbose_name="Les Articles",on_delete=models.CASCADE)
    designation = models.CharField(max_length=20)
    marque = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    seuil = models.IntegerField()
    pid1 = models.CharField(max_length=20,unique=True)
    active = models.CharField(max_length=3,verbose_name="consommable",choices=choix)
    ville = models.CharField(max_length=6,blank=True, null=True)
    def __str__(self):
        return self.designation[0:4] + ': ' + self.model 
class Contrat(models.Model):
    choix_ville = (
        ('tunis', 'tunis'),
        ('sousse', 'sousse'),
        ('nice','nice'),
    )
    article = models.ForeignKey(SousFamille,on_delete=models.CASCADE)
    designation = models.CharField(max_length=20)
    fournisseur = models.ForeignKey(Contact,on_delete=models.CASCADE)
    dateacquisition = models.DateField(db_column='dateAcquisition',blank=True, null=True)  # Field name made lowercase.
    echeance = models.DateField(blank=True, null=True)
    montant = models.CharField(max_length=20)   
    observation = models.CharField(max_length=20,blank=True, null=True)
    ville = models.CharField(max_length=6,choices=choix_ville)

class Facture(models.Model):
    choix_societe = (
        ('argos', 'argos'),
        ('jupiter', 'jupiter'),
        ('ithaque','ithaque'),
        ('tanis','tanis'),
        
    )
    phone_number = models.ForeignKey(Contact,verbose_name="fournisseur",on_delete=models.CASCADE)
    ref = models.CharField(max_length=50,default='0',verbose_name='Réference facture', blank=True, null=True)
    Society = models.CharField(max_length=50,default='0', blank=True, null=True,choices=choix_societe)
    dateen = models.DateField()
    
class distinations(models.Model):
    nom_dis = models.CharField(max_length=50,unique=True)
    def __str__(self):
        return self.nom_dis
    
class Stock(models.Model):
    id_sous_famille = models.ForeignKey(SousFamille,verbose_name="Article",on_delete=models.CASCADE)
    quantity = models.IntegerField(blank=True, null=True)
    receive_quantity = models.IntegerField( blank=True, null=True)
    receive_by = models.CharField(max_length=50, blank=True, null=True)
    issue_quantity = models.IntegerField(default=0,blank=True, null=True)
    issue_by = models.CharField(max_length=50, blank=True, null=True)
    issue_to = models.ForeignKey(distinations,verbose_name="Emplacement",on_delete=models.CASCADE,default=1)
    fac =  models.ForeignKey(Facture,on_delete=models.CASCADE)
    created_by = models.CharField(max_length=50, blank=True, null=True)
    reorder_level = models.IntegerField(default='0',verbose_name="garantie", blank=True, null=True)
    last_updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    ci=models.CharField(max_length=50, blank=True, null=True)
    def __str__(self):
        return self.id_sous_famille
	

class Historique_Stock(models.Model):
	codeibar=models.CharField(max_length=50, blank=True, null=True)
	id_sous_famille = models.ForeignKey(SousFamille,on_delete=models.CASCADE)
	quantity = models.IntegerField(default='0', blank=True, null=True)
	receive_quantity = models.IntegerField(default='0', blank=True, null=True)
	receive_by = models.CharField(max_length=50, blank=True, null=True)
	issue_quantity = models.IntegerField(default='0', blank=True, null=True)
	issue_by = models.CharField(max_length=50, blank=True, null=True)
	issue_to = models.CharField(max_length=50,blank=True, null=True)
	ci=models.CharField(max_length=50, blank=True, null=True)
	created_by = models.CharField(max_length=50, blank=True, null=True)
	reorder_level = models.IntegerField(default='0', blank=True, null=True)
	last_updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    
class Task(models.Model):
	title = models.CharField(max_length=200)
	complete = models.BooleanField(default=False)
	created = models.DateTimeField(auto_now_add=True)
	by = models.CharField(max_length=50, blank=True, null=True)
    
