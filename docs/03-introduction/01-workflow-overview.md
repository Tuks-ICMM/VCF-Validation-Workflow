---
title: Workflow Overview
layout: page
permalink: workflow-design/analysis
nav_order: 1
parent: Workflow Design
---

# Workflow Overview
{: .no_toc }

A breakdown of the analyses performed by this workflow.
{: .fs-6 .fw-300 }

[Cheat-Sheets](/cheat-sheets/quickstart)
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

The {{ site.title }} design follows the following order-of-events graph:

```mermaid
timeline
    title Workflow Design

    section VCF Validation Workflow
        PREPARE : Remove INFO column : Normalize INDELs : Sort Variants: Filter QUAL scores: Annotate
        LIFTOVER : Liftover
```