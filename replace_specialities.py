#!/usr/bin/env python3
"""Replace the static Specialities section with dynamic Django template."""

# Read the template
with open('base/templates/base/index.html', 'r') as f:
    content = f.read()

# Find the start - right after the opening div of sp-wrapper
start_marker = '<div class="sp-wrapper sp-center-filter">'
start_idx = content.find(start_marker)

if start_idx == -1:
    print("Start marker not found!")
    exit(1)

# Start after the opening tag
content_start = start_idx + len(start_marker)

# Find the end - look for the closing div of sp-wrapper (it's followed by two newlines and more divs)
# We want to find "</div>" that comes after all the service cards, then the two newlines, then another closing div
# The pattern to look for is the closing </a> of the last service, then "\n                            </div>\n"
end_marker = '</a>\n                            </div>\n'
content_end = content.find(end_marker, content_start)

if content_end == -1:
    print("End marker not found!")
    exit(1)

# Move to after the </a> tag
content_end = content.find('</a>', content_start + 5000) # Start searching from near the end

# The new dynamic content
new_content = '''
                {% for service in specialities_services %}
                    <a href="{% url 'base:service-detail' service.slug %}">
                        <div class="md-all-sp {% if forloop.first %}active{% endif %}">
                            <div class="md-all-spInner">
                                {% if service.icon %}
                                <img src="{{ service.icon.url }}" width="120" height="120" alt="{{ service.name }} icon" loading="lazy">
                                {% else %}
                                <svg width="120" height="120" viewBox="0 0 120 120" fill="none" xmlns="http://www.w3.org/2000/svg">
                                    <circle cx="60" cy="60" r="40" stroke="#58595B" stroke-width="2" fill="none"/>
                                    <path d="M60 30 L60 90 M30 60 L90 60" stroke="#58595B" stroke-width="2"/>
                                </svg>
                                {% endif %}
                                <span>
                                    {{ service.name }}
                                </span>
                            </div>
                            <div class="md-sp-arrowsvg">
                                <svg width="7" height="12" viewBox="0 0 7 12" fill="none"
                                     xmlns="https://www.w3.org/2000/svg">
                                    <path d="M1 0.999612L5.8 5.79961L1 10.5996" stroke="#58595B" stroke-width="2"
                                          stroke-linecap="round" stroke-linejoin="round"/>
                                </svg>
                            </div>
                        </div>
                    </a>
                {% endfor %}'''

before = content[:content_start]
after = content[content_end + 4:]  # +4 to skip past the </a> tag

new_full_content = before + new_content + after

# Write back
with open('base/templates/base/index.html', 'w') as f:
    f.write(new_full_content)

print("Specialities section has been replaced with dynamic template!")
print(f"Replaced content from position {content_start} to {content_end}")
