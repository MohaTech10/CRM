from django.shortcuts import render



def homePage(request):
    return render(request, 'DashBoard.html')

def productsPaeg(request):
    return render(request, 'Products.html')
