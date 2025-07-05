from django.urls import path
from .views import auth__views
authViews= auth__views()

urlpatterns=[
    path('login/', authViews.loginPage, name='loginPage'),
    path('logout', authViews.logout, name='logout'),
    path('register', authViews.registerPage, name='registerPage'),
    path('log', authViews.login, name='login'),
    path('reg', authViews.register, name='register'),
    
]