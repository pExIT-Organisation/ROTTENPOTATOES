from django.http import HttpResponse


def pk_index(request):
    return HttpResponse("Pawel's concept page")