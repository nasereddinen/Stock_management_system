from django.urls import path

from . import Viewfournisseur
from . import viewDisc
from . import viewFamille
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('login',views.login_view,name='login'),
    path('logout',views.logout_view,name="logout"),
    
    path('article',views.sous_famille,name="article"),
    path('article_form',views.article_form,name="article_form"),
    path('articleUpdate/<str:pk>/',views.articleUpdate,name="articleUpdate"),
    path('articledelete/<str:pk>/',views.articledelete,name="articledelete"),
    path('Contrat',views.contrat,name="Contrat"),
    path('ContratUpdate/<str:pk>/',views.updateContrat,name="UpdateContrat"),
    path('ContratDelete/<str:pk>/',views.deleteContrat,name="DeleteContrat"),
    path('stock_details',views.stock_details,name="stock_details"),
    path('stock_ajouter',views.stock_ajout,name="stock_ajout"),
    path('chaque_detail/<str:pk>/',views.chaque_detail,name="chaque_detail"),
    path('issue_items/<str:pk>/',views.issue_items,name="issue_items"),
    path('receive_items/<str:pk>/',views.receive_items,name="receive_items"),
    path('ContratForm',views.ajoutContrat,name="ContratForm"),
    path('Historique',views.Historique,name="Historique"),
    path('retour_details',views.retour_details,name="retour_details"),
    path('chaque_Barcode/<str:pk>/',views.chaque_Barcode,name="chaque_Barcode"),
    path('gest_Distinations',views.gest_Distinations,name="gest_Distinations"),
    path('DistinationUpdate/<str:pk>/',views.DistinationUpdate,name="DistinationUpdate"),
    path('deleteDistination/<str:pk>/',views.deleteDistination,name="deleteDistination"),
    path('gest_familles',viewFamille.famille_list,name="gest_famille"),
    path('famille/create/',viewFamille.famille_create,name="famille_create"),
    path('famille/update/<str:pk>/',viewFamille.update_famille,name="famille_update"),
    path('famille/delete/<str:pk>/',viewFamille.famille_delete,name="famille_delete"),
    path('valid_famille',viewFamille.valid_famille_name,name="valid_famille"),
    path('facture_pdf/<str:pk>/',views.pdf_view,name="facture_pdf"),
    path('disinfect/',viewDisc.datacor,name="datacor"),
    path('fournisseur/',Viewfournisseur.fournisseur_main,name="fournisseur"),
    path('create_fournisseur/',Viewfournisseur.create_fournisseur,name="create_fournisseur"),
    path('update_fournisseur/<str:pk>/',Viewfournisseur.update_fournisseur,name="update_fournisseur"),
    path('delete_fournisseur/<str:pk>/',Viewfournisseur.delete_fournisseur,name="delete_fournisseur"),
    path('listHistory',views.histbyown,name="historybyown"),
    path('itemhistory/<str:pk>/',views.itemhistory,name="itemhistory"),
    path('itemhistory_pdf/<str:pk>/',views.item_history_pdf,name="item_history_pdf"),
    path('list_tasks',views.List_tasks,name="list_tasks"),
    path('tasks_update/<str:pk>/',views.updateTask,name="taskUpdate"),
    path('tasks_delete/<str:pk>/',views.deleteTask,name="taskdelete"),
    path('tasks_cross/<str:pk>/',views.cross_on,name="task_cross"),
    path('tasks_cross_off/<str:pk>/',views.cross_off,name="task_cross_off"),
    path('view_facture/<str:pk>/',views.facture_view,name='facture_view'),
    path('items_emplacment/',views.items_Distinations,name='item_emplacement'),
    path('Sortie_Stock/',views.Sortie_stock,name='Sortie_Stock'),
    path('list_utilisateurs/',views.users_view,name='users'),
    path('users_form/',views.add_user,name='add_users'),
    path('users_update/<str:pk>',views.update_user,name='users_update'),
    path('users_delete/<str:pk>',views.deleteUser,name='users_delete'),

 

    
    
]