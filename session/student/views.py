from django.shortcuts import render

# Create your views here.
def setsession(request):
    request.session['name'] = 'Sonali'
    request.session['lname'] = 'Bindre'
    return render(request, 'student/setsession.html')

def getsession(request):
    name = request.session['name']
    lname = request.session['lname']
    return render(request,'student/getsession.html',{'name':name,'lname':lname})  

def delsession(request):
    if 'name' in request.session:
        del request.session['name']      
    return render(request,'student/delsession.html')    