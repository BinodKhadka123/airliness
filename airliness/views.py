from django.shortcuts import render
def homepage(request):
    return render(request,"index_4.html")

def login(request):
    return render(request,"login.html")
def book(request):
    return render(request,"book.html")
    