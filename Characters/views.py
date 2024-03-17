from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from . import models
from .forms import Character

def home(request):
    return render(request, 'main/home.html',{'title':'Home'})

def create(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            if 'save' in request.POST:
                pk = request.POST.get('save')
                if pk:
                    char = models.Character.objects.get(id=pk)
                    form = Character(request.POST, request.FILES, instance=char)
                else:
                    form = Character(request.POST, request.FILES)
                if form.is_valid():
                    char = form.save()
                    request.user.character.add(char)
                    return render(request, 'main/char.html',{'title':char.name,'char':char})
                else:
                    for field_name, error_messages in form.errors.items():
                     print(f"Error en el campo {field_name}: {error_messages}")
            elif 'delete' in request.POST:
                pk = request.POST.get('delete')
                try:
                    char1 = models.Character.objects.get(id=pk)
                    char1.delete()
                    char = models.Character.objects.all()
                    return render(request, 'main/chars.html',{'title':'Characters', 'char':char})
                except models.Character.DoesNotExist:
                    return HttpResponse("Character does not exist or could not be found.")
            elif 'edit' in request.POST:
                pk = request.POST.get('edit')
                try:
                    char = models.Character.objects.get(id=pk)
                    form = Character(instance=char)
                    return render(request, 'main/create.html',{'title':'Create Character', 'form':form,'char':char})
                except models.Character.DoesNotExist:
                    return HttpResponse("Character does not exist or could not be found.")
            elif 'copy' in request.POST:
                pk = request.POST.get('copy')
                try:
                    char = models.Character.objects.get(id=pk)
                    form = Character(instance=char)
                    if form.is_valid():
                        char_copy = form.save()
                        request.user.character.add(char_copy)
                except models.Character.DoesNotExist:
                    return HttpResponse("Character does not exist or could not be found.")
        else:
            form = Character()
        return render(request, 'main/create.html',{'title':'Create Character', 'form':form})
    else:
        return render(request, 'main/ask.html',{'title':'Info'})

def characters(request):
    if request.user.is_authenticated:
        char = models.Character.objects.all()
        return render(request, 'main/chars.html',{'title':'Characters', 'char':char})
    else:
        return render(request, 'main/ask.html',{'title':'Info'})

def index(request,id):
    char = models.Character.objects.get(id=id)
    return render(request, 'main/char.html',{'title':char.name,'char':char})

def allchar(request):
    char = models.Character.objects.all()
    return render(request, 'main/allchar.html',{'title':'Characters', 'char':char})

def contrib(request):
    return render(request, 'main/contrib.html',{'title':'Contributors'})