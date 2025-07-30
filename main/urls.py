from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('obituaries/', views.obituaries, name='obituaries'),
    path('obituary/<int:pk>/', views.obituary_detail, name='obituary_detail'),
    path('funeral-planning/', views.funeral_planning, name='funeral_planning'),
    path('arrange-service/', views.arrange_service, name='arrange_service'),
    path('farewell-calculator/', views.farewell_calculator, name='farewell_calculator'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('our-approach/', views.our_approach, name='our_approach'),
]
