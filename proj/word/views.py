from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Word
from .forms import *


def my_view(request):
    message = 'Выберите файл'
    # Handle file upload
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Word(docfile=request.FILES['docfile'])
            newdoc.save()

            # Redirect to the document list after POST
            return redirect('my-view')
        else:
            message = 'The form is not valid. Fix the following error:'
    else:
        form = DocumentForm()  # An empty, unbound form

    # Load documents for the list page
    documents = Word.objects.all()

    # Render list page with the documents and the form
    context = {'documents': documents, 'form': form, 'message': message, }
    return render(request, 'list.html', context)


def load(request):
    if request.method == 'POST':
        f = open(request.FILES)
        text = f.read()
        text = text.replace("\n", " ")
        text = text.replace(",", "").replace(".", "").replace("?", "").replace("!", "").replace("—", "")
        text = text.lower()
        words = text.split()
        return HttpResponse(words)
