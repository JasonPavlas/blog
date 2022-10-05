from django.shortcuts import render, redirect 
from django.contrib.auth.forms  import UserCreationForm 
from django.contrib import messages

        ###this definition maps to a file in the users/remplates/users directory
        ###(request) are the hppt requests from the browser 
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleanded_data.get('username')
            messages.success(request, f'Account created for {username}!')
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form})

