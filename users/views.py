from multiprocessing import context
from .importation import *
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
@login_required(login_url ='/login')
def index(request):
    try:
        cortn=datacor("tunisia")
        newcases = cortn['active_cases'].replace(',','')
        dig = [s for s in newcases.split() if s.isdigit()]
        cases =dig[0]
        deaths = dig[1]
        
    except:
        newcases='there is a problem'
        cases="there a problem"
        deaths="there a problem"
    users = get_user_model()
    Users =users.objects.all()
    dates=Stock.objects.order_by('last_updated')[0]
    price= Stock.objects.all().aggregate(Sum('issue_quantity'))['issue_quantity__sum']
    artcl = SousFamille.objects.all()
    tasks = Task.objects.all()
    history = Historique_Stock.objects.all()
    restant = Stock.objects.all().aggregate(Sum('quantity'))['quantity__sum']
    cf = Contact.objects.all()
    nbtrans =  history.count()
    tot_articl = artcl.count()
    fourni = cf.count()
    labels = []
    data = []
    requet = Stock.objects.all()
    for societe in requet:
        labels.append(societe.id_sous_famille)
        data.append(societe.issue_quantity)
    datat=dict()
    datat['labels']=labels
    datat['series']=data
    
    lt=0
    perd=[]
    for ob in requet:
        if ob.quantity < ob.id_sous_famille.seuil:
            lt=+1
            ###engine = pyttsx3.init()
            ##engine.setProperty("rate", 148)
            #engine.setProperty('volume',1.0) 
            #engine.say("attention il ya " + (str(ob.id_sous_famille.designation) + " qauntité  " + str(ob.quantity - ob.id_sous_famille.seuil)))
            #engine.runAndWait()
            perd.append(str(ob.id_sous_famille.designation) + " qauntité  " + str(ob.quantity - ob.id_sous_famille.seuil))
    return render(request, "./home/index.html",{"prix":price,"trans":str(nbtrans),"labels":labels,"data":datat,"alert":lt,"list":perd,"stck":requet,"rest":restant,"nbfour":fourni,"nwc":newcases,"Stock":requet,"nbarticle":tot_articl,"last_date":dates,"deaths":deaths,"cases":cases,'tasks':tasks,"allusers":Users})

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "./home/page-sign-in.html", {
                "message": "Invalid credentials."
            })
    else:
        return render(request, "./home/page-sign-in.html")


def logout_view(request):
    logout(request)
    return render(request, "./home/page-sign-in.html", {
        "message": "Logged out."
    })
@login_required(redirect_field_name='login')
def sous_famille(request):
     if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
     form = familleForm()
     return render(request,"./ArticlePage/articles.html",{
         'sous_famille':SousFamille.objects.all(),
         "form":form
     })
@login_required(redirect_field_name='login')
def article_form(request):
    form = sous_familleForm()
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    if request.method == "POST":
         form = sous_familleForm(request.POST)
         if form.is_valid():
             form.save()
             return HttpResponseRedirect(reverse("article"))
    return render(request,"./ArticlePage/form.html",{
     
         "form":form
    })

@login_required
def articleUpdate(request,pk):
    artcl = SousFamille.objects.get(id=pk)
    artcl_form = sous_familleForm(instance=artcl)
    if request.method == "POST":
        artcl_form = sous_familleForm(request.POST,instance=artcl)
        if artcl_form.is_valid():
            artcl_form.save()
            return HttpResponseRedirect(reverse("article"))
    return render(request,"./ArticlePage/form.html",{'form':artcl_form})

@login_required
def articledelete(request,pk):
    Sousfamille = SousFamille.objects.get(id=pk)
    if request.method == 'POST':
        Sousfamille.delete()
        return HttpResponseRedirect(reverse("article"))
    return render(request,"/ArticlePage/articles.html",{"artcl":Sousfamille})

@login_required
def fournisseur(request):
    form = ContactForm()
    
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    if request.method == "POST":
        form =ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("fornisseur"))
    
    return render(request,"./FournisseurPage/fournisseur.html",{
         'fornisseur':Contact.objects.all(),
         "form":form
     })     
@login_required
def contrat(request):
     list_contrat=Contrat.objects.all()
     
     return render(request,"./PageContrat/contrat.html",{
         'contrats':list_contrat
        
     }) 
@login_required
def updateContrat(request, pk):
	task = Contrat.objects.get(id=pk)
	form = ContratForm(instance=task)
	if request.method == 'POST':
		form = ContratForm(request.POST, instance=task)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse("Contrat"))
	context = {'form':form}
	return render(request, 'PageContrat/contratForm.html', context)

