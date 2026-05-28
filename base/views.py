from django.shortcuts import render

# Create your views here.

def home(request):
    """
    Main homepage view
    """
    from .models import Service
    
    # Fetch services that should be displayed in the specialities section
    services = Service.objects.filter(
        is_active=True,
        show_in_specialities=True
    ).order_by('specialities_order')
    
    # Fetch services for Model of Care section
    model_of_care_services = Service.objects.filter(
        is_active=True,
        show_in_model_of_care=True
    ).order_by('model_of_care_order')
    
    context = {
        'services': services,
        'model_of_care_services': model_of_care_services,
    }
    
    return render(request, 'base/index.html', context)

# Add more views here as needed
def about(request):
    return render(request, 'base/about.html')

def blog(request):
    return render(request, 'base/blog.html')


def blogdtl(request):
    return render(request, 'base/blog-detail.html')

def blogdtl_backup(request):
    return render(request, 'base/blog-detail-backup.html')

def careers(request):
    return render(request, 'base/careers.html')

def contact(request):
    return render(request, 'base/contact.html')

def health_library(request):
    return render(request, 'base/health-library.html')

def home_care(request):
    return render(request, 'base/home-care.html')

def international_patient(request):
    return render(request, 'base/international-patient.html')

def sudharshan heart clinic_labs(request):
    return render(request, 'base/sudharshan heart clinic-labs.html')

def our_pharmacy(request):
    return render(request, 'base/our-pharmacy.html')


def service_detail(request, slug):
    from django.shortcuts import get_object_or_404
    from .models import Service

    service = get_object_or_404(Service, slug=slug, is_active=True)

    context = {
        'service': service,
        'features': service.features.all(),
        'doctors': service.doctors.all(),
        'teams': service.teams.all(),
        'treatments': service.treatments.all(),
        'ailments': service.ailments.all(),
        'technologies': service.technologies.all(),
        'accordions': service.accordions.all(),
        'success_stories': service.success_stories.all(),
        'subspecializations': service.accordions.filter(section_type='subspecialization'),
    }

    return render(request, 'base/service-detail.html', context)

def services(request):
    return render(request, 'base/services.html')

def why_us(request):
    return render(request, 'base/why-us.html')

def hopitals_near_me(request):
    return render(request, 'base/gurugramhospital.html')

def cardiology(request):
    return render(request, 'base/cardiology.html')

def health_checkup(request):
    return render(request, 'base/health-checkup.html')


def second_option(request):
    return render(request, 'base/second-option.html')

def Find_doctor(request):
    return render(request, 'base/Find-a-doctor.html')

def treatments(request):
    return render(request, 'base/treatments.html')

def terms_conditions(request):
    return render(request, 'base/terms-conditions.html')

def help_desk(request):
    return render(request, 'base/help-desk.html')

def oncology(request):
    return render(request, 'base/oncology.html')

def neurology(request):
    return render(request, 'base/neurology.html')

def gastroenterology(request):
    return render(request, 'base/gastroenterology.html')

def orthopaedics(request):
    return render(request, 'base/orthopaedics.html')

def urology_nephrology(request):
    return render(request, 'base/urology_nephrology.html')

def angioplasty(request):
    return render(request, 'base/angioplasty.html')

def lucknow_hospital(request):
    return render(request, 'base/lucknow-hospital.html')

def patna_hospital(request):
    return render(request, 'base/patna-hospital.html')

def indore_hospital(request):
    return render(request, 'base/indore_hospital.html')

def noida_hospital(request):
    return render(request, 'base/noida-hospital.html')

def ranchi_hospitals(request):
    return render(request, 'base/ranchi-hospitals.html')

def mediclinics(request):
    return render(request, 'base/mediclinics.html')

def speciality(request):
    return render(request, 'base/speciality.html')

def technology(request):
    return render(request, 'base/technology.html')

def ailments(request):
    return render(request, 'base/ailments.html')

# def contact(request):
#     return render(request, 'base/contact.html')
