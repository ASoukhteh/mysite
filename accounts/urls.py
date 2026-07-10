from django.urls import path
from accounts import views 

app_name = 'accounts'

urlpatterns = [
    path('login/', views.login_view, name='login'), 
    path('logout/', views.logout_view, name='logout'), 
    path('signup/', views.login_view, name='signup'), 
]