@login_required
def deleteContrat(request, pk):
	item = Contrat.objects.get(id=pk)
	if request.method == 'POST':
		item.delete()
		return HttpResponseRedirect(reverse("Contrat"))
	context = {'item':item}
	return render(request, 'PageContrat/contrat.html', context)

@login_required
def stock_ajout(request):
      if request.method == 'GET':
        formset = Formsetst(request.GET or None)
        formi = fornisseurform(request.GET or None)
      elif request.method == 'POST':
        formset = Formsetst(request.POST)
        formi = fornisseurform(request.POST)
        if formi.is_valid():
            facutre = Facture.objects.create(phone_number_id=formi.data["phone_number"],ref=formi.data["ref"],Society=formi.data["Society"],dateen=formi.data['dateen'])   
           
        if formset.is_valid():
            for form in formset:
                famil = form.cleaned_data.get('id_sous_famille')
                quan = form.cleaned_data.get('quantity')
                garantie=form.cleaned_data.get('reorder_level')
                
                if(famil.active == 'oui'):
                     emp = distinations.objects.get(nom_dis='stock')
                     
                     Stock(id_sous_famille=famil,quantity=quan,reorder_level=garantie,issue_to = emp,fac=facutre,ci='consommable').save()
                else:
                    for i in range(0,quan):
                        code=str(form.cleaned_data.get('id_sous_famille'))[0:5] + str(famil.id) + str(i)+str(i+1)+str(quan)+str(facutre.id)
                        Stock(id_sous_famille=famil,quantity=1,issue_quantity=0,receive_quantity=0,reorder_level=garantie,fac=facutre,ci=code).save()
            facutre.save()
           

            return HttpResponseRedirect(reverse('stock_details'))
      return render(request,"./PageStock/AjouterStock.html",{"formset":formset,"form":formi})

@login_required
def stock_details(request):
    tous_article = Stock.objects.all().filter(quantity__gt = 0)
    filtrer = ArticleFilter(request.GET,queryset=tous_article)
   
    s=filtrer.qs.aggregate(Sum('quantity'))['quantity__sum']
    
    
    list_article = filtrer.qs
    
    return render(request,"./PageStock/stock_delais.html",{'Stock':list_article,'filtrer':filtrer,'titre':s})    

@login_required
def receive_items(request, pk):
    queryset=Stock.objects.get(id=pk)
    if request.method == 'GET':
         form=ReceiveForm(request.GET or None,instance=queryset,initial={'receive_quantity':1})
         if(queryset.ci != 'consommable'):
            
             form.fields['receive_quantity'].widget.attrs['readonly']= True
    if request.method == 'POST':
        form=ReceiveForm(request.POST, instance=queryset or None)
      
    if form.is_valid():
      
        instance=form.save(commit=False) 
        if  instance.receive_quantity > instance.issue_quantity:
            return HttpResponse("quantity problem")
        instance.quantity += instance.receive_quantity
        instance.receive_quantity = instance.receive_quantity
        instance.issue_quantity = instance.issue_quantity - instance.receive_quantity
        instance.receive_by=str(request.user)
        instance.save()
        issue_history = Historique_Stock(
	    last_updated = instance.last_updated,
	    id_sous_famille = instance.id_sous_famille,
	    quantity = instance.quantity, 
	    receive_quantity = instance.receive_quantity, 
	    receive_by = instance.receive_by, 
        issue_to = instance.issue_to,
        ci = instance.id,
        codeibar=instance.ci)
        issue_history.save()
        return HttpResponseRedirect(reverse('stock_details'))
    context = {
			"title": 'Reaceive ' + str(queryset.id_sous_famille),
			"instance": queryset,
			"form": form,
           
			"username": 'Recu a: ' + str(request.user)
            }
	
    return render(request, "./PageStock/receive_form.html", context)

@login_required
def chaque_detail(request, pk):
	queryset = Stock.objects.get(id=pk)
	context = {
		"title": queryset.id_sous_famille,
		"queryset": queryset,
	}
	return render(request, "./PageStock/chaque.html", context)

