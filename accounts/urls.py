from django.urls import path
from .views import *

urlpatterns = [
    # S I G N U P
    path("signup/", SignupView.as_view(), name="signup"),
]
