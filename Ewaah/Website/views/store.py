from django.db import models
from django.shortcuts import render
from django.views import View

class Store(View):

    def get(self, request):
        return render(request, 'storepage.html' )