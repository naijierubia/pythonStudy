from django.http import HttpResponse


def page_001_view(request):
    return HttpResponse("page001")


def pageN_view(request, pageNumbers):
    return HttpResponse("page" + str(pageNumbers))


def add_view(request, NumberA, NumberB):
    return HttpResponse(str(int(NumberA) + int(NumberB)))


def birthday_view(request, year, month, day):
    return HttpResponse("Happy " + str(year) + " " + str(month) + " " + str(day))
