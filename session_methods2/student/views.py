from django.shortcuts import render

# Create your views here.
def settestcookie(request):
    request.session.set_test_cookie()
    return render(request,'student/settestcookie.html')

def settestcookie(request):
    request.session.set_test_cookie()
    return render(request,'student/settestcookie.html')

def checktestcookie(request):
    print(request.session.test_cookie_worked())
    return render(request,'student/checktestcookie.html')

def deltestcookie(request):
    request.session.del_test_cookie()
    return render(request,'student/deltestcookie.html')

