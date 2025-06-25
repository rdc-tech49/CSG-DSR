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
    
    #admin page
    #dashboard
    path('admin-dashboard/', views.admin_dashboard_view, name='admin_dashboard'),
    path('admin_users/', views.admin_users_view, name='admin_users_page'),

    # admin strength
    path('admin_officers_strength/', views.admin_officers_strength_view, name='admin_officers_strength_page'),
    path('admin_officers_strength_page/edit/<int:officer_id>/', views.admin_officers_strength_view, name='edit-officer'),

    # admin buildings 
    path('admin_MPS_buildings/', views.admin_MPS_buildings_view, name='admin_MPS_buildings_page'),
    path('admin_MPS_buildings/mps/edit/<int:mps_id>/', views.admin_MPS_buildings_view, name='edit_mps'),
    path('admin_MPS_buildings/checkpost/edit/<int:checkpost_id>/', views.admin_MPS_buildings_view, name='edit_checkpost'),

    # admin other agencies 
    path('admin_other_agencies/', views.admin_other_agencies_view, name='admin_other_agencies_page'),
    path('admin_other_agencies/agency/edit/<int:agency_id>/', views.admin_other_agencies_view, name='edit_agency'),
    path('admin_other_agencies/attacker/edit/<int:attacker_id>/', views.admin_other_agencies_view, name='edit_attacker'),
    path('admin_other_agencies/arrest_tn/edit/<int:arrest_tn_id>/', views.admin_other_agencies_view, name='edit_arrest_tn'),
    path('admin_other_agencies/arrest_sl/edit/<int:arrest_sl_id>/', views.admin_other_agencies_view, name='edit_arrest_sl'),

    # admin seizure
    path('admin_seizure_items/', views.admin_seizure_items_view, name='admin_seizure_items_page'),
    path('admin_seizure_items/edit/<int:item_id>/', views.admin_seizure_items_view, name='edit_seizure_item'),

    # user page
    #dashboard
    path('user-dashboard/', views.user_dashboard_view, name='user_dashboard'),
    #forms main page
    path('forms/', views.forms_view, name='forms_page'),

    #categories forms
    #Officer
    path('officer_form/', views.officer_form_view, name='officer_form'),
    #Seized Item Category
    path('seized_item_category_form/', views.seized_item_category_form_view, name='seized_item_category_form'),
    #checkpost
    path('add_checkpost/', views.add_checkpost, name='add_checkpost'),
    #Other_Agencies
    path('other_agencies_form/', views.other_agencies_form_view, name='other_agencies_form'),
    #AttackOnTNFishermen_ChoicesForm
    path('attack_on_tnfishermen_choices_form/', views.attack_on_tnfishermen_choices_form_view, name='attack_on_tnfishermen_choices_form'),
    #TNFishermenArrest_ChoicesForm
    path('tnfishermen_arrest_choices_form/', views.tnfishermen_arrest_choices_form_view, name='tnfishermen_arrest_choices_form'),
    #ArrestOfSLFishermen_ChoicesForm
    path('arrest_of_sl_fishermen_choices_form/', views.arrest_of_sl_fishermen_choices_form_view, name='arrest_of_sl_fishermen_choices_form'),

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
    #Rescue at beach
    path('rescue_at_beach_form/', views.rescue_at_beach_form_view, name='rescue_at_beach_form'),
    #Rescue at sea
    path('rescue_at_sea_form/', views.rescue_at_sea_form_view, name='rescue_at_sea_form'),
    #Seizure
    path('seizure_form/', views.seizure_form_view, name='seizure_form'),
    #forecast 
    path('forecast_form/', views.forecast_form_view, name='forecast_form'),
    #attack on TN fishermen 
    path('attack_on_tnfishermen/', views.attack_on_tnfishermen_view, name='attack_on_tnfishermen_form'),
    #TN fishermen_arrest
    path('tnfishermen_arrest_form/', views.tnfishermen_arrest_form_view, name='tnfishermen_arrest_form'),
    #Arrest Of SL Fishermen
    path('arrest_of_sl_fishermen_form/', views.arrest_of_sl_fishermen_form_view, name='arrest_of_sl_fishermen_form'),
    #On Road Vehicle Status
    path('onroad_vehicle_status_form/', views.onroad_vehicle_status_form_view, name='onroad_vehicle_status_form'),
    #On Water Vehicle  Status
    path('onwater_vehicle_status_form/', views.onwater_vehicle_status_form_view, name='onwater_vehicle_status_form'),
    #VVC meeting
    path('vvc_meeting_form/', views.vvc_meeting_form_view, name='vvc_meeting_form'),
    #Beat   Details
    path('beat_details_form/', views.beat_details_form_view, name='beat_details_form'),
    #Proforma
    path('proforma_form/', views.proforma_form_view, name='proforma_form'),
    #Boat Patrol
    path('boat_patrol_form/', views.boat_patrol_form_view, name='boat_patrol_form'),
    #Atv patrol
    path('atv_patrol_form/', views.atv_patrol_form_view, name='atv_patrol_form'),
    #Vehicle CheckPost
    path('vehicle_checkpost_form/', views.vehicle_checkpost_form_view, name='vehicle_checkpost_form'),
    #Vehicle Check others
    path('vehicle_check_others_form/', views.vehicle_check_others_form_view, name='vehicle_check_others_form'),

    

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

    #maritimeact_summary
    path('maritimeact/ajax-search/maritimeact/', views.maritimeact_ajax_search_view, name='maritimeact_ajax_search'),
    path('maritimeact/export-word/', views.maritimeact_export_word_view, name='maritimeact_export_word'),
    path('maritimeact/<int:pk>/download/', views.maritimeact_download_view, name='maritimeact_download'),
    path('maritimeact/<int:pk>/edit/', views.maritimeact_edit_view, name='maritimeact_edit'),
    path('maritimeact/<int:pk>/delete/', views.maritimeact_delete_view, name='maritimeact_delete'),
    
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
