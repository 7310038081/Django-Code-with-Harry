from django.shortcuts import render,HttpResponse

# Create your views here.

def index(request):
    context = {
    "variable1":"Aman is great",
    "variable2":"Vivek is great"
    }
    return render(request,'index.html',context)
    # return HttpResponse("This is HomePage")

def about(request):
    return render(request,'about.html')

def services(request):
    return render(request,'services.html')

def contact(request):
    return render(request,'contact.html')

