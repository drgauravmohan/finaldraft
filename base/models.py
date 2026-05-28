from django.db import models
from django.utils.text import slugify

class Service(models.Model):
    """Main service/speciality model"""
    name = models.CharField(max_length=200, help_text="Service name (e.g., Neurosciences, Cardiology)")
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    icon = models.ImageField(upload_to='services/icons/', blank=True, null=True, help_text="Icon for navigation menu (26x26px recommended)")

    # Banner section
    banner_image_desktop = models.ImageField(upload_to='services/banners/', blank=True, null=True, help_text="Desktop banner image (optional)")
    banner_image_mobile = models.ImageField(upload_to='services/banners/', blank=True, null=True, help_text="Mobile banner image (optional)")

    # Meta information
    meta_title = models.CharField(max_length=200, blank=True)
    meta_description = models.TextField(blank=True)
    meta_keywords = models.CharField(max_length=500, blank=True)

    # Overview section
    overview_title = models.CharField(max_length=200, default="Overview")

    # Homepage display settings
    show_in_specialities = models.BooleanField(default=False, help_text="Show in Specialities section on homepage")
    specialities_order = models.PositiveIntegerField(default=0, help_text="Display order in Specialities section")

    show_in_model_of_care = models.BooleanField(default=False, help_text="Show in Model of Care section on homepage")
    model_of_care_order = models.PositiveIntegerField(default=0, help_text="Display order in Model of Care section")
    model_of_care_image = models.ImageField(upload_to='services/model_of_care/', blank=True, null=True, help_text="Image for Model of Care section")

    show_in_services = models.BooleanField(default=False, help_text="Show in Services section on homepage")
    services_order = models.PositiveIntegerField(default=0, help_text="Display order in Services section")
    card_image = models.ImageField(upload_to='services/cards/', blank=True, null=True, help_text="Image for service cards")
    short_description = models.TextField(blank=True, help_text="Short description for homepage cards")
    logo_image = models.ImageField(upload_to='services/logos/', blank=True, null=True, help_text="Logo image for service cards")

    # Status
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'Service'
        verbose_name_plural = 'Services'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class ServiceFeature(models.Model):
    """Features/highlights for a service"""
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='features')
    title = models.CharField(max_length=300)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']
        verbose_name = 'Service Feature'
        verbose_name_plural = 'Service Features'

    def __str__(self):
        return f"{self.service.name} - {self.title[:50]}"


class ServiceDoctor(models.Model):
    """Doctor/Chairman message section"""
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='doctors')
    name = models.CharField(max_length=200, help_text="Doctor's full name")
    title = models.CharField(max_length=300, help_text="e.g., Chairman, Institute Of Neurosciences")
    image = models.ImageField(upload_to='services/doctors/', blank=True, null=True, help_text="Doctor's photo (optional)")
    message = models.TextField(help_text="Message/description from the doctor")
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']
        verbose_name = 'Service Doctor'
        verbose_name_plural = 'Service Doctors'

    def __str__(self):
        return f"{self.name} - {self.service.name}"


class ServiceTeam(models.Model):
    """Team sections with images and descriptions"""
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='teams')
    title = models.CharField(max_length=300, help_text="Team section title")
    subtitle = models.CharField(max_length=500, blank=True, help_text="Optional subtitle")
    image = models.ImageField(upload_to='services/teams/', blank=True, null=True, help_text="Team image (optional)")
    description = models.TextField()
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']
        verbose_name = 'Service Team'
        verbose_name_plural = 'Service Teams'

    def __str__(self):
        return f"{self.service.name} - {self.title[:50]}"


class Treatment(models.Model):
    """Treatments offered under a service"""
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='treatments')
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, blank=True)
    image = models.ImageField(upload_to='services/treatments/', blank=True, null=True, help_text="Treatment image (optional)")
    description = models.TextField()
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']
        verbose_name = 'Treatment'
        verbose_name_plural = 'Treatments'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.service.name} - {self.name}"


class Ailment(models.Model):
    """Ailments/conditions treated under a service"""
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='ailments')
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, blank=True)
    image = models.ImageField(upload_to='services/ailments/', blank=True, null=True, help_text="Ailment image (optional)")
    description = models.TextField()
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']
        verbose_name = 'Ailment'
        verbose_name_plural = 'Ailments'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.service.name} - {self.name}"


class Technology(models.Model):
    """Latest technology used in the service"""
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='technologies')
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='services/technologies/', blank=True, null=True, help_text="Technology image (optional)")
    short_description = models.TextField(help_text="Brief description (shown in card)")
    full_description = models.TextField(blank=True, help_text="Full description (optional)")
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']
        verbose_name = 'Technology'
        verbose_name_plural = 'Technologies'

    def __str__(self):
        return f"{self.service.name} - {self.name}"


class ServiceAccordion(models.Model):
    """Generic accordion items for services (can be used for sub-specializations, FAQs, etc.)"""
    SECTION_CHOICES = [
        ('subspecialization', 'Sub-Specialization'),
        ('faq', 'FAQ'),
        ('other', 'Other'),
    ]

    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='accordions')
    section_type = models.CharField(max_length=50, choices=SECTION_CHOICES, default='other')
    title = models.CharField(max_length=300)
    description = models.TextField()
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['section_type', 'order']
        verbose_name = 'Service Accordion'
        verbose_name_plural = 'Service Accordions'

    def __str__(self):
        return f"{self.service.name} - {self.section_type} - {self.title[:50]}"


class SuccessStory(models.Model):
    """Patient success stories"""
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='success_stories')
    patient_name = models.CharField(max_length=200, blank=True, help_text="Optional - can be anonymous")
    title = models.CharField(max_length=300)
    story = models.TextField()
    image = models.ImageField(upload_to='services/success_stories/', blank=True, null=True)
    video_url = models.URLField(blank=True, help_text="Optional YouTube/Vimeo URL")
    order = models.PositiveIntegerField(default=0)
    is_featured = models.BooleanField(default=False)

    class Meta:
        ordering = ['order']
        verbose_name = 'Success Story'
        verbose_name_plural = 'Success Stories'

    def __str__(self):
        return f"{self.service.name} - {self.title[:50]}"
