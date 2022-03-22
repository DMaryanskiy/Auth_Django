from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from .forms import CreateUserForm


def index(request):
    """ Main page without any functionality """
    return render(request, 'index.html', {})

def registerPage(request):
    """ Register page function. It doesn't open if user is authenticated """
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()

        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                messages.success(request, 'Account was created successfully for ' + username) # flash message after successful registration

                return redirect('login')
        
        return render(request, 'register.html', {'form': form})

def loginPage(request):
    """ Login page function. It doesn't open if user is authenticated """
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None: # if user with given credentials exists
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Username or password is incorrect') # flash message when user gives incorrect credentials
                return render(request, 'login.html', {})

        return render(request, 'login.html', {})

def logoutPage(request):
    """ Logout page function. It uses Django's view for logout """
    logout(request)
    return redirect('login')
