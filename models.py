# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group_id = models.IntegerField()
    permission_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group_id', 'permission_id'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type_id = models.IntegerField()
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type_id', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user_id = models.IntegerField()
    group_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user_id', 'group_id'),)


class AuthUserUserPermissions(models.Model):
    user_id = models.IntegerField()
    permission_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user_id', 'permission_id'),)


class Contact(models.Model):
    fournisseur = models.CharField(max_length=80)
    nom = models.CharField(max_length=80)
    adresse = models.CharField(max_length=250)
    tel1 = models.CharField(max_length=50)
    tel2 = models.CharField(max_length=50)
    tel3 = models.CharField(max_length=50)
    fax = models.CharField(max_length=50)
    mail = models.CharField(max_length=80)
    activite = models.CharField(max_length=80)
    obs = models.CharField(max_length=250)
    ville = models.CharField(max_length=6)

    class Meta:
        managed = False
        db_table = 'contact'


class Contrat(models.Model):
    article = models.TextField()
    designation = models.TextField()
    fournisseur = models.IntegerField()
    dateacquisition = models.DateField(db_column='dateAcquisition')  # Field name made lowercase.
    echeance = models.DateField()
    montant = models.TextField()
    observation = models.TextField()
    ville = models.CharField(max_length=6)

    class Meta:
        managed = False
        db_table = 'contrat'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type_id = models.IntegerField(blank=True, null=True)
    user_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class EntreeStock(models.Model):
    id_sous_famille_id = models.IntegerField()
    pid = models.CharField(max_length=20)
    numero_serie = models.TextField()
    id_fournisseur = models.IntegerField()
    date_entree = models.DateTimeField(blank=True, null=True)
    bl = models.CharField(max_length=20)
    facture = models.CharField(max_length=20)
    quantite = models.IntegerField()
    prix = models.CharField(max_length=5)
    garantie = models.IntegerField()
    date_deb_gar = models.DateField(blank=True, null=True)
    societe = models.CharField(max_length=13)
    whomodif = models.CharField(max_length=20)
    date_modif = models.DateTimeField(blank=True, null=True)
    num_bon = models.CharField(max_length=20)
    ville = models.CharField(max_length=6)

    class Meta:
        managed = False
        db_table = 'entree_stock'


class Familles(models.Model):
    famille = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'familles'


class Log(models.Model):
    who = models.CharField(max_length=20)
    what = models.CharField(max_length=50)
    detail = models.CharField(max_length=300)
    when = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'log'


class ReparationMat(models.Model):
    id_sous_famille = models.IntegerField()
    pid = models.CharField(max_length=25)
    date_sortie = models.DateField()
    fournisseur = models.IntegerField()
    obs = models.TextField()
    date_modif = models.DateTimeField()
    whomodif = models.TextField()
    num_bon = models.TextField()
    ville = models.CharField(max_length=6)

    class Meta:
        managed = False
        db_table = 'reparation_mat'


class SortiPlateau(models.Model):
    id_sorti_stock = models.IntegerField()
    id_entree_stock = models.IntegerField()
    ancien_etat = models.TextField()
    nouvelle_etat = models.IntegerField()
    quantite = models.IntegerField()
    date_sortie_plateau = models.DateField()
    obs = models.TextField()
    date_modif = models.DateTimeField()
    whomodif = models.TextField()
    num_bon = models.TextField()
    ville = models.TextField()

    class Meta:
        managed = False
        db_table = 'sorti_plateau'


class SortiStock(models.Model):
    id_entree_stock = models.IntegerField()
    date_sorti = models.DateField()
    quantite = models.IntegerField()
    lieu = models.CharField(max_length=10)
    obs = models.TextField()
    whomodif = models.CharField(max_length=10)
    date_modif = models.DateTimeField()
    num_bon = models.CharField(max_length=20)
    etat = models.CharField(max_length=1)
    ville = models.CharField(max_length=6)
    responsable = models.TextField()
    voyant = models.TextField()
    nom_voyant = models.TextField()
    prenom_voyant = models.TextField()

    class Meta:
        managed = False
        db_table = 'sorti_stock'


class SousFamille(models.Model):
    id_famille_id = models.IntegerField()
    designation = models.CharField(max_length=20)
    marque = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    seuil = models.IntegerField()
    pid1 = models.CharField(max_length=20)
    active = models.CharField(max_length=3)
    ville = models.CharField(max_length=6)

    class Meta:
        managed = False
        db_table = 'sous_famille'


class Users(models.Model):
    login = models.CharField(max_length=50)
    mdp = models.CharField(max_length=50)
    site = models.CharField(max_length=6)
    droit = models.CharField(max_length=11)
    active = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'users'
