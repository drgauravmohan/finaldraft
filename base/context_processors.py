"""
Context processors for the base app.
These functions make variables available to all templates.
"""
from .models import Service


def services_processor(request):
    """
    Makes all active services available to all templates.
    Also provides filtered services for homepage sections.
    Usage in templates:
    - {% for service in all_services %}
    - {% for service in specialities_services %}
    - {% for service in model_of_care_services %}
    - {% for service in services_section_services %}
    """
    return {
        'all_services': Service.objects.filter(is_active=True).order_by('name'),
        'specialities_services': Service.objects.filter(
            is_active=True,
            show_in_specialities=True
        ).order_by('specialities_order')[:6],
        'model_of_care_services': Service.objects.filter(
            is_active=True,
            show_in_model_of_care=True
        ).order_by('model_of_care_order')[:5],
        'services_section_services': Service.objects.filter(
            is_active=True,
            show_in_services=True
        ).order_by('services_order')[:4],
    }
