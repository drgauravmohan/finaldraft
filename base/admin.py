from django.contrib import admin
from .models import (
    Service, ServiceFeature, ServiceDoctor, ServiceTeam,
    Treatment, Ailment, Technology, ServiceAccordion, SuccessStory
)


class ServiceFeatureInline(admin.TabularInline):
    model = ServiceFeature
    extra = 1
    fields = ('title', 'order')


class ServiceDoctorInline(admin.StackedInline):
    model = ServiceDoctor
    extra = 0
    fields = ('name', 'title', 'message', 'image', 'order')


class ServiceTeamInline(admin.StackedInline):
    model = ServiceTeam
    extra = 0
    fields = ('title', 'subtitle', 'image', 'description', 'order')


class TreatmentInline(admin.TabularInline):
    model = Treatment
    extra = 0
    fields = ('name', 'image', 'order')
    show_change_link = True


class AilmentInline(admin.TabularInline):
    model = Ailment
    extra = 0
    fields = ('name', 'image', 'order')
    show_change_link = True


class TechnologyInline(admin.TabularInline):
    model = Technology
    extra = 0
    fields = ('name', 'image', 'order')
    show_change_link = True


class ServiceAccordionInline(admin.TabularInline):
    model = ServiceAccordion
    extra = 0
    fields = ('section_type', 'title', 'order')
    show_change_link = True


class SuccessStoryInline(admin.TabularInline):
    model = SuccessStory
    extra = 0
    fields = ('title', 'patient_name', 'is_featured', 'order')
    show_change_link = True


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'is_active', 'created_at', 'updated_at')
    list_filter = ('is_active', 'created_at')
    search_fields = ('name', 'meta_title', 'meta_description')
    prepopulated_fields = {'slug': ('name',)}

    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'slug', 'icon', 'is_active')
        }),
        ('Banner Images', {
            'fields': ('banner_image_desktop', 'banner_image_mobile')
        }),
        ('Overview', {
            'fields': ('overview_title',)
        }),
        ('Homepage Display - Specialities Section', {
            'fields': ('show_in_specialities', 'specialities_order'),
            'classes': ('collapse',)
        }),
        ('Homepage Display - Model of Care Section', {
            'fields': ('show_in_model_of_care', 'model_of_care_order', 'model_of_care_image'),
            'classes': ('collapse',)
        }),
        ('Homepage Display - Services Section', {
            'fields': ('show_in_services', 'services_order', 'card_image', 'short_description', 'logo_image'),
            'classes': ('collapse',)
        }),
        ('SEO Meta Information', {
            'fields': ('meta_title', 'meta_description', 'meta_keywords'),
            'classes': ('collapse',)
        }),
    )

    inlines = [
        ServiceFeatureInline,
        ServiceDoctorInline,
        ServiceTeamInline,
        TreatmentInline,
        AilmentInline,
        TechnologyInline,
        ServiceAccordionInline,
        SuccessStoryInline,
    ]


@admin.register(Treatment)
class TreatmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'service', 'order')
    list_filter = ('service',)
    search_fields = ('name', 'description')
    prepopulated_fields = {'slug': ('name',)}
    fields = ('service', 'name', 'slug', 'image', 'description', 'order')


@admin.register(Ailment)
class AilmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'service', 'order')
    list_filter = ('service',)
    search_fields = ('name', 'description')
    prepopulated_fields = {'slug': ('name',)}
    fields = ('service', 'name', 'slug', 'image', 'description', 'order')


@admin.register(Technology)
class TechnologyAdmin(admin.ModelAdmin):
    list_display = ('name', 'service', 'order')
    list_filter = ('service',)
    search_fields = ('name', 'short_description')
    fields = ('service', 'name', 'image', 'short_description', 'full_description', 'order')


@admin.register(ServiceAccordion)
class ServiceAccordionAdmin(admin.ModelAdmin):
    list_display = ('title', 'service', 'section_type', 'order')
    list_filter = ('service', 'section_type')
    search_fields = ('title', 'description')
    fields = ('service', 'section_type', 'title', 'description', 'order')


@admin.register(SuccessStory)
class SuccessStoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'service', 'patient_name', 'is_featured', 'order')
    list_filter = ('service', 'is_featured')
    search_fields = ('title', 'story', 'patient_name')
    fields = ('service', 'title', 'patient_name', 'story', 'image', 'video_url', 'is_featured', 'order')
