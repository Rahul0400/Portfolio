from django.http import HttpResponse
from django.shortcuts import render

def aboutus(request):
    return HttpResponse("welcome to rahul this site")

def rahul(request):
    return HttpResponse("rahul this site")

def homepage(request):
    data={
        'title':'home new',
        'bdate':'welcome rahul kumar',
        'slist':['Python','php','Django','C'],
        'student_details':[
            {'name':'Rahul','Phone':'7078244313'},
            {'name':'Ram','Phone':'9012171199'}
        ]
        
    }
    return render(request,"index.html",data)