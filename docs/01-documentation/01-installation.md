---
title: Installation
layout: page
permalink: documentation/installation
nav_order: 1
has_children: false
parent: Documentation
---

# How to configure the workflow
{: .no_toc }

Infrastructure-related settings, standard analysis-agnostic data files, etc
{: .fs-6 .fw-300 }

Reference Genome Configuration
{: .label }

<a href="{{ site.baseurl }}/cheat-sheets/quickstart" style="color: #44434d; text-decoration: none;" target="_blank"><strong><i>Cheat-Sheets</i></strong></a>
{: .label .label-yellow }

---

This workflow has been designed using [Snakemake](https://snakemake.github.io/), a python library for building scalable, modular processing workflows using a domain-specific language based on Python.


## Configuration

The <i>{{site.title}}</i> workflow makes use of a configuration file, located in `config/config.json`, to declare system information required at runtime, which is not related to analysis. This file contains a top-level JSON `object` to record the configuration options. These have been broken down and are accessible via the table of contents below.
