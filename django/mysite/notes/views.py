from django.shortcuts import render
from django.http import HttpResponse

# import models
from .models import Note

from rest_framework import viewsets
from .serializers import NoteSerializer

def index(request):
    # Получить все заметки:
    notes = Note.objects.all()

    context = {
        'notes': notes
    }
    return render(request, 'notes/index.html', context)


class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all().order_by('-created_at')
    serializer_class = NoteSerializer