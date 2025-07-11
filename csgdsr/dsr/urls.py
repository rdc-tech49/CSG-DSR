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

    #admin users
    path('admin_users/', views.admin_users_view, name='admin_users_page'),
    path('admin_users/edit/<int:user_id>/', views.admin_users_view, name='edit_user'),

    # admin strength
    path('admin_officers_strength/', views.admin_officers_strength_view, name='admin_officers_strength_page'),
    path('admin_officers_strength_page/edit/<int:officer_id>/', views.admin_officers_strength_view, name='edit-officer'),

    # admin buildings 
    path('admin_MPS_buildings/', views.admin_MPS_buildings_view, name='admin_MPS_buildings_page'),
    path('admin_MPS_buildings/mps/edit/<int:mps_id>/', views.admin_MPS_buildings_view, name='edit_mps'),
    path('admin_MPS_buildings/checkpost/edit/<int:checkpost_id>/', views.admin_MPS_buildings_view, name='edit_checkpost'),
    path('admin_MPS_buildings/ps/edit/<int:ps_id>/', views.admin_MPS_buildings_view, name='edit_ps'),

    # admin vehicle boat 
    path('admin_vehicle_boat/', views.admin_vehicle_boat_view, name='admin_vehicle_boat_page'),
    path('admin_vehicle_boat/vehicle/edit/<int:vehicle_id>/', views.admin_vehicle_boat_view, name='edit_vehicle'),
    path('admin_vehicle_boat/boat/edit/<int:boat_id>/', views.admin_vehicle_boat_view, name='edit_boat'),



    # admin other agencies 
    path('admin_other_agencies/', views.admin_other_agencies_view, name='admin_other_agencies_page'),
    path('admin_other_agencies/agency/edit/<int:agency_id>/', views.admin_other_agencies_view, name='edit_agency'),


    # admin seizure
    path('admin_seizure_items/', views.admin_seizure_items_view, name='admin_seizure_items_page'),
    path('admin_seizure_items/edit/<int:item_id>/', views.admin_seizure_items_view, name='edit_seizure_item'),

    #admin reports
    path('admin_cases_summary/', views.admin_admin_cases_summary_view, name='admin_cases_summary'),
    path('admin_vvc_beat_proforma_summary/', views.admin_vvc_beat_proforma_summary_view, name='admin_vvc_beat_proforma_summary'),
    path('admin_patrol_check_summary/', views.admin_patrol_check_summary_view, name='admin_patrol_check_summary'),
    path('admin_fishermen_attack_arrest_summary/', views.admin_fishermen_attack_arrest_summary_view, name='admin_fishermen_attack_arrest_summary'),
    path('admin_assets_summary/', views.admin_assets_summary_view, name='admin_assets_summary'),




    # user page
    #dashboard
    path('user-dashboard/', views.user_dashboard_view, name='user_dashboard'),
    #forms main page
    path('forms/', views.forms_view, name='forms_page'),

    #categories forms
    #Officer

    #checkpost
    path('add_checkpost/', views.add_checkpost, name='add_checkpost'),
    #Other_Agencies
    path('other_agencies_form/', views.other_agencies_form_view, name='other_agencies_form'),


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
    #Fishermen Attack Arrest
    path('attack_tnfishermen_form/', views.attack_tnfishermen_form, name='attack_tnfishermen_form'),
    path('arrest_tnfishermen_form/', views.arrest_tnfishermen_form, name='arrest_tnfishermen_form'),
    path('arrest_slfishermen_form/', views.arrest_slfishermen_form, name='arrest_slfishermen_form'),
    #onroad vehicle status
    path('onroad_vehicle_status_form/', views.onroad_vehicle_status_form_view, name='onroad_vehicle_status_form'),
    #onwater vehicle status 
    path('onwater_vehicle_status_form/', views.onwater_vehicle_status_form_view, name='onwater_vehicle_status_form'),
    #VVC meeting
    path('vvc_meeting_form/', views.vvc_meeting_form_view, name='vvc_meeting_form'),
    #Beat Details
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
    path('rescue_seizure_summary/', views.rescue_beach_summary_view, name='rescue_seizure_summary'),
    path('forecast_summary/', views.forecast_summary_view, name='forecast_summary'),
    path('fishermen_attack_arrest_summary/', views.fishermen_attack_arrest_summary, name='fishermen_attack_arrest_summary'),
    path('vehicle_status_summary/', views.vehicle_status_summary_view, name='vehicle_status_summary'),
    path('beat__vvc_summary/', views.beat__vvc_summary_view, name='beat__vvc_summary'),
    path('proforma_summary/', views.proforma_summary_view, name='proforma_summary'),
    path('vehicle_check_patrol_summary/', views.vehicle_check_patrol_summary_view, name='vehicle_check_patrol_summary'),

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
    
    #rescue_summary
    path('rescue_at_beach/ajax-search/rescueb/', views.rescue_at_beach_ajax_search_view, name='rescue_beach_ajax_search'),
    path('rescue_at_beach/export-word/', views.rescue_at_beach_export_word_view, name='rescue_beach_export_word'),
    path('rescue_at_beach/<int:pk>/download/', views.rescue_at_beach_download_view, name='rescue_beach_download'),
    path('rescue_at_beach/<int:pk>/edit/', views.rescue_at_beach_edit_view, name='rescue_beach_edit'),
    path('rescue_at_beach/<int:pk>/delete/', views.rescue_at_beach_delete_view, name='rescue_at_beach_delete'),
    
    #rescue_at_sea_summary
    path('rescue_at_sea/ajax-search/rescue_sea/', views.rescue_at_sea_ajax_search_view, name='rescue_sea_ajax_search'),
    path('rescue_at_sea/export-word/', views.rescue_at_sea_export_word_view, name='rescue_sea_export_word'),
    path('rescue_at_sea/<int:pk>/download/', views.rescue_at_sea_download_view, name='rescue_sea_download'),
    path('rescue_at_sea/<int:pk>/edit/', views.rescue_at_sea_edit_view, name='rescue_sea_edit'),
    path('rescue_at_sea/<int:pk>/delete/', views.rescue_at_sea_delete_view, name='rescue_sea_delete'),

    #seizure_summary
    path('seizure/ajax-search/seizure/', views.seizure_ajax_search_view, name='seizure_ajax_search'),
    path('seizure/export-word/', views.seizure_export_word_view, name='seizure_export_word'),
    path('seizure/<int:pk>/download/', views.seizure_download_view, name='seizure_download'),
    path('seizure/<int:pk>/edit/', views.seizure_edit_view, name='seizure_edit'),
    path('seizure/<int:pk>/delete/', views.seizure_delete_view, name='seizure_delete'),

    #forecast_summary
    path('forecast/ajax-search/forecast/', views.forecast_ajax_search_view, name='forecast_ajax_search'),
    path('forecast/export-word/', views.forecast_export_word_view, name='forecast_export_word'),
    path('forecast/<int:pk>/download/', views.forecast_download_view, name='forecast_download'),
    path('forecast/<int:pk>/edit/', views.forecast_edit_view, name='forecast_edit'),
    path('forecast/<int:pk>/delete/', views.forecast_delete_view, name='forecast_delete'),
    
    #tn_fishermen_attack_summary
    path('tnfishermen_attack/ajax-search/tnfishermen_attack/', views.ajax_search_attack_tnfishermen, name='tnfishermen_attack_ajax_search'),
    path('tnfishermen_attack/export-word/', views.attack_tnfishermen_export_word_view, name='tnfishermen_attack_export_word'),
    path('tnfishermen_attack/<int:pk>/download/', views.attack_tnfishermen_download_view, name='tnfishermen_attack_download'),
    path('tnfishermen_attack/<int:pk>/edit/', views.attack_tnfishermen_edit_view, name='tnfishermen_attack_edit'),
    path('tnfishermen_attack/<int:pk>/delete/', views.delete_attack_tnfishermen, name='tnfishermen_attack_delete'),

    #tn_fishermen_arrest_summary
    path('tnfishermen_arrest/ajax-search/tnfishermen_arrest/', views.ajax_search_arrest_tnfishermen, name='tnfishermen_arrest_ajax_search'),
    path('tnfishermen_arrest/export-word/', views.arrest_tnfishermen_export_word_view, name='tnfishermen_arrest_export_word'),
    path('tnfishermen_arrest/<int:pk>/download/', views.arrest_tnfishermen_download_view, name='tnfishermen_arrest_download'),
    path('tnfishermen_arrest/<int:pk>/edit/', views.arrest_tnfishermen_edit_view, name='tnfishermen_arrest_edit'),
    path('tnfishermen_arrest/<int:pk>/delete/', views.delete_arrest_tnfishermen, name='tnfishermen_arrest_delete'),

    #sl_fishermen_arrest_summary
    path('slfishermen_arrest/ajax-search/slfishermen_arrest/', views.ajax_search_arrest_slfishermen, name='slfishermen_arrest_ajax_search'),
    path('slfishermen_arrest/export-word/', views.arrest_slfishermen_export_word_view, name='slfishermen_arrest_export_word'),
    path('slfishermen_arrest/<int:pk>/download/', views.arrest_slfishermen_download_view, name='slfishermen_arrest_download'),
    path('slfishermen_arrest/<int:pk>/edit/', views.arrest_slfishermen_edit_view, name='slfishermen_arrest_edit'),
    path('slfishermen_arrest/<int:pk>/delete/', views.delete_arrest_slfishermen, name='slfishermen_arrest_delete'),

    #beat_summary
    path('beat/ajax-search/beat/', views.beat_ajax_search_view, name='beat_ajax_search'),
    path('beat/export-word/', views.beat_export_word_view, name='beat_export_word'),
    path('beat/<int:pk>/download/', views.beat_download_view, name='beat_download'),
    path('beat/<int:pk>/edit/', views.beat_edit_view, name='beat_edit'),
    path('beat/<int:pk>/delete/', views.beat_delete_view, name='beat_delete'),  

    #vvc_summary
    path('vvc/ajax-search/vvc/', views.vvc_ajax_search_view, name='vvc_ajax_search'),
    path('vvc/export-word/', views.vvc_export_word_view, name='vvc_export_word'),
    path('vvc/<int:pk>/download/', views.vvc_download_view, name='vvc_download'),
    path('vvc/<int:pk>/edit/', views.vvc_edit_view, name='vvc_edit'),
    path('vvc/<int:pk>/delete/', views.vvc_delete_view, name='vvc_delete'),

    #proforma_summary
    path('proforma/ajax-search/proforma/', views.proforma_ajax_search_view, name='proforma_ajax_search'),
    path('proforma/export-word/', views.proforma_export_word_view, name='proforma_export_word'),
    path('proforma/<int:pk>/download/', views.proforma_download_view, name='proforma_download'),
    path('proforma/<int:pk>/edit/', views.proforma_edit_view, name='proforma_edit'),
    path('proforma/<int:pk>/delete/', views.proforma_delete_view, name='proforma_delete'),

    #onroad_vehicle_status_summary
    path('onroad_vehicle_status/ajax-search/onroad_vehicle_status/', views.onroad_vehicle_status_ajax_search_view, name='onroad_vehicle_status_ajax_search'),
    path('onroad_vehicle_status/export-word/', views.onroad_vehicle_status_export_word_view, name='onroad_vehicle_status_export_word'),
    path('onroad_vehicle_status/<int:pk>/download/', views.onroad_vehicle_status_download_view, name='onroad_vehicle_status_download'),
    path('onroad_vehicle_status/<int:pk>/edit/', views.onroad_vehicle_status_edit_view, name='onroad_vehicle_status_edit'),
    path('onroad_vehicle_status/<int:pk>/delete/', views.onroad_vehicle_status_delete_view, name='onroad_vehicle_status_delete'),

    #onwater_vehicle_status_summary
    path('onwater_vehicle_status/ajax-search/onwater_vehicle_status/', views.onwater_vehicle_status_ajax_search_view, name='onwater_vehicle_status_ajax_search'),
    path('onwater_vehicle_status/export-word/', views.onwater_vehicle_status_export_word_view, name='onwater_vehicle_status_export_word'),
    path('onwater_vehicle_status/<int:pk>/download/', views.onwater_vehicle_status_download_view, name='onwater_vehicle_status_download'),
    path('onwater_vehicle_status/<int:pk>/edit/', views.onwater_vehicle_status_edit_view, name='onwater_vehicle_status_edit'),
    path('onwater_vehicle_status/<int:pk>/delete/', views.onwater_vehicle_status_delete_view, name='onwater_vehicle_status_delete'),


    #boat_patrol_summary
    path('boat_patrol/ajax-search/boat_patrol/', views.boat_patrol_ajax_search, name='boat_patrol_ajax_search'),
    path('boat_patrol/export-word/', views.boat_patrol_export_word_view, name='boat_patrol_export_word'),
    path('boat_patrol/<int:pk>/download/', views.boat_patrol_download_view, name='boat_patrol_download'),
    path('boat_patrol/<int:pk>/edit/', views.boat_patrol_edit_view, name='boat_patrol_edit'),
    path('boat_patrol/<int:pk>/delete/', views.boat_patrol_delete_view, name='boat_patrol_delete'),

    #atv_patrol_summary
    path('atv_patrol/ajax-search/atv_patrol/', views.atv_patrol_ajax_search_view, name='atv_patrol_ajax_search'),
    path('atv_patrol/export-word/', views.atv_patrol_export_word_view, name='atv_patrol_export_word'),
    path('atv_patrol/<int:pk>/download/', views.atv_patrol_download_view, name='atv_patrol_download'),
    path('atv_patrol/<int:pk>/edit/', views.atv_patrol_edit_view, name='atv_patrol_edit'),
    path('atv_patrol/<int:pk>/delete/', views.atv_patrol_delete_view, name='atv_patrol_delete'),

    #vehicle_checkpost_summary
    path('vehicle_checkpost/ajax-search/vehicle_checkpost/', views.vehicle_checkpost_ajax_search_view, name='vehicle_checkpost_ajax_search'),
    path('vehicle_checkpost/export-word/', views.vehicle_checkpost_export_word_view, name='vehicle_checkpost_export_word'),
    path('vehicle_checkpost/<int:pk>/download/', views.vehicle_checkpost_download_view, name='vehicle_checkpost_download'),
    path('vehicle_checkpost/<int:pk>/edit/', views.vehicle_checkpost_edit_view, name='vehicle_checkpost_edit'),
    path('vehicle_checkpost/<int:pk>/delete/', views.vehicle_checkpost_delete_view, name='vehicle_checkpost_delete'),

    #vehicle_check_others_summary
    path('vehicle_check_others/ajax-search/vehicle_check_others/', views.vehicle_check_others_ajax_search_view, name='vehicle_check_others_ajax_search'),
    path('vehicle_check_others/export-word/', views.vehicle_check_others_export_word_view, name='vehicle_check_others_export_word'),
    path('vehicle_check_others/<int:pk>/download/', views.vehicle_check_others_download_view, name='vehicle_check_others_download'),
    path('vehicle_check_others/<int:pk>/edit/', views.vehicle_check_others_edit_view, name='vehicle_check_others_edit'),
    path('vehicle_check_others/<int:pk>/delete/', views.vehicle_check_others_delete_view, name='vehicle_check_others_delete'),
    













]
