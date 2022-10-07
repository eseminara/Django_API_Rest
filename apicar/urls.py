from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('autos/', views.autos_list),
    path('autos/<int:id>', views.autos_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)