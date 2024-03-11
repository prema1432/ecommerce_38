from django.shortcuts import render, redirect

from user.forms import CustomUserForm


# Create your views here.


def register_user(request):
    context = {}
    if request.method == "POST":
        form = CustomUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.roles = "rider"
            user.save()

            return redirect('index')
    else:
        form = CustomUserForm()
    context["form"] = form
    return render(request, 'register_user.html', context)
