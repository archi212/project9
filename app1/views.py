from django.shortcuts import render

# Create your views here.
def hello(request):
    return render(request,'app1.html')

def hai(request):
     return render(request,'app2.html')   
