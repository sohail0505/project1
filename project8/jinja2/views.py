from django.shortcuts import render

# Create your views here.
def conditions(request):
    d={'name':'sohail','age': 90,'gender':'male'}
    return render(request,'conditions.html',context=d)
