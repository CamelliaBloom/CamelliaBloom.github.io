---
title:  "Read Bible -- Schudle"
last_modified_at: 2025-05-07T16:00:58-04:00
categories: 
  - Jekyll
tags:
  - Bible
  - Reading
toc: true
toc_label: "Getting Started"
author_profile: false
---


<table>
  <tr>
    <th>STARTING</th>
    <th>PASSAGES</th>
    <th>DONE</th>
  </tr>
  {% for row in site.data.read_bible %}
  <tr>
    <td>{{ row.STARTING }}</td>
    <td>{{ row.PASSAGES }}</td>
    <td>{{ row.DONE }}</td>
  </tr>
  {% endfor %}
</table>
