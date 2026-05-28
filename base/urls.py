from django.urls import path
from . import views

app_name = 'base'

urlpatterns = [
    path('', views.home, name='home'),

    path('about/', views.about, name='about'),

    path('blog/', views.blog, name='blog'),

    path('blog-detail/', views.blogdtl, name='blog-detail'),

    path('blog-detail-backup/', views.blogdtl_backup, name='blog-detail-backup'),

    path('careers/', views.careers, name='careers'),

    path('contact-us/', views.contact, name='contact-us'),

    path('health-library/', views.health_library, name='health-library'),

    path('home-care/', views.home_care, name='home-care'),

    path('international-patient/', views.international_patient, name='international-patient'),

    path('sudharshan heart clinic-labs/', views.sudharshan heart clinic_labs, name='sudharshan heart clinic-labs'),

    path('our-pharmacy/', views.our_pharmacy, name='our-pharmacy'),

    path('service/<slug:slug>/', views.service_detail, name='service-detail'),

    path('services/', views.services, name='services'),

    path('why-us/', views.why_us, name='why-us'),



    path('healthcheckup/gurugram-hospital',views.health_checkup,name='health-checkup'),

    path('second-opinion/',views.second_option,name='second-option'),

    path('doctor-listing/',views.Find_doctor,name='Find-a-doctor'),

    path('treatments/',views.treatments,name='treatments'),

    path('patient/terms-conditions/',views.terms_conditions,name='terms-conditions'),

    path('help-desk/',views.help_desk,name='help-desk'),

    path('technology/',views.technology,name='technology'),

    path('ailments/',views.ailments,name='ailments'),




# speciality routes 

    path('hospitals-near-me/gurugram-hospital/speciality/cardiology',views.cardiology,name='cardiology'),

    path('hospitals-near-me/gurugram-hospital/speciality/oncology/',views.oncology,name='oncology'),

    path('hospitals-near-me/gurugram-hospital/speciality/neurology/',views.neurology,name='neurology'),

    path('hospitals-near-me/gurugram-hospital/speciality/gastroenterology/',views.gastroenterology,name='gastroenterology'),

    path('hospitals-near-me/gurugram-hospital/speciality/orthopaedics/',views.orthopaedics,name='orthopaedics'),

    path('hospitals-near-me/gurugram-hospital/speciality/urology-nephrology/',views.urology_nephrology,name='urology-nephrology'),

    path('hospitals-near-me/gurugram-hospital/speciality/angioplasty/',views.angioplasty,name='angioplasty'),

    path('hospitals-near-me/gurugram-hospital/speciality',views.speciality,name='speciality'),


    path('mediclinics/',views.mediclinics,name='mediclinics'),





# hospitals 

    path('hospitals-near-me/gurugram-hospital/',views.hopitals_near_me,name='hospitals-near-me'),

    path('hospitals-near-me/lucknow-hospital/',views.lucknow_hospital,name='lucknow-hospital'),

    path('hospitals-near-me/patna-hospital/',views.patna_hospital,name='patna-hospital'),

    path('hospitals-near-me/indore-hospital/',views.indore_hospital,name='indore-hospital'),

    path('hospitals-near-me/noida-hospital/',views.noida_hospital,name='noida-hospital'),

    path('hospitals-near-me/ranchi-hospitals/',views.ranchi_hospitals,name='ranchi-hospitals'),


    









    # Add more URL patterns here as needed
    # path('about/', views.about, name='about'),
    # path('contact/', views.contact, name='contact'),
]
