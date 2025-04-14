from django.template import loader
from django.http import HttpResponse, JsonResponse, FileResponse, Http404
from django.shortcuts import render, redirect
from .forms import SignUpForm
from .models import UploadedFile
from django.core.files.storage import default_storage
from django.conf import settings
from django.db import connection
from django.contrib.auth import authenticate, logout, login as auth_login
from django.contrib.auth.decorators import login_required
import os
from app.models import Login, SignUp

def app(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

@login_required
def upload(request):
    print(request.user.is_authenticated)
    if request.method == 'POST':
        uploaded_file = request.FILES.get('file')
        if uploaded_file:
            # Save the file and track it in the session
            saved_file = UploadedFile.objects.create(file=uploaded_file)
            if 'uploaded_files' not in request.session:
                request.session['uploaded_files'] = []
            request.session['uploaded_files'].append(saved_file.file.path)
            request.session.modified = True
            return redirect('upload')  # Redirect after successful upload 

    files = UploadedFile.objects.all()
    return render(request, 'upload.html', {'files': files})  # Always return a response

@login_required
def download_file(request, file_id):
    try:
        file_entry = UploadedFile.objects.get(id=file_id)
        file_path = file_entry.file.path
        return FileResponse(open(file_path, 'rb'), as_attachment=True,filename=file_entry.file.name)
    except UploadedFile.DoesNotExist:
        raise Http404("File does not exist")
    except FileExistsError:
        raise Http404("File not found on the server")

def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = Login.objects.get(email=email)
            if user.check_password(password):
                auth_login(request, user) #Log the user in
                return redirect('/')
            else:
                return render(request, 'login.html', {'error': 'Invalid password'})
        except Login.DoesNotExist:
            return render(request, 'signup.html', {'error': 'User does not exist'})

    return render(request, 'login.html')  # Render the login page


def signup_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        if Login.objects.filter(email=email).exists():
            return render(request, 'signup.html', {'alert': 'Email already exists'})

        user = Login(email=email)
        user.set_password(password)
        user.save()

        return redirect('login')  # Redirect to the login page after signup
    return render(request, 'signup.html')  # Render the signup page

def logout_view(request):
    logout(request)
    return redirect('/')


def cleanup_database(request):
    media_root = settings.MEDIA_ROOT
    deleted_files = []

    for file_entry in UploadedFile.objects.all():
        file_path = os.path.join(media_root, file_entry.file.name)
        if not os.path.exists(file_path):
            deleted_files.append(file_entry.file.name)
            file_entry.delete()
    with connection.cursor() as cursor:
        cursor.execute("UPDATE sqlite_sequence SET seq = (SELECT MAX(id) FROM app_uploadedfile) WHERE name = 'app_uploadedfile'")
        
    return JsonResponse({'status': 'success', 'deleted_files': deleted_files})