from django.urls import path
from snippets import views

urlpatterns = [
    path('', views.SnippetList.as_view(), name='snippet-list'),
]