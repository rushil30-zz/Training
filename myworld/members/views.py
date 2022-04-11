from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.template import loader
from .models import Members, Profile
from django.urls import reverse 
from django.views.generic import TemplateView
from django.core.mail import send_mail
from members.forms import LoginForm, ProfileForm
from django.views.decorators.csrf import csrf_exempt
from members.serializer import MembersSerializer
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from rest_framework.decorators import api_view

#to display all members
def index(request):
    mymembers = Members.objects.all().values()
    # print((mymembers))
    return render(request, "index.html", {'mymembers': mymembers})

# adding member template
def add(request):
    return render(request, "add.html", {})

# to add a new member record
@csrf_exempt
@api_view(("GET","POST"))
def add_record(request): 
    if request.method == 'GET':
        return HttpResponseRedirect(reverse('index'))

    elif request.method == 'POST':
        members = request.data
        print(members)
        serializer = MembersSerializer(data=members)
        if serializer.is_valid():
            print("Helloo")
            serializer.save()
        else:
            print((serializer.errors))
            return Response(data = serializer.errors, status=400) 
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


# sending simple E-mail:
def sendEmail(request):
    print("Workingg.....")
    res = send_mail('Subject here', 'Here is the message.', 'agarwalrushil98@gmail.com', ['agarwalrushil98@gmail.com'],fail_silently=True)
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


from django.core.mail import EmailMessage
from django.shortcuts import render, HttpResponse, HttpResponseRedirect

from .forms import SendMailForm


# Create your views here.
def simple_send_mail(request):
    if request.method == 'POST':
        fm = SendMailForm(request.POST or None, request.FILES or None)
        if fm.is_valid():
            subject = fm.cleaned_data['subject']
            message = fm.cleaned_data['msg']
            from_mail = 'agarwalrushil@98gmail.com'
            print(from_mail)
            to_mail = fm.cleaned_data['email_id']
            to_cc = fm.cleaned_data['email_cc']
            to_bcc = fm.cleaned_data['email_bcc']
            print(fm.cleaned_data)
            attach = fm.cleaned_data['attachment']
            if from_mail and to_mail:
                try:
                    mail = EmailMessage(subject=subject, body=message, from_email=from_mail, to=[to_mail], bcc=[to_bcc],
                                        cc=[to_cc]
                                        )
                    mail.attach(attach.name, attach.read(), attach.content_type)
                    mail.send()
                # except Exception as ex:
                except ArithmeticError as aex:
                    print(aex.args)
                    return HttpResponse('Invalid header found')
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse('Make sure all fields are entered and valid.')
    else:
        fm = SendMailForm()
    return render(request, 'send_mail.html', {'fm': fm})
