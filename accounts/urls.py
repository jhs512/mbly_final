from django.contrib.auth import views as auth_views
from django.urls import path, reverse_lazy
from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView

from . import views
from .forms import MyPasswordResetForm
from .views import MyTokenObtainPairView, MyPasswordResetView, MyPasswordResetConfirmView

app_name = 'accounts'

urlpatterns = [
    path('login/', views.login, name='login'),
    path('join/', views.join, name='join'),
    path('edit/', views.edit, name='edit'),
    path('logout/', views.logout, name='logout'),
    path('find_username/', views.find_username, name='find_username'),
    path('login/kakao/', views.kakao_login, name="kakao_login"),
    path('login/kakao/callback/', views.kakao_login_callback, name="kakao_login_callback"),
    path('api/token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/access_token/', TokenRefreshView.as_view(), name='token_refresh_access_token'),
    path('api/token/refresh/refresh_token/', views.ApiRefreshRefreshTokenView.as_view(),
         name='token_refresh_refresh_token'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('reset_password/', MyPasswordResetView.as_view(
        success_url=reverse_lazy('accounts:login'),
        template_name='accounts/password_reset_form.html',
        email_template_name='accounts/password_reset_email.html',
        form_class=MyPasswordResetForm,
    ), name='reset_password'),
    path('reset/<uidb64>/<token>', MyPasswordResetConfirmView.as_view(
        success_url=reverse_lazy('accounts:login'),
        template_name='accounts/password_reset_confirm.html'
    ), name='password_reset_confirm'),
]
