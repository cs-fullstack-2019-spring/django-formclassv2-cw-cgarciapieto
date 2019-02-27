from django.shortcuts import render
from django.http import HttpResponse
from .forms import EmployeeForm



# Create your views here.
def index(request):
    return HttpResponse("testing index")


# function that sends the post to to the results html page


def apply(request):
    # return HttpResponse("testapply")

    if(request.method == 'POST'):

        context = {"name": request.POST["name"]}
        return render(request, "employeeApp/results.html", context)
    else:
        newForm = EmployeeForm()
        context = {
            "newForm": newForm,
        }
        return render(request, "employeeApp/index.html", context)

