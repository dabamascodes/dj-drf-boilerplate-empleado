from django.urls import path
from django.views.generic import RedirectView
from . import views

urlpatterns = [
    path('', RedirectView.as_view(url='/admin/', permanent=False)),
    path('home/', views.IndexView.as_view()),
    path('lista/', views.PruebaListView.as_view()),    
    path('lista-prueba/', views.ModeloPruebaListView.as_view()),    

]
