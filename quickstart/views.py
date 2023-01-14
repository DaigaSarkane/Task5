from django.http import HttpResponse, JsonResponse, FileResponse
from django.shortcuts import render
from datetime import datetime
from django.template import Template, Context


def home(request):
    return render(request, "home.html")


def hello(request):
    return HttpResponse("Hellooo")


def messages(request):
    datalist = []
    if request.method == "POST":
        userA = request.POST.get("userA", None)
        userB = request.POST.get("userB", None)
        message = request.POST.get("message", None)
        time = datetime.now()
        with open("msgdata.txt", "a+") as f:
            f.write("{}--{}--{}--{}--\n".format(userB, userA, message, time.strftime("%Y-%m-%d %H:%M:%S")))
    if request.method == "GET":
        userC = request.GET.get("userC", None)
        if userC is not None:
            with open("msgdata.txt", 'r') as f:
                cnt = 0
                for line in f:
                    linedata = line.split('--')
                    if linedata[0] == userC:
                        cnt = cnt + 1
                        d = {"userA": linedata[1], "message": linedata[2], 'time': linedata[3]}
                        datalist.append(d)
                    if cnt >= 20:
                        break
    return render(request, "msgSingleWeb.html", {"data": datalist})


def httpresponse(request):
    response = HttpResponse()
    response.write("<h1>Homepage created with HttpResponse</h1>")
    response.write("<p>Random text</p>")
    return response


def jsonresponse(request):
    response = JsonResponse({'key': 'value',
                             'key1': 'value2'})
    return response


def fileresponse(request):
    img = open('quickstart/templates/randomImage.png', 'rb')
    response = FileResponse(img)
    return response


def httptemplate(request):
    template = Template("<h1>This is a template with context: {{ randomContext }}</h1>")
    context = Context({"randomContext": "Useless text"})
    return HttpResponse(template.render(context))
