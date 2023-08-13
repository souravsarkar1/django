from django.http import HttpResponse


def aboutUs(request):
    return HttpResponse("welcome to my website!")