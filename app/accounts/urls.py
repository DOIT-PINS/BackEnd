from django.urls import path, include
from . import views
from rest_framework import urls

urlpatterns =[
    path('signup/', views.UserCreate.as_view()),
    path('login/', include('rest_framework.urls')),
    path('dj-rest-auth/', include('dj_rest_auth.urls'))
    # path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls'))
 ]