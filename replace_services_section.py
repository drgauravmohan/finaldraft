#!/usr/bin/env python3
"""Replace the static Services section with dynamic Django template."""

# Read the template
with open('base/templates/base/index.html', 'r') as f:
    content = f.read()

# Find the Services section - looking for the wire:id marker and the static service cards
start_marker = '<div wire:id="WtnOzdKJSBVAIqVvoH1T"'
end_marker = '<!-- Livewire Component wire-end:WtnOzdKJSBVAIqVvoH1T --></section>'

start_idx = content.find(start_marker)
end_idx = content.find(end_marker)

if start_idx == -1 or end_idx == -1:
    print(f"Markers not found! start_idx={start_idx}, end_idx={end_idx}")
    exit(1)

# Find the actual content div (the one with the service cards)
# We want to replace from the div with class "space-row3" to just before the wire-end comment
content_start = content.find('<div class=" space-row3 slider-tb-shadow', start_idx)
content_end = content.find('</div>', content_end) # Find the closing div before wire-end

new_content = '''<div class="space-row3 slider-tb-shadow wow fadeInUp" data-wow-delay=".3s">
            <div class="slide-item">
                <div class="services-doc dflex space-between">
                    {% for service in services_section_services %}
                    {% if forloop.counter == 1 %}
                    <div class="technology-card">
                        <div class="thumb thumb-ratio thumb-ratio1">
                            {% if service.card_image %}
                            <img loading="lazy" width="540" height="300" src="{{ service.card_image.url }}" alt="{{ service.name }}">
                            {% endif %}
                        </div>
                        <div class="card-desk">
                            <div class="heading-md font600 card-title hidden-xs mb-2">{{ service.name }}</div>
                            <div class="card-text">
                                <p>{{ service.short_description }}</p>
                            </div>
                            <div class="card-button dflex space-between centered-items">
                                <div class="common-button">
                                    <a href="{% url 'base:service-detail' service.slug %}" class="anchor-button">Know More
                                        <span></span> </a>
                                </div>
                                <div class="services-logo">
                                    {% if service.logo_image %}
                                    <img loading="lazy" width="100" height="100" src="{{ service.logo_image.url }}" alt="{{ service.name }}-logo">
                                    {% endif %}
                                </div>
                            </div>
                        </div>
                    </div>
                    {% elif forloop.counter == 2 %}
                    <div class="technology-card-b">
                        <div class="card-desk">
                            <div class="heading-md font600 card-title hidden-xs mb-2">{{ service.name }}</div>
                            <div class="card-text">
                                <p>{{ service.short_description }}</p>
                            </div>
                            <div class="card-button dflex space-between centered-items">
                                <div class="common-button">
                                    <a href="{% url 'base:service-detail' service.slug %}" class="anchor-button">Know More
                                        <span></span> </a>
                                </div>
                                <div class="services-logo">
                                    {% if service.logo_image %}
                                    <img loading="lazy" width="100" height="100" src="{{ service.logo_image.url }}" alt="{{ service.name }}-logo">
                                    {% endif %}
                                </div>
                            </div>
                        </div>
                    {% elif forloop.counter == 3 %}
                        <div class="card-desk">
                            <div class="heading-md font600 card-title hidden-xs mb-2">{{ service.name }}</div>
                            <div class="card-text">
                                <p>{{ service.short_description }}</p>
                            </div>
                            <div class="card-button dflex space-between centered-items">
                                <div class="common-button">
                                    <a href="{% url 'base:service-detail' service.slug %}" class="anchor-button">Know More
                                        <span></span> </a>
                                </div>
                                <div class="services-logo">
                                    {% if service.logo_image %}
                                    <img loading="lazy" width="100" height="100" src="{{ service.logo_image.url }}" alt="{{ service.name }}-logo">
                                    {% endif %}
                                </div>
                            </div>
                        </div>
                    </div>
                    {% elif forloop.counter == 4 %}
                    <div class="technology-card">
                        <div class="thumb thumb-ratio thumb-ratio1">
                            {% if service.card_image %}
                            <img loading="lazy" src="{{ service.card_image.url }}" alt="{{ service.name }}" width="540" height="300">
                            {% endif %}
                        </div>
                        <div class="card-desk">
                            <div class="heading-md font600 card-title hidden-xs mb-2">{{ service.name }}</div>
                            <div class="card-text">
                                <p>{{ service.short_description }}</p>
                            </div>
                            <div class="card-button dflex space-between centered-items">
                                <div class="common-button">
                                    <a href="{% url 'base:service-detail' service.slug %}" class="anchor-button">Know More
                                        <span></span> </a>
                                </div>
                                <div class="services-logo">
                                    {% if service.logo_image %}
                                    <img loading="lazy" src="{{ service.logo_image.url }}" alt="{{ service.name }}-logo" width="100" height="100">
                                    {% endif %}
                                </div>
                            </div>
                        </div>
                    </div>
                    {% endif %}
                    {% endfor %}
                </div>
            </div>

        </div>'''

# We need to replace from the actual content start to a better end point
# Let me find the section more precisely
section_start = content.find('<div class="space-row3 slider-tb-shadow', start_idx)
# Find the end of this section - look for the closing tag of the wire component
section_end = content.find('</div>', content.find('</div>', content.find('</div>', section_start) + 1) + 1) + 6

before = content[:section_start]
after = content[section_end:]

new_full_content = before + new_content + after

# Write back
with open('base/templates/base/index.html', 'w') as f:
    f.write(new_full_content)

print("Services section has been replaced with dynamic template!")
