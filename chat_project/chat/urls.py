from django.urls import path
from . import views

app_name = 'chat'
urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('chat/', views.chat, name='chat'),
]
