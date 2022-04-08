from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.template import loader
from .models import Members, Profile
from django.urls import reverse 
from django.views.generic import TemplateView
from django.core.mail import send_mail
from members.forms import LoginForm, ProfileForm

#to display all members
def index(request):
    mymembers = Members.objects.all().values()
    # template = loader.get_template('index.html')
    # context = {
    #     'mymembers':mymembers,
    # }
    return render(request, "index.html", {'mymembers': mymembers})
    # return HttpResponse(template.render(context, request))

# adding member template
def add(request):
    # template = loader.get_template('add.html')
    # return HttpResponse(template.render({}, request))
    return render(request, "add.html", {})
    # return redirect("https://www.google.com")
    # return redirect(delete, id="7")

# to add a new member record
def addrecord(request):   
    received_firstname = request.POST['first'] 
    received_lastname = request.POST['last']

    member = Members(firstname = received_firstname, lastname = received_lastname)
    member.save()
    return HttpResponseRedirect(reverse('index'))   

# to delete a member record
def delete(request, id):
    member = Members.objects.get(id=id)
    member.delete()
    return HttpResponseRedirect(reverse('index'))

# updating member template
def update(request, id):
    mymember = Members.objects.get(id=id)
    template = loader.get_template('update.html')
    context = {
        'mymember': mymember,
    }    
    return HttpResponse(template.render(context, request))

# to update a member record:
def updaterecord(request, id):
    first = request.POST['first']
    last = request.POST['last']
    member = Members.objects.get(id=id)
    member.firstname = first
    member.lastname = last
    member.save()
    return HttpResponseRedirect(reverse('index'))

# to test different queries
# http://127.0.0.1:8000/members/testing_queries/
def testing(request):

# to get all values in table
    # mydata = Members.objects.all().values()

# and/or conditions in filter    
    # mydata = Members.objects.filter(firstname="Rushil", lastname='Agarwal').values() | Members.objects.filter(firstname="Sanjay", lastname='Agarwal').values()

# field lookups    
    # mydata = Members.objects.filter(firstname__startswith='S').values()

#ascending    
    # mydata = Members.objects.all().order_by('firstname').values()

#descending    
    # mydata = Members.objects.all().order_by('-firstname').values() 

# multiple order bys
    mydata = Members.objects.all().order_by('lastname', '-id').values()


    template = loader.get_template('testing_queries.html')
    context = {
        'mymembers': mydata,
    } 
    return HttpResponse(template.render(context, request))


# Django Generic View(Static Files)
class StaticView(TemplateView):
    template_name = 'static.html'


# sending simple HTML E-mail:
def sendEmail(request):
    res = send_mail("hello paul", "paul@polo.com", ["polo@gmail.com"], html_message="Hello my name is Rushil")
    return HttpResponse('%s'%res)


# Django Form Processing
def login(request):
    username = 'not logged in'

    if request.method == 'POST':
        #Get the posted form
        MyLoginForm = LoginForm(request.POST)

        if MyLoginForm.is_valid():
            username = MyLoginForm.cleaned_data['username']
        else:
            MyLoginForm = LoginForm()

    return render(request, 'loggedin.html', {'username':username})            


# Django File Uploading
def SaveProfile(request):
    saved = False

    if request.method == "POST":
        MyProfileForm = ProfileForm(request.POST, request.FILES)

        if MyProfileForm.is_valid():
            profile = Profile()
            profile.name = MyProfileForm.cleaned_data['name']
            profile.picture = MyProfileForm.cleaned_data['picture']
            profile.save()
            saved = True
        else:
            MyProfileForm = ProfileForm()    

    return render(request, 'saved.html', locals())        