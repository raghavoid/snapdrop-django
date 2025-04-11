from django.template import loader
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import SignUpForm

def app(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

def upload(request):
    template = loader.get_template('upload.html')
    return HttpResponse(template.render())

def login(request):
    template = loader.get_template('login.html')
    return HttpResponse(template.render())

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'login.html', {'form': form})
