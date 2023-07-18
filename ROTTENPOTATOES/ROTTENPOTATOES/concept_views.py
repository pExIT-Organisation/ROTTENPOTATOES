from django.shortcuts import render


def pk_index(request):
    return render(request, 'PK-home_page.html')

def pk_film_ranking(request):
    return render(request, 'PK-film_ranking.html')

def pk_quiz(request):
    return render(request, 'PK-quiz.html')
