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

[Cheat-Sheets](/cheat-sheets/quickstart)
{: .label .label-blue }

---

The <i>{{site.title}}</i> uses a global configuration located in `config/config.json` to record information that is not analysis-specific. This file contains a top-level JSON `object` to record the configuration options. These broadly include:

- [Environment Options](installation/environment-related)
  - [Scheduler Profiles](installation/scheduler-profiles)
  - [Software](installation/scheduler-profiles)
- [Reference Genomes](installation/reference-genomes)




<!-- TODO: Move to the cheat-sheet -->
{::options parse_block_html="true" /}

<details><summary class="text-delta" markdown="span">A bare-bones example <code>config.json</code></summary>
```json
{
    "reference-genomes": [
        {
            "version": "GRCh38",
            "file_path": [
                "/",
                "path",
                "to",
                "my",
                "copy",
                "of",
                "GRCh38.fa.gz"
            ]
        }
    ],
    "environment": {
        "email": {
            "address": "jane.doe@tuks.co.za",
            "conditions": [
                "o",
                "e"
            ]
        },
        "working-directory": "/path/to/my/working/directory/",
        "queues": [
            {
                "queue": "long",
                "walltime": "900:00:00",
                "memory": "128G",
                "cores": "10",
                "nodes": "1",
                "rules": [
                    "all",
                    "VALIDATE",
                    "LIFTOVER",
                    "COLLATE",
                    "ALL_COLLATE",
                    "ANNOTATE",
                    "ADMIXTURE",
                    "TRIM_AND_NAME",
                    "FILTER",
                    "TRANSPILE_CLUSTERS",
                    "PLINK"
                ]
            }
        ],
        "envmodules": {
            "bcftools": "bcftools-1.7",
            "piccard": "picard-2.17.11",
            "tabix": "samtools-1.7",
            "latex": "latex"
        }
    }
}
```
</details>

{::options parse_block_html="false" /}

