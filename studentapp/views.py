from django.shortcuts import render


# Create your views here.

def home(request):
    return render(request,"studentapp/home.html")

def application(request):
    if request.method == 'POST':
        Student.objects.create(
            name = request.POST["name"],
            email = request.POST["ingredients"],
            department =request.POST["process"],
            mobile = request.POST["mobile"],
        )
      #  return HttpResponseRedirect(reverse("menu:home"))
        return HttpResponseRedirect(reverse("studentapp:apply"))
    return render(request,"studentapp/apply.html")

def details(request):
    



