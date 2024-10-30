---
title: Installation
layout: page
permalink: documentation/installation
nav_order: 1
has_children: false
parent: Documentation
---

# Installation
{: .no_toc }

Infrastructure-related settings, standard analysis-agnostic data files, etc
{: .fs-6 .fw-300 }

Reference Genome Configuration
{: .label }

<a href="{{ site.baseurl }}/cheat-sheets/quickstart" style="color: #44434d; text-decoration: none;" target="_blank"><strong><i>Cheat-Sheets</i></strong></a>
{: .label .label-yellow }

---

This workflow was created by <a href="https://github.com/G-kodes" target="_blank">{% avatar G-Kodes size=15 %} Graeme Ford</a> under the [Institute for Cellular and Molecular Medicine (ICMM)](https://www.up.ac.za/institute-for-cellular-and-molecular-medicine). This workflow is maintained and distributed through the [ICMM GitHub page](https://github.com/Tuks-ICMM), where releases are versioned for convenience.



## Dependencies overview

The <i>{{site.title}}</i> workflow makes use of a configuration file, located in `config/config.json`, to declare system information required at runtime, which is not related to analysis. This file contains a top-level JSON `object` to record the configuration options. These have been broken down and are accessible via the table of contents below.

This workflow is built and powered using a python-based framework for workflow management. In addition, we make use of several underlying bioinformatics toolkits and third-party command-line programs to perform some steps in the analysis (For more information, see the [methodology page](/workflow/methodology)).


- Download a copy of the [Pharmacogenetics Analysis Workflow](https://github.com/Tuks-ICMM/Pharmacogenetic-Analysis-Pipeline)
- Prepare a [Python](https://github.com/Tuks-ICMM/Pharmacogenetic-Analysis-Pipeline) environment with basic dependencies installed
- Download and install required CLI dependencies:
    - Python
    - BCFtools


### Python

In addition to powering the overall workflow management framework, this workflow makes use of Python scripts to perform data-processing, perform network calls (VEP), and perform data-aggregation where needed. To prevent conflicts with python versions, we recommend the use of conda environments.

{: .normal }
> With increased popularity and adoption of Python, many operating systems now include a stripped down python version for internal use. This does pose some logistical issues when a user may want to install a custom, complete installation for direct use. It is possible in many cases to mix and overwrite python versions unless a dedicated strategy or version-management system is used. This can be especially dangerous as depending on the damage to the OS python installation, fixing this issue may require re-installing the OS.


### BCFtools

[BCFtools](https://samtools.github.io/bcftools/bcftools.html) is a command-line bioinformatics program which provides a collection of functions to allow for the manipulation of variant call records found in VCF files. It has been used in several places to perform VCF file merging, normalization and other quality-control operations.

The best way to install this software is to compile a copy for your needs from the source files. Instructions for this can be found [here](https://samtools.github.io/bcftools/howtos/install.html)

{: .normal }
> Pre-compiled copies are available for use through other platforms such as package-managers (E.g. Ubuntu's `apt`), however these are typically not the most up-to-date version of the tool. For this reason, we recommend making use of a copy compiled from source for your needs, as this will grantee the latest available version.
