from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request,'input.html')
def calculate(request):
    x=request.GET["t1"]
    y=request.GET["t2"]
    z=int(x)+int(y)
    request.session['z']=z
    request.session.set_expiry(100)
    res=HttpResponse("data submitted successfully")
    res.set_cookie('z',z,max_age=100)
    return res
def display(request):
    if request.session.has_key('z'):
        res=request.session['z']
        return HttpResponse("The sum is:"+str(res))
    else:
        return render(request,'input.html')
