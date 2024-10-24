---
title: Workflow Overview
layout: page
permalink: introduction/workflow-overview
nav_order: 1
parent: Introduction
---

# Introduction
{: .no_toc }

A breakdown of the analyses performed by this workflow.
{: .fs-6 .fw-300 }

<a href="{{ site.baseurl }}/cheat-sheets/quickstart" style="color: #44434d; text-decoration: none;" target="_blank"><strong><i>Cheat-Sheets</i></strong></a>
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
flowchart TD

  classDef bcftools stroke:#FF5733,fill:#D3D3D3,stroke-width:4px,color:black;
  classDef plink stroke:#36454F,fill:#D3D3D3,stroke-width:4px,color:black;
  classDef python stroke:#FEBE10,fill:#D3D3D3,stroke-width:4px,color:black;
  classDef admixture stroke:#333,fill:#D3D3D3,stroke-width:4px,color:black;
  classDef tabix stroke:#023020,fill:#D3D3D3,stroke-width:4px,color:black;
  classDef gatk stroke:#007FFF,fill:#D3D3D3,stroke-width:4px,color:black;
  classDef workflow stroke:#fff,fill:#000000,stroke-width:4px,color:white;

  subgraph ValidateVcfWorkflow [Validate VCF Workflow]
      wipeInfo[[**wipeInfo**:
  Remove INFO column for computational processing  efficiency]]
      normalize[[**normalize**:
  Normalize all SNPs]]
      sort[[**sort**:
  Ensure correct variant order]]
      filter[[**filter**:
  Remove all variants except SNPs]]
      annotate[[**annotate**:
  Annotate VCF against given reference VCF such as dbSNP, and rename any unknown variants.]]

      tabix[[**tabix**: Generate tabix-index for targeted decompression]]

      class tabix tabix;
      class wipeInfo,normalize,sort,filter,annotate bcftools;

      subgraph liftoverProtocol [Liftover]
          direction LR
          liftoverProtocolStart(((Start)))
          liftover[[liftover:
  Perform reference genome
  liftover]]
          liftoverProtocolEnd(((End)))
          ifLiftoverRequired{Is a
  liftover
  required?}

          liftoverProtocolStart --> ifLiftoverRequired
          ifLiftoverRequired --> |yes| liftover --> liftoverProtocolEnd
          ifLiftoverRequired --> |no| liftoverProtocolEnd
          class liftover gatk;
      end

      tabix --> wipeInfo & normalize & sort & filter & annotate
      wipeInfo --> normalize --> sort --> filter --> annotate --> liftoverProtocol
  end
```