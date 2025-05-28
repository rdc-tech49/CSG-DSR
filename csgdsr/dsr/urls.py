from django.urls import path
from .views import signup_view
from . import views
from django.contrib.auth import views as auth_views
from .views import CustomPasswordChangeView, update_user_view


urlpatterns = [
    path('signup/', signup_view, name='signup'),
    path('', views.home_view, name='home'),
    path('user-dashboard/', views.user_dashboard_view, name='user_dashboard'),
    # Password reset
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='dsr/registration/password_reset.html'), name='password_reset'),
    path('password-reset_done/', auth_views.PasswordResetDoneView.as_view(template_name='dsr/registration/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='dsr/registration/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='dsr/registration/password_reset_complete.html'), name='password_reset_complete'),
    
    path('change-password/', CustomPasswordChangeView.as_view(), name='password_change'),
    path('update-user/', update_user_view, name='update_user'),

    path('logout/', views.logout_view, name='logout'),
    
    

]
