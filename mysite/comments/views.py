from django.views.generic.list import ListView
from django.shortcuts import render

class Index(ListView):
    def get(self, req):
        return render(req, 'comments/index.html')

class Store(ListView):
    def post(self, req):
        pass
    