from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import CustomUserCreationForm

def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        print('Invalid form')
    else:
        form = CustomUserCreationForm()
    return render(request, 'users/register.html', {'form': form})

def login_view(request):
    messages = []
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            print("teste")
            return redirect('home')
        
        messages.append("Invalid email or password")

    return render(request, 'users/login.html', { 'messages': messages, 'have_messages': len(messages) > 0 })

def logout_view(request):
    logout(request)
    return redirect('login')
