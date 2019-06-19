from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm


# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(
                request, f'Welcome to HOMEBRU { username }, your account has successfully been created!')

            return redirect('home')
    else:
        form = UserRegisterForm()

    return render(request, 'users_register.html', {'form': form})
