from django.shortcuts import render
from .models import MyPortfolio


# Create your views here.

def index(request):
    projects = MyPortfolio.objects.all()
    context = {'projects': projects}
    return render(request, 'index.html', context)


def project_detail(request, project_id):
    project = MyPortfolio.objects.get(id=project_id)
    context = {'project': project}
    return render(request, 'project_detail.html', context)