@login_required
def issue_items(request, pk):
    queryset=Stock.objects.get(id=pk)
    form=IssueForm()
    if request.method == 'POST':
        form=IssueForm(request.POST, instance=queryset)
        
        issue_qt = int(request.POST['issue_quantity'])
    if form.is_valid() and issue_qt <= queryset.quantity:
        instance=form.save(commit=False)
        instance.quantity -= int(request.POST['issue_quantity'])
        instance.issue_quantity = instance.issue_quantity + int(request.POST['issue_quantity'])
        
        instance.issue_by=str(request.user)
        instance.issue_to = instance.issue_to
        instance.save()
        messages.success(request, "affecter SUCCESS. " + str(instance.quantity) + " " + str(instance.id_sous_famille) + "est on stock")
        issue_history = Historique_Stock(
	     
	    last_updated = instance.last_updated,
	    id_sous_famille = instance.id_sous_famille,
	    quantity = instance.quantity, 
	    issue_quantity = int(request.POST['issue_quantity']), 
	    issue_by = instance.issue_by, 
        issue_to = instance.issue_to, 
        ci = instance.id,
        codeibar=instance.ci
        
        )
        issue_history.save()
        alertquery = Stock.objects.all()

      
        for alq in alertquery:
            if alq.id_sous_famille.active == "oui" and  alq.quantity < alq.id_sous_famille.seuil:
                email_from = settings.EMAIL_HOST_USER
                try:
                    send_mail("test", "manque de "+ alq.id_sous_famille.designation + "quantite" + str(alq.quantity),email_from,['nasreddine@tanis-tunisie.com'])
                except BadHeaderError:
                    return HttpResponse('Invalid header found.') 
                   
        return HttpResponseRedirect(reverse('stock_details'))

    context = {
			"title": 'Reaceive ' + str(queryset.id_sous_famille),
			"instance": queryset,
			"form": form,
			"username": 'Recu a: ' + str(request.user)
            }
    return render(request, "./PageStock/issue_form.html", context)

@login_required(redirect_field_name='login')  
def ajoutContrat(request):
    form = ContratForm()
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    if request.method == "POST":
        form =ContratForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("Contrat"))
     
    return render(request,"./PageContrat/contratForm.html",{
        
         "form":form
     }) 

@login_required(redirect_field_name='login')
def Historique(request):
	queryset = Historique_Stock.objects.all()
	context = {
		
		"queryset": queryset,
	}
	return render(request, "./PageStock/historique.html", context)

@login_required(redirect_field_name='login')
def retour_details(request):
    tous_article = Stock.objects.filter(issue_quantity__gt=0)
   
    filtrer = ArticleFilter(request.GET,queryset=tous_article)
   
    s=filtrer.qs.aggregate(Sum('quantity'))['quantity__sum']
    
    
    list_article = filtrer.qs
    
    return render(request,"./PageStock/retour_delais.html",{'Stock':list_article,'filtrer':filtrer,'titre':s})   
#########################----------CRUD-Emplacement-----------------------#################
@login_required
def gest_Distinations(request):
    form = DistinationForm()
   
    if request.method == "POST":
         form = DistinationForm(request.POST)
         if form.is_valid():
             form.save()
             return HttpResponseRedirect(reverse("gest_Distinations"))
    return render(request,"./PageDistination/Distinations.html",{
         'emplacement':distinations.objects.all(),
         "form":form
     })
@login_required
def items_Distinations(request):
    items = Stock.objects.filter(issue_quantity__gt=0)
    distination = distinations.objects.all()
   
    return render(request,"./PageDistination/item_emplacement.html",{
         
         'items':items,
         'distinations':distination
              })
@login_required
def DistinationUpdate(request,pk):
    emp = distinations.objects.get(id=pk)
    form = DistinationForm(instance=emp)
    if request.method == "POST":
        form = DistinationForm(request.POST,instance=emp)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("gest_Distinations"))
    return render(request,"./PageDistination/Distinations.html",{"form":form})

@login_required
def deleteDistination(request,pk):
    emp = distinations.objects.get(id=pk)
    if request.method == 'POST':
        emp.delete()
        return HttpResponseRedirect(reverse("gest_Distinations"))
    return render(request,"./PageDistination/Distinations.html",{"distination":emp})




#########################----------BARCODE-----------------------#################
@login_required
def chaque_Barcode(request, pk):
	queryset = Stock.objects.get(id=pk)
	context = {
		"title": queryset.id_sous_famille,
		"queryset": queryset,
	}
	return render(request, "./PageStock/Barcode.html", context)

def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html = template.render(context_dict)
    response = HttpResponse(content_type='application/pdf')
    pdf_status = pisa.CreatePDF(html, dest=response)

    if pdf_status.err:
        return HttpResponse('Some errors were encountered <pre>' + html + '</pre>')

    return response

