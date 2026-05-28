# Service Detail Template Update Guide

This guide shows you how to replace static content in `service-detail.html` with dynamic data from the database.

## Available Context Variables

The view passes these variables to the template:
- `service` - Main service object
- `features` - Service features/highlights
- `doctors` - Doctor/chairman messages
- `teams` - Team sections
- `treatments` - All treatments
- `ailments` - All ailments
- `technologies` - All technologies
- `accordions` - All accordion items
- `subspecializations` - Filtered accordions for sub-specializations
- `success_stories` - Patient success stories

## Key Replacements

### 1. Service Name
```django
{# Replace static text with: #}
<h1 class="heading medantaxlheading mb-10">{{ service.name }}</h1>
```

### 2. Banner Images
```django
{# Desktop banner #}
<img src="{{ service.banner_image_desktop.url }}" alt="{{ service.name }}">

{# Mobile banner (if exists) #}
{% if service.banner_image_mobile %}
<img src="{{ service.banner_image_mobile.url }}" alt="{{ service.name }}">
{% endif %}
```

### 3. Meta Tags (in <head> section)
```django
<title>{{ service.meta_title|default:service.name }} | Medanta</title>
<meta name="description" content="{{ service.meta_description }}">
<meta name="keywords" content="{{ service.meta_keywords }}">
```

### 4. Service Features (those bullet points)
```django
<div class="institute-features">
    {% for feature in features %}
    <div class="feature-block">
        <div class="medantaxxsheading font700 clr-dark">{{ feature.title }}</div>
    </div>
    {% endfor %}
</div>
```

### 5. Doctor/Chairman Section
```django
{% for doctor in doctors %}
<div class="col-wrap dflex flexwrap centered-items wow fadeInUp">
    <div class="col col3">
        <div class="chairman-message">
            <div class="para-wrap">
                <p>{{ doctor.message }}</p>
            </div>
        </div>
    </div>
    <div class="col col3">
        <div class="chairman-image text-center">
            <img src="{{ doctor.image.url }}" alt="{{ doctor.name }}" width="544" height="715">
        </div>
    </div>
    <div class="col col3">
        <div class="chairman-info">
            <div class="heading-lg clr-dark mb-10 font700">{{ doctor.name }}</div>
            <div class="medantaxsheading clr-primary font700 mb-20">{{ doctor.title }}</div>
        </div>
    </div>
</div>
{% endfor %}
```

### 6. Team Sections
```django
<div id="heart-slider" class="space-row slick-arrow-style-1 slider-tb-shadow eqslides-height">
    {% for team in teams %}
    <div class="slide-item">
        <div class="post-card eqheight">
            <div class="thumb thumb-ratio thumb-ratio1">
                <img src="{{ team.image.url }}" alt="{{ team.title }}" width="514" height="400">
            </div>
            <div class="card-desk">
                <div class="para-wrap">
                    <p class="m-0">{{ team.description }}</p>
                </div>
            </div>
        </div>
    </div>
    {% endfor %}
</div>
```

### 7. Treatments Section
```django
<section class="py-50 treatment-section content-section" id="treatment-section">
    <div class="container">
        <div class="heading mb-10 clr-dark text-center">Our Treatments</div>
        <div class="tabbed-set">
            {% for treatment in treatments %}
            <input type="radio" name="treatment-tabs" id="treatment-tab-{{ forloop.counter }}" {% if forloop.first %}checked{% endif %}>
            <label for="treatment-tab-{{ forloop.counter }}">{{ treatment.name }}</label>
            {% endfor %}

            {% for treatment in treatments %}
            <div class="content treatment-content">
                <div class="col-wrap dflex flexwrap centered-items">
                    <div class="col col4">
                        <img src="{{ treatment.image.url }}" alt="{{ treatment.name }}" width="340" height="340">
                    </div>
                    <div class="col col8">
                        <div class="para-wrap">
                            {{ treatment.description|safe }}
                        </div>
                    </div>
                </div>
            </div>
            {% endfor %}
        </div>
    </div>
</section>
```

