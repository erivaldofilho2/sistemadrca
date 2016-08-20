# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http.response import HttpResponse
from django.template import RequestContext, loader
from coredrca.models import Aluno
from datetime import datetime

# Create your views here.
def home(request):
    template = loader.get_template('index.html')
    context = RequestContext(request)
    return HttpResponse(template.render(context))

def alunos(request):
    alunos = Aluno.objects.all()
    teste = 'Alunos'
    template = loader.get_template('alunos.html')
    context = RequestContext(request,{'alunos':alunos})
    return HttpResponse(template.render(context))
    