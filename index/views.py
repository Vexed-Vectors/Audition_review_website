from multiprocessing import context
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from .models import Question
from django.contrib.auth.models import User,auth
from django.contrib import messages
import time


# Create your views here.
def login(request):
    if request.method == 'POST':
        username= request.POST['username']
        password= request.POST['password']

        user= auth.authenticate(username= username, password=password)

        if user is not None:
            auth.login(request,user)
            
            return redirect('questions/')
        else:
            messages.info(request, 'Invalid Credentials')
            return redirect( '/')
    
    else:
        return render(request, 'login.html')

def sign_up(request):
    return HttpResponse("sign_up yahan")

def questions(request):
   
    
    
    questions= Question.objects.all()
    
    
    

    
    for i in range(1,len(questions)+1):
        response= "response"+str(i)
        if response in request.POST:
            questions[i-1].question_text_response = request.POST[response]
            questions[i-1].save()
        else:
            pass
        
    context={
        'questions': questions,
        

        
        #'time_remaining': timer,
    }

    
    return render (request, 'questions.html', context)

def register(request):
    if request.method== 'POST':
        username= request.POST['username']
        email= request.POST['email']
        password= request.POST['password']
        password2= request.POST['password2']
        first_name= request.POST['first_name']
        last_name= request.POST['last_name']

        if password == password2:
            if User.objects.filter(email = email).exists():
                messages.info(request, 'Email already Used')           
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username already used')
                return redirect('register') 
            elif first_name=="" or last_name=="":
                messages.info(request, 'Please fill in your first name and last name')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, email=email, password= password, first_name= first_name, last_name= last_name )
                user.save(); ######## I DON'T SEE THE POINT OF THE ; USED HERE
                return redirect('login')
        else:
            messages.info(request, 'Password confirmation failed')
            return redirect('register')
    else:
        return render(request, 'signup.html')
    
    