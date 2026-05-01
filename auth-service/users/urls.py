from django.urls import path
from .views import logout, register, login, get_me, validate_token, admin_test
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('register', register),
    path('login', login),
    path('me', get_me),
    path('validate', validate_token),
    path('refresh', TokenRefreshView.as_view()),
    path('logout', logout),
    path('admin-test', admin_test),

]

