from django.shortcuts import render


def movie1(request):
    return render(request, 'base.html', {})
