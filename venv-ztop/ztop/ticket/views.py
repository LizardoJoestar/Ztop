from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    #return HttpResponse("Ticket Generation Form Goes Here:")
    #if(request.method=='POST'):
     #   ID_req = request.POST.get('name')
      #  ID_tech = request.POST.get('name')
       # assigned = models.BooleanField()
        #dateCreation = models.DateTimeField('Date created')
        #dateAssign = models.DateTimeField('Date assigned', null=True, blank=True)
        #dateFinish = models.DateTimeField('Date finished', null=True, blank=True)

    return render(request, 'ticket/ticket.html')