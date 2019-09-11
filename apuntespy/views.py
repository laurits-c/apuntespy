from django.http import HttpResponse
from .models import Tag, Tip
from django.views import generic
from django import forms


class IndexView(generic.ListView):
    template = 'apuntespy/index.html'
    context_object_name = 'tags'
    def get_queryset(self):
        return Tag.objects.all()

class DetailView(generic.DetailView):
    model = Tag
    template_name = 'apuntespy/detail.html'

class ResultsView(generic.DetailView):
    model = Tip
    template_name = 'apuntespy/result.html'

class TipCreateView(generic.edit.CreateView):
    model = Tip
    fields = ['tip_nombre', 'tip_descripcion', 'tip_ejemplo', 'tags']

    def form_valid(self, form):
        return super().form_valid(form)

class TagCreateView(generic.edit.CreateView):
    model = Tag
    fields = ['tag_text']

    def form_valid(self, form):
        return super().form_valid(form)