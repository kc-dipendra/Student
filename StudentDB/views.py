from django.http import HttpResponse
from django.shortcuts import render

def homePage(request):
    data={
        'title':'Home Page',
        'bdata': 'Welcome to Harvard',
    }
    return render(request,"index.html",data)
 
def aboutUs(request):
    return HttpResponse("<b> Let us learn more about Harvard Academy. </b>")

def course(request):
    return HttpResponse("We provide following Courses.")

def courseDetails(request,courseid):
    return HttpResponse(courseid)
