from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login


def cichy(request):
    return render(request, 'AC-base_concept.html')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('cichy')  # Redirect to the homepage after successful registration
    else:
        form = UserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})
