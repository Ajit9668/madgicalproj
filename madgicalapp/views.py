from django.shortcuts import render
from django.http import HttpResponse
from .models import Issue
def createTicketView(request):
    if request.method=='GET':
        return render(request,'madgicalapp/create_ticket.html')
    else:
        Issue(number=request.POST["key"],
                name=request.POST["fields"]["summary"],
                description=request.POST["fields"]["description"],
                reporter=request.POST["fields"]["reporter"]["name"],
                status=request.POST["fields"]["status"]["name"],
                due_date=request.POST["fields"]["duedate"],).save()
        return HttpResponse('Data Saved In Database')

def showData(request):
    if request.method=='GET':
        alldata=Issue.objects.all()
        return render(request, 'madgicalapp/show_ticket.html',{'alldata':alldata})
        