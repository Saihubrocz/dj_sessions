from django.shortcuts import render

# Create your views here.
def setsession(request):
    request.session['name'] = 'Sonaliii'
    request.session['lname'] = 'Singha'
    return render(request, 'student/setsession.html')

def getsession(request):
    ame = request.session.get('name')
    lname = request.session.get('lname')
    keys = request.session.keys()
    items = request.session.items()
    age = request.session.setdefault('age','26')
    return render(request,'student/getsession.html',{'nameee':ame,'lname':lname,
    'keys':keys,'items':items,'age':age})  

def delsession(request):
    request.session.flush()
    return render(request,'student/delsession.html')    