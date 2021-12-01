from django.urls import path

from .views import *

urlpatterns = [
    path('register/', Registration.as_view()),
    path('activation/', Activation.as_view()),
    path('login/', LoginView.as_view()),
    path('logout/', LogoutView.as_view())
]
