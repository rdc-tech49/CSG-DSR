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
    #dashboard
    path('user-dashboard/', views.user_dashboard_view, name='user_dashboard'),
    #forms main page
    path('forms/', views.forms_view, name='forms_page'),

    #individual forms
    #cases registered forms
    #csr
    path('csr_form/', views.csr_form_view, name='csr_form'),
    #194bnss_missing
    path('bnss-missing-form/', views.bnss_missing_form_view, name='bnss_missing_form'),
    #Other cases
    path('othercases_form/', views.othercases_form, name='othercases_form'),

    #Maritime act
    path('maritimeact_form/', views.maritimeact_form_view, name='maritimeact_form'),
    #Rescue
    path('rescue_form/', views.rescue_form_view, name='rescue_form'),
    #Seizure
    path('seizure_form/', views.seizure_form_view, name='seizure_form'),
    #forecast 
    path('forecast_form/', views.forecast_form_view, name='forecast_form'),
    #fishermen_attack
    path('fishermen_attack_form/', views.fishermen_attack_form_view, name='fishermen_attack_form'),
    #fishermen_arrest
    path('fishermen_arrest_form/', views.fishermen_arrest_form_view, name='fishermen_arrest_form'),
    #boat_vehicle_status
    path('boat_vehicle_status_form/', views.boat_vehicle_status_form_view, name='boat_vehicle_status_form'),
    #vvc
    path('vvc_form/', views.vvc_form_view, name='vvc_form'),
    #beat
    path('beat_form/', views.beat_form_view, name='beat_form'),
    #proforma
    path('proforma_form/', views.proforma_form_view, name='proforma_form'),
    #boat_patrol
    path('boat_patrol_form/', views.boat_patrol_form_view, name='boat_patrol_form'),
    #vehicle_check
    path('vehicle_check_form/', views.vehicle_check_form_view, name='vehicle_check_form'),


    #submitted forms summary
    #cases_registered_summary
    path('cases-summary/', views.cases_registered_summary_view, name='cases_summary'),

    #csr_summary
    path('csr/<int:pk>/download/', views.csr_download_view, name='csr_download'),
    path('csr/<int:pk>/edit/', views.csr_edit_view, name='csr_edit'),
    path('csr/<int:pk>/delete/', views.csr_delete_view, name='csr_delete'),
    path('ajax/csr-search/', views.csr_ajax_search_view, name='csr_ajax_search'),
    path('csr/export-word/', views.csr_export_word_view, name='csr_export_word'),

    #194bnss_summary
    path('bnss-194/ajax-search/194bnss/', views.bnss194_cases_ajax_search_view, name='bnss194_cases_ajax_search'),
    path('bnss-194/export-word/', views.bnss_194_export_word_view, name='bnss_194_export_word'),
    
    path('bns194/<int:pk>/download/', views.bnss194_download_view, name='bnss194_download'),
    path('bnss-missing/<int:pk>/edit/', views.bnss_missing_edit_view, name='bnss_missing_edit'),
    path('bnss-missing/<int:pk>/delete/', views.bnss_missing_delete_view, name='bnss_missing_delete'),
    
    #missing_summary
    path('missing/ajax-search/missing/', views.missing_ajax_search_view, name='missing_cases_ajax_search'),
    path('missing/export-word/', views.missing_export_word_view, name='missing_export_word'),

    #othercases_summary
    path('othercases/ajax-search/othercases/', views.othercases_ajax_search_view, name='othercases_ajax_search'),
    path('othercases/export-word/', views.othercases_export_word_view, name='othercases_export_word'),
    path('othercases/<int:pk>/download/', views.othercases_download_view, name='othercases_download'),
    path('othercases/<int:pk>/edit/', views.othercases_edit_view, name='othercases_edit'),
    path('othercases/<int:pk>/delete/', views.othercases_delete_view, name='othercases_delete'),

    
    #rescue_seizure_summary
    path('rescue_seizure_summary/', views.rescue_seizure_summary_view, name='rescue_seizure_summary'),
    #forecast_summary
    path('forecast_summary/', views.forecast_summary_view, name='forecast_summary'),
    #fishermen_attack_arrest_summary
    path('fishermen_attack_arrest_summary/', views.fishermen_attack_arrest_summary_view, name='fishermen_attack_arrest_summary'),
    #vehicle_status_summary
    path('vehicle_status_summary/', views.vehicle_status_summary_view, name='vehicle_status_summary'),
    #vvc_beat_proforma_summary
    path('vvc_beat_proforma_summary/', views.vvc_beat_proforma_summary_view, name='vvc_beat_proforma_summary'),
    #patrol_vehicle_check_summary
    path('patrol_vehicle_check_summary/', views.patrol_vehicle_check_summary_view, name='patrol_vehicle_check_summary'),











]
