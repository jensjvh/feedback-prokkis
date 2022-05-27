from django.http import HttpResponse


def index(request):
    # print(request.)
    if request.method == "POST":
        test = request.POST["numero1"]
        print(test)

    return HttpResponse("Hello lol")
