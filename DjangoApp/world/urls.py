from django.urls import path
from . import views
from .views import SignUpView

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('pharmacy/', views.Pharmacy.as_view(), name='pharmacy'),
    path('updatedb/', views.update_location, name='updatedb'),
    path('', views.maps, name='maps'),
    path('pharmacy/', views.pharmacy, name='pharmacy'),
    path('signup/', SignUpView.as_view(), name='signup'),
]
