from django.shortcuts import render , redirect
from django.http import HttpResponse
from .models import Member
from django.contrib import messages
# Create your views here.
def members(request):
    members = Member.objects.all()  
    return render(request, 'members/home.html', {'members': members})

def add_member(request):
    if request.method == 'POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        age = request.POST.get('age')

        Member.objects.create(fname=fname, lname=lname, age=age)
        messages.success(request, 'Member added successfully!')
        return redirect('form')
        
    return  render (request, 'members/form.html')   
