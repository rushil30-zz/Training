from django.http import HttpResponse, HttpResponseRedirect
# from django.shortcuts import render
from django.template import loader
from .models import Members
from django.urls import reverse 

#to display all members
def index(request):
    mymembers = Members.objects.all().values()
    template = loader.get_template('index.html')
    context = {
        'mymembers':mymembers,
    }
    return HttpResponse(template.render(context, request))

# adding member template
def add(request):
    template = loader.get_template('add.html')
    return HttpResponse(template.render({}, request))

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
