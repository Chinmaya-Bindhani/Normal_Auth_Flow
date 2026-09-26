from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import get_user_model,login,logout,authenticate
from . forms import  UserRegisterForm , MyLoginForm
from django.contrib.auth.decorators import  login_required


# REGISTER VIEW
def register_view(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        else:
            return redirect('register')
    else:
        form = UserRegisterForm()
        return render(request,'register.html',context={"form":form})

#LOGIN FORM
def login_view(request):
    if request.method == "POST":
        form = MyLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request,email=email,password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                form.add_error(None,'Invalid email or password')
        return render(request,'login.html', context={"form":form})
    else :
         form = MyLoginForm()
         return render(request,'login.html', context={"form":form})


#LOGOUT VIEWS
@login_required()
def logout_view(request):
    logout(request)
    return redirect("login")
#HOME VIEWS
@login_required()
def home(request):
    return render(request,'home.html',context={"user":request.user})