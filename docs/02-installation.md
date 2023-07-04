---
title: Installation
layout: page
permalink: installation
nav_order: 2
has_children: true
---

# How to configure the workflow
{: .no_toc }

How to set up infrastructure-related settings and provide standard analysis-agnostic data files like reference genomes, etc.
{: .fs-6 .fw-300 }

Reference Genome Configuration
{: .label }

<a href="{{ site.baseurl }}/cheat-sheets/quickstart" style="color: #44434d; text-decoration: none;"><strong><i>Cheat-Sheets</i></strong></a>
---

The <i>{{site.title}}</i> uses a global configuration located in `config/config.json` to record information that is not analysis-specific. This file contains a top-level JSON `object` to record the configuration options.
