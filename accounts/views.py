from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login


def register(request):
    if request.user.is_authenticated:
        return redirect("bookly_nest:index")

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("bookly_nest:index")
    else:
        form = UserCreationForm()

    context = {
        "form": form,
    }
    return render(request, "registration/register.html", context=context)
