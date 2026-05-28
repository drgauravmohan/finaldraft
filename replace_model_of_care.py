#!/usr/bin/env python3
"""Replace the static Model of Care section with dynamic Django template."""

# Read the template
with open('base/templates/base/index.html', 'r') as f:
    content = f.read()

# Find the start - after the center image
start_marker = '<img  loading="lazy" wire:ignore src="https://sudharshan heart clinic.s3.ap-south-1.amazonaws.com/why-sudharshan heart clinic/January2025/SAaBLwOTiDeA1koPWX1qrQb6Ddqj0F-metadHJ1c3QtYmFzZWQtY29tcGFzc2lvbmF0ZS1jYXJlLW1vYmlsZS53ZWJw-.webp" alt="Dermatology" class="center-image" width="450" height="450"/>'
start_idx = content.find(start_marker)

if start_idx == -1:
    print("Start marker not found!")
    exit(1)

# Start after this image tag - look for the next line
content_start = content.find('\n\n\n', start_idx) + 3  # Skip the newlines

# Find the end - look for the pattern after the last service block
end_marker = '                    </div>\n\n                            </div>'
end_idx = content.find(end_marker, content_start)

if end_idx == -1:
    print("End marker not found!")
    exit(1)

# The end position should be right at the end_idx (before the closing div)
content_end = end_idx

# The new dynamic content - using forloop.counter to assign correct block class
new_content = '''{% for service in model_of_care_services %}
                    {% if forloop.counter == 1 %}
                    <div class="why-block blocking-hover wow fadeInDown" data-wow-delay=".3s">
                        <div class="click-text">
                            <div class="block-head {% if forloop.first %}active{% endif %}">{{ service.name }}</div>
                            <div class="common-button">
                                <a href="{% url 'base:service-detail' service.slug %}" class="anchor-button">Know More
                                    <span></span> </a>
                            </div>
                        </div>
                        <a href="{% url 'base:service-detail' service.slug %}" class="abc">
                            {% if service.model_of_care_image %}
                            <div datasrc="{{ service.model_of_care_image.url }}" class="click-circle {% if forloop.first %}active{% endif %}"></div>
                            {% else %}
                            <div class="click-circle {% if forloop.first %}active{% endif %}"></div>
                            {% endif %}
                        </a>
                    </div>
                    {% elif forloop.counter == 2 %}
                    <div class="why-block-b blocking-hover wow fadeInRight" data-wow-delay=".5s">
                        <a href="{% url 'base:service-detail' service.slug %}" class="abc">
                            {% if service.model_of_care_image %}
                            <div datasrc="{{ service.model_of_care_image.url }}" class="click-circle"></div>
                            {% else %}
                            <div class="click-circle"></div>
                            {% endif %}
                        </a>
                        <div class="click-text">
                            <div class="block-head">{{ service.name }}</div>
                            <div class="common-button">
                                <a href="{% url 'base:service-detail' service.slug %}" class="anchor-button">Know More
                                    <span></span> </a>
                            </div>
                        </div>
                    </div>
                    {% elif forloop.counter == 3 %}
                    <div class="why-block-c blocking-hover wow fadeInRight" data-wow-delay=".7s">
                        <a href="{% url 'base:service-detail' service.slug %}">
                            {% if service.model_of_care_image %}
                            <div datasrc="{{ service.model_of_care_image.url }}" class="click-circle"></div>
                            {% else %}
                            <div class="click-circle"></div>
                            {% endif %}
                        </a>
                        <div class="click-text">
                            <div class="block-head">{{ service.name }}</div>
                            <div class="common-button">
                                <a href="{% url 'base:service-detail' service.slug %}" class="anchor-button">Know More
                                    <span></span> </a>
                            </div>
                        </div>
                    </div>
                    {% elif forloop.counter == 4 %}
                    <div class="why-block-d blocking-hover wow fadeInLeft" data-wow-delay=".7s">
                        <div class="click-text">
                            <div class="block-head">{{ service.name }}</div>
                            <div class="common-button">
                                <a href="{% url 'base:service-detail' service.slug %}" class="anchor-button">Know More
                                    <span></span> </a>
                            </div>
                        </div>
                        <a href="{% url 'base:service-detail' service.slug %}">
                            {% if service.model_of_care_image %}
                            <div datasrc="{{ service.model_of_care_image.url }}" class="click-circle"></div>
                            {% else %}
                            <div class="click-circle"></div>
                            {% endif %}
                        </a>
                    </div>
                    {% elif forloop.counter == 5 %}
                    <div class="why-block-e blocking-hover wow fadeInLeft" data-wow-delay=".5s">
                        <div class="click-text">
                            <div class="block-head">{{ service.name }}</div>
                            <div class="common-button">
                                <a href="{% url 'base:service-detail' service.slug %}" class="anchor-button">Know More
                                    <span></span> </a>
                            </div>
                        </div>
                        <a href="{% url 'base:service-detail' service.slug %}">
                            {% if service.model_of_care_image %}
                            <div datasrc="{{ service.model_of_care_image.url }}" class="click-circle"></div>
                            {% else %}
                            <div class="click-circle"></div>
                            {% endif %}
                        </a>
                    </div>
                    {% endif %}
                {% endfor %}

                            '''

before = content[:content_start]
after = content[content_end:]

new_full_content = before + new_content + after

# Write back
with open('base/templates/base/index.html', 'w') as f:
    f.write(new_full_content)

print("Model of Care section has been replaced with dynamic template!")
print(f"Replaced from position {content_start} to {content_end}")