### 8. Ailments Section
```django
<section class="py-50 treatment-section content-section" id="ailment-section">
    <div class="container">
        <div class="heading mb-10 clr-dark text-center">Ailments</div>
        <div class="tabbed-set">
            {% for ailment in ailments %}
            <input type="radio" name="ailment-tabs" id="ailment-tab-{{ forloop.counter }}" {% if forloop.first %}checked{% endif %}>
            <label for="ailment-tab-{{ forloop.counter }}">{{ ailment.name }}</label>
            {% endfor %}

            {% for ailment in ailments %}
            <div class="content treatment-content">
                <div class="col-wrap dflex flexwrap centered-items">
                    <div class="col col4">
                        <img src="{{ ailment.image.url }}" alt="{{ ailment.name }}" width="340" height="340">
                    </div>
                    <div class="col col8">
                        <div class="para-wrap">
                            {{ ailment.description|safe }}
                        </div>
                    </div>
                </div>
            </div>
            {% endfor %}
        </div>
    </div>
</section>
```

### 9. Technology Section
```django
<section class="technology-section py-50 content-section" id="technology-section">
    <div class="heading mb-10 text-center">Latest Technology Utilisation</div>
    <div id="technology-slider" class="space-row slick-arrow-style-1 slider-tb-shadow">
        {% for tech in technologies %}
        <div class="technology-card">
            <div class="thumb">
                <img src="{{ tech.image.url }}" alt="{{ tech.name }}" width="340" height="340">
            </div>
            <div class="card-desk">
                <div class="medantaxsheading font700 clr-dark mb-10">{{ tech.name }}</div>
                <div class="para-wrap">
                    <p>{{ tech.short_description }}</p>
                </div>
            </div>
        </div>
        {% endfor %}
    </div>
</section>
```

### 10. Sub-Specializations (Accordion)
```django
<section class="py-50 content-section" id="sub-specialisations-section1">
    <div class="container">
        <div class="heading mb-30 clr-dark text-center">Sub-Specializations</div>
        <div class="accordion-wrapper">
            {% for item in subspecializations %}
            <div class="accordion-item">
                <input type="checkbox" id="accordion-{{ item.id }}">
                <label for="accordion-{{ item.id }}" class="accordion-header">
                    <h3>{{ item.title }}</h3>
                    <span class="accordion-icon">+</span>
                </label>
                <div class="accordion-content">
                    <div class="para-wrap">
                        {{ item.description|safe }}
                    </div>
                </div>
            </div>
            {% endfor %}
        </div>
    </div>
</section>
```

### 11. Success Stories
```django
{% if success_stories %}
<section class="py-50 content-section" id="patientstories-section">
    <div class="container">
        <div class="heading mb-30 clr-dark text-center">Success Stories</div>
        <div class="stories-slider">
            {% for story in success_stories %}
            <div class="story-card">
                {% if story.image %}
                <img src="{{ story.image.url }}" alt="{{ story.title }}">
                {% endif %}
                <h4>{{ story.title }}</h4>
                {% if story.patient_name %}
                <p class="patient-name">{{ story.patient_name }}</p>
                {% endif %}
                <div class="story-content">{{ story.story|safe }}</div>
                {% if story.video_url %}
                <a href="{{ story.video_url }}" target="_blank">Watch Video</a>
                {% endif %}
            </div>
            {% endfor %}
        </div>
    </div>
</section>
{% endif %}
```

## Important Notes

1. **Image URLs**: Always use `.url` property for ImageFields: `{{ service.banner_image_desktop.url }}`

2. **Check if image exists**:
```django
{% if service.banner_image_mobile %}
    <img src="{{ service.banner_image_mobile.url }}" alt="{{ service.name }}">
{% endif %}
```

3. **Safe filter**: Use `|safe` for HTML content stored in text fields:
```django
{{ treatment.description|safe }}
```

4. **Loop counters**: Use `{{ forloop.counter }}` for unique IDs in loops

5. **First item**: Use `{% if forloop.first %}` to mark the first item in a loop

## Next Steps

1. Open `base/templates/base/service-detail.html`
2. Find each section (search for the section IDs like `#treatment-section`, `#ailment-section`, etc.)
3. Replace the static HTML with the dynamic template code shown above
4. Test with a service created in the admin panel

## Testing

After updating the template:
1. Run migrations: `python manage.py makemigrations && python manage.py migrate`
2. Create a superuser: `python manage.py createsuperuser`
3. Access admin: http://localhost:8000/admin
4. Create a new Service with all related content
5. Visit: http://localhost:8000/service/your-service-slug/
