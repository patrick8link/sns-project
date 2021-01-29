from django.urls import path

from . import views
from haystack.views import SearchView

app_name = 'search'
urlpatterns = [
                path('<search_id>/', views.search_id, name='search_id'),
		path('', SearchView(), name="haystack_search"),
        ]