@login_required
def pdf_view(request, pk):
    template_name = './Pdf_templates/template_facture.html'
    facture_details = Facture.objects.get(id=pk)
    items = Stock.objects.filter(fac__id=pk)
    context = {"ref": facture_details.ref,"societe": facture_details.Society,"date":facture_details.dateen,"fournisseurnom":facture_details.phone_number.nom,"fournisseurmail":facture_details.phone_number.mail,"fac_id": facture_details.id, "items":items}
    return render_to_pdf(template_name,context)
def facture_view(request, pk):
    template_name = './Pdf_templates/viewTemplate.html'
    facture_details = Facture.objects.get(id=pk)
    items = Stock.objects.filter(fac__id=pk)
    context = {"ref": facture_details.ref,"societe": facture_details.Society,"date":facture_details.dateen,"fournisseurnom":facture_details.phone_number.nom,"fournisseurmail":facture_details.phone_number.mail,"fac_id": facture_details.id, "items":items}
    return render(request,template_name,context)

def histbyown(request):     
    data = Historique_Stock.objects.all().values('ci','id_sous_famille__designation','codeibar','id_sous_famille__model').distinct()
    return render(request, "./PageStock/listhistory.html", {"data":data})

def itemhistory(request,pk):     
    infos=Historique_Stock.objects.filter(ci=pk)[0]
    data = Historique_Stock.objects.filter(ci=pk)
    return render(request, "./PageStock/itemhistory.html", {"data":data,"infos":infos})

def item_history_pdf(request,pk): 
    template_name = './Pdf_templates/template_history_item_pdf.html' 
    infos=Historique_Stock.objects.filter(ci=pk)[0]
    data = Historique_Stock.objects.filter(ci=pk)
    context = {"data":data,"infos":infos}
    return render_to_pdf(template_name,context)

#todo goes there===>:

@login_required
def List_tasks(request):
	tasks = Task.objects.all()
	form = TaskForm()
	if request.method =='POST':
		form = TaskForm(request.POST)
		if form.is_valid():
			form.save()
		return HttpResponseRedirect(reverse("list_tasks"))
	context = {'tasks':tasks, 'form':form}
	return render(request, 'todos/list.html', context)

def updateTask(request, pk):
	task = Task.objects.get(id=pk)
	form = TaskForm(instance=task)
	if request.method == 'POST':
		form = TaskForm(request.POST, instance=task)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse("list_tasks"))
	context = {'form':form}
	return render(request, 'todos/list.html', context)

def deleteTask(request,pk):
	item = Task.objects.get(id=pk)
	item.delete()
	return HttpResponseRedirect(reverse("list_tasks"))
	


def cross_on(request,pk):
    item=Task.objects.get(id=pk)
    item.complete=True
    item.save()
    return HttpResponseRedirect(reverse("list_tasks"))

def cross_off(request,pk):
    item=Task.objects.get(id=pk)
    item.complete=False
    item.save()
    return HttpResponseRedirect(reverse("list_tasks"))





def Sortie_stock(request):
    tous_article = Stock.objects.all().filter(quantity__gt = 0)
    if request.method == 'GET':
        filtrer_gat = request.GET.get('filter_gat')
        if filtrer_gat != '' and filtrer_gat is not None:
            tous_article = tous_article.filter(id_sous_famille__active=filtrer_gat)
    s=tous_article.aggregate(Sum('quantity'))['quantity__sum']
    ms = dumps(s)
    context={'list_article':tous_article,"ms":ms}
    return render(request,"./PageStock/Sortie_Stock.html",context)
def users_view(request):
    users_list = User.objects.values()
    context = {'list_users':users_list}
    return render(request,"./PageUser/users_list.html",context)


def add_user(request):
    form = UserForm()
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            role = form.cleaned_data.get('role_field')
            user = User.objects.create(username=username,password=password,is_staff=True,is_active=True)
            user.password = make_password(password)
           
            if role =='2':
                user.is_superuser = True
                user.save()
            else:
                user.save()
            return HttpResponseRedirect(reverse("users"))
    return render(request,"./PageUser/users_form.html",{"form":form})
def update_user(request,pk):
   
    use =User.objects.get(id=pk)
    form = UserForm(instance=use)
    if request.method == "POST":
        form = UserForm(request.POST,instance=use)
        if form.is_valid():
           
            role = form.cleaned_data.get('role_field')
            form.save(commit=False)
           
            if role =='2':
                use.is_superadmin = True
                form.save()
            else:
                form.save()
            return HttpResponseRedirect(reverse("users"))
    return render(request,"./PageUser/users_form.html",{"form":form})
def deleteUser(request, pk):
	user = User.objects.get(id=pk)
	user.is_active = False
	user.save()
	
	return HttpResponseRedirect(reverse("users"))
