from django.urls import path

from . import views

app_name = 'search'
urlpatterns = [
                path('<search_id>/', views.search_id, name='search_id')
        ]
