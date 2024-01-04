from django.shortcuts import render
from django.views import generic


class AdminPanelView(generic.TemplateView):

    def get(self, request, *args, **kwargs):
        return render(request, 'adminPanel/index.html')
