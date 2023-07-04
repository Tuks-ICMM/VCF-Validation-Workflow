---
title: Introduction
layout: page
permalink: introduction/analysis
nav_order: 1
parent: Introduction
---

# Introduction
{: .no_toc }

A breakdown of the analyses performed by this workflow.
{: .fs-6 .fw-300 }

<a href="{{ site.baseurl }}/cheat-sheets/quickstart" style="color: #44434d; text-decoration: none;"><strong><i>Cheat-Sheets</i></strong></a>
{: .label .label-yellow }

<details markdown="block">
  <summary>
    Table of contents
  </summary>
  {: .text-delta }
1. TOC
{:toc}
</details>

---

The <i>{{ site.title }}</i> design follows the following order-of-events graph:

```mermaid
timeline
    title Workflow Design

    section VCF Validation Workflow
        PREPARE : Remove INFO column : Normalize INDELs : Sort Variants: Filter QUAL scores: Annotate
        LIFTOVER : Liftover
```