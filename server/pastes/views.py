from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Paste, Language
from .forms import  PasteForm
from django.views.generic import DetailView, ListView, CreateView

def index(request):
    return render(request, 'pastes/index.html')

class PasteView(ListView):
    model = Paste
    template_name = 'paste_list.html'

class PasteDetail(DetailView):
    model = Paste
    template_name = 'paste_detail.html'

def PasteAddView(request):
    form = PasteForm(request.POST or None)
    if request.method=='POST':
        title = request.POST['title']
        user = request.user
        content = request.POST['content']
        paste = Paste.objects.create(title = title, author = user, content = content)
        paste.save()
        return redirect('/')
    else:
        return render(request, 'paste_add.html', {'form': form})

class LanguageAddView(CreateView):
    model = Language
