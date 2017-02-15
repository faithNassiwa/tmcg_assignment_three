from django.shortcuts import render
from models import Group


def index(request):
    groups = Group.objects.all()
    return render(request, 'app/index.html', {'groups': groups})
