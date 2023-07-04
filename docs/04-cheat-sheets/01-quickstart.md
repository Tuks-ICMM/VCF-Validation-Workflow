---
title: Quickstart
layout: page
parent: Cheat Sheets
nav_order: 1
permalink: cheat-sheets/quickstart
---

# Quickstart
{: .no_toc }

A series of reference resources aimed at end-users.
{: .fs-6 .fw-300 }

Quickstart
{: .label }

Templates
{: .label }

---


{::options parse_block_html="true" /}

<details><summary markdown="span"><code>config.json</code></summary>
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

{::options parse_block_html="true" /}

<details><summary markdown="span"><code>email</code> value</summary>
```json
{
    "address": "your_email",
    "conditions": [
        "o",
        "e"
    ]
}
```
</details>

{::options parse_block_html="false" /}

{::options parse_block_html="true" /}

<details><summary markdown="span"><code>envmodules</code> value</summary>
```json
{
    "bcftools": "bcftools-1.7",
    "piccard": "picard-2.17.11",
    "tabix": "samtools-1.7",
    "latex": "latex"
}
```
</details>

{::options parse_block_html="false" /}


{::options parse_block_html="true" /}

<details><summary markdown="span"><code>reference_genome</code> list item</summary>
```json
{
    "version": "GRCh38",
    "file_path": [
        "/",
        "path",
        "here",
        "GRCh38.fa.gz"
    ]
}
```
</details>

{::options parse_block_html="false" /}

{::options parse_block_html="true" /}

<details><summary markdown="span"><code>queue</code> list item</summary>
```json
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
```
</details>

{::options parse_block_html="false" /}