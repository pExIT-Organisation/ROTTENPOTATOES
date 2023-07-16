from django.http import HttpResponse
from django.template import loader


def pk_index(request):
    template = loader.get_template('PK-home_page.html')
    return HttpResponse(template.render({}, request))