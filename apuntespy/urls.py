from django.urls import path
from . import views

app_name='apuntespy'
urlpatterns = [
    # ex: /polls/
    path('', views.IndexView.as_view(), name='tag_list'),
    # ex: /polls/5/
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # ex: /polls/5/results/
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    # ex: /polls/5/vote/
    path('new', views.TipCreateView.as_view(), name='new'),
    path('new-tag', views.TagCreateView.as_view(), name='new-tag'),



]