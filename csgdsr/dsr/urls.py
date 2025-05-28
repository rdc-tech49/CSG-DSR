from django.urls import path
from .views import signup_view
from . import views
from django.contrib.auth import views as auth_views
from .views import CustomPasswordChangeView, update_user_view


urlpatterns = [
    
    path('', views.home_view, name='home'),
    
    # Password reset
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='dsr/registration/password_reset.html'), name='password_reset'),
    path('password-reset_done/', auth_views.PasswordResetDoneView.as_view(template_name='dsr/registration/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='dsr/registration/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='dsr/registration/password_reset_complete.html'), name='password_reset_complete'),
    path('change-password/', CustomPasswordChangeView.as_view(), name='password_change'),

    # Update user information
    path('update-user/', update_user_view, name='update_user'),
    #Signup
    path('signup/', signup_view, name='signup'),
    #logout
    path('logout/', views.logout_view, name='logout'),
    
    # user page
    path('user-dashboard/', views.user_dashboard_view, name='user_dashboard'),
    path('forms/', views.forms_view, name='forms_page'),
    path('register_case_form/', views.register_case_form_view, name='register_case_form'),
    path('rescue-seizure_form/', views.rescue_seizure_form_view, name='rescue_seizure_form'),
    path('forecast_form/', views.forecast_form_view, name='forecast_form'),
    path('fishermen_attack_arrest_form/', views.fishermen_attack_arrest_form_view, name='fishermen_attack_arrest_form'),
    path('vehicle-status_form/', views.vehicle_status_form_view, name='vehicle_status_form'),
    path('vvc-beat-proforma_form/', views.vvc_beat_proforma_form_view, name='vvc_beat_proforma_form'),
    path('patrol-vehicle-check_form/', views.patrol_vehicle_check_form_view, name='patrol_vehicle_check_form'),
    path('beat_proforma/', views.beat_proforma_view, name='beat_proforma'),
    path('vvc/', views.vvc_view, name='vvc')

]
