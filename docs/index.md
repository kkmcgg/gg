---
literate_nav_exclude: true
---

# Welcome

This is Glossarium Geographia.

An operational database of geospatial terminology and tools is a chaotic work in progress—curated with a certain level of precision but still evolving. Navigate the sidebar to access definitions, references, and practical tools. Proceed with cautious curiosity and expect dynamic, iterative improvements as you explore the system.

All the magic happens in the [Glossary](glossary\AGRG)


Calling the test macro: {{ basic_test_macro() }}

---

## Discovered Headers Map:
Headers found in the '`{{ config.docs_dir }}/{{ SCAN_DIR_FOR_HEADERS_CONFIG }}`' directory:

{% if discovered_header_map is defined and discovered_header_map %}
<ul>
{% for header, stem in discovered_header_map.items() %}
  <li>'{{ header | e }}' was found in '<code>{{ stem | e }}.md</code>'</li>
{% endfor %}
</ul>
{% elif discovered_header_map is defined %}
<p>No headers were discovered in the specified directory.</p>
{% else %}
<p>Error: The 'discovered_header_map' variable was not defined.</p>
{% endif %}

---
End of test.