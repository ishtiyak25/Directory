from django.http import HttpResponse


def index(request):
    return HttpResponse("Hell. You're at the index Page.")