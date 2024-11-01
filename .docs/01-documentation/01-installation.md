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


This workflow is maintained and distributed through the [ICMM GitHub page](https://github.com/Tuks-ICMM). The source-code has been versioned according to publications and relevant checkpoints, and can be downloaded via a git clone command:

```bash
git clone https://github.com/Tuks-ICMM/VCF-Validation-Workflow.git
```

If you would like to clone a specific version, versions are declared and maintained via the repositories [releases page](https://github.com/Tuks-ICMM/VCF-Validation-Workflow/tags). To access a version, users can clone the repository, and perform a <code>checkout</code> command, providing the version to checkout:

```bash
git clone https://github.com/Tuks-ICMM/VCF-Validation-Workflow.git
git checkout tags/<release_version>
```


## Dependencies

This workflow is built and powered using a python-based framework for workflow management. In addition, we make use of several underlying bioinformatics tools and third-party command-line programs to perform some steps in the analysis (For more information, see the [methodology page](/workflow/methodology)):

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
