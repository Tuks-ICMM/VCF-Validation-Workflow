---
title: Reference-Genomes
layout: page
permalink: installation/reference-genomes
nav_order: 1
parent: Installation
has_children: false
---

# Reference Genomes
{: .no_toc }

How to declare a reference-genome for use
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

You may configure a list to describe available reference genomes in the form of an `array` of `objects`. Each object requires the following information:

<dl class="def-wide">
  <dt><strong>version</strong>
    <code>&lt;str&gt;</code>
  </dt>
  <dd>The version string to be used to access this reference genome in the pipeline input files.
    <br><strong>
      <i>E.g.
        <code>GRCh38</code>
      </i>
    </strong>
  </dd>

  <dt><strong>file_path</strong>
    <code>&lt;array [str]&gt;</code>
  </dt>
  <dd>An array containing the decomposed location of the dataset to be used in the analysis. See the note below for additional information.
    <br><strong>
      <i>E.g.
        <code>["/", "reference", "human", "GRCh38.fa.gz"]</code>
      </i>
    </strong>
  </dd>
</dl>

{: .normal }
> We use the built-in python function `os.path` to generate platform-specific paths. Should you wish to provide a path from root, you may do so by setting the first element in the array to the drive reference for your OS. \***\*Linux E.g. ["/", ...]\*\***

{::options parse_block_html="true" /}

<details><summary class="text-delta" markdown="span">Example <code>"reference_genome"</code> entry</summary>
```json
{
  "reference_genome": [
    {
      "version": "GRCh38",
      "file_path": ["/", "reference", "human", "GRCh38.fa.gz"]
    },
    {
      "version": "GRCh37",
      "file_path": ["/", "reference", "human", "GRCh37.fa.gz"]
    }
  ]
}
```
</details>

{::options parse_block_html="false" /}

{: .normal-title }
> Performance Tips
>
> Users are encouraged to use compression and indexing for performance gain when using reference genomes. Block compression (BGZIP), such as that provided by [SamTools](http://www.htslib.org/doc/bgzip.html), can be used to compress a wide variety of bioinformatics file formats, including `FASTA` files. In order to decompress the blocks created through Block compression, you will also need to create an apropriate index file describing the contents of each block.
>
>An example fileset for the `GRCH38` reference genome would include:
>-  `GRCh38.fa.gz.gzi` file (Can be generated during compression) ([Samtools]>(http://www.htslib.org/doc/bgzip.html))
>-  `GRCh38.dict` file ([Samtools](http://www.htslib.org/doc/samtools-dict.html))
>-  `GRCh38.fa.gz.fai` file ([Samtools](http://www.htslib.org/doc/samtools-faidx.html))

{: .normal-title}
> Should I include the index files in my `config.json`?
>
> The accomanying index files need only be named and stored alongside the compressed file. They do not need to be listed in the `reference_genome` configuration entry.


---
## Environment-related options

The _{{ site.title }}_ supports several environmental-related options which are set in the `config/config.json` as follows:

### `environment` (`Object`)

This object contains the configuration for all infrastructure-related configurations. These include:

---
#### `email` (`Object`)
If your PBS/Torque systems email notifications have been configured, you may configure a  notification email as follows:

<dl class="def-wide">
  <dt><strong>email</strong> <code>&lt;str [Email]&gt;</code></dt>
  <dd>An email address to which the notification should be sent.</dd>

  <dt><strong>conditions</strong> <code>[ &lt;enum ['o', 'e']&gt; ]</code></dt>
  <dd>An array of mail-options which indicates when you should receive a notification email for this pipeline execution. <code>a</code> indicates mail should be sent when job is aborted, <code>b</code> indicates mail should be sent when job begins and <code>e</code> indicates mail should be sent when job terminates.</dd>
</dl>

{::options parse_block_html="true" /}

<details><summary class="text-delta" markdown="span">Example <code>'email'</code> entry</summary>
```json
{
    "email": {
        "email": "jane.doe@university.com",
        "conditions": ["o", "e"],
    }
}
```
</details>

{::options parse_block_html="false" /}

#### `queues`
The PBS-Torque batch scheduling system manages per-installation generic resources like memory, time, and cpus which are available for request by users. The _{{ site.title }}_ has been designed to take advantage of the granularity provided by these scheduler systems. Each rule in the workflow can be split into a separate job submissions on a cluster. As a result, it is possible to parallelize the analysis and assign cluster resources on a per-rule basis.

To do this, you may use the `queue` key to describing the available PBS-Torque resources and queues you would like to use. These can be described as follows:

{: .normal-title }
> Custom core and node selections
>
> In some cases, users might want to run some jobs on multiple nodes and some on single nodes. To support this, you may declare the same underlying queue multiple times with a different `queue` key in the config file and create multiple versions of the same underlying hardware queue.

{: .note }
> It is recommended that you submit the workflow execution script with the longest available walltime as this will create a watcher process who is responsible for queueing each rule and monitoring their states. If this process is interupted, the workflow will cease.

<dl>
  <dt><strong>queue</strong> <code>&lt;str&gt;</code></dt>
  <dd>The name of the queue.</dd>
  
  <dt><strong>walltime</strong> <code>&lt;str&gt;</code></dt>
  <dd>The maximum walltime jobs on this queue are permitted to execute in a HH:MM:SS format.
  <br><i>E.g. "900:00:00" = 37.5 days</i></dd>

  <dt><strong>memory</strong> <code>&lt;str&gt;</code></dt>
  <dd>The amount of RAM available on this queue.
  <br><i>E.g. 128G</i></dd>

  <dt><strong>cores</strong> <code>&lt;str&gt;</code></dt>
  <dd>The number of cores available on this queue.
  <br><i>E.g. 10</i></dd>

  <dt><strong>nodes</strong> <code>&lt;str&gt;</code></dt>
  <dd>The number of nodes available in this queue.
  <br><i>E.g. 1</i></dd>

  <dt><strong>rules</strong> <code>&lt;array [&lt;str&gt;]&gt;</code></dt>
  <dd>An array of rules this rule should be used for. For a reference of rules, please reference the rules list included in teh example below.</dd>
</dl>


{::options parse_block_html="true" /}

<details><summary class="text-delta" markdown="span">Example <code>'queues'</code> entry </summary>
```json
{
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
  ]
}
```
</details>

{::options parse_block_html="false" /}

#### `envmodules`
The `envmodules` key allows users to provide [Environment Modules]() accessor names. These are used internally by snakemake to execute the required `module load` commands before queued rule execution. `module load` name accessors will be needed for the following command-line tools: 
- plink-2
- plink-1.9
- bcftools
- samtools
- piccard
- structure
- admixture-1.3
- python-3
- r
- latex


{::options parse_block_html="true" /}

<details><summary class="text-delta" markdown="span">Example <code>'envmodules'</code> entry</summary>
```json
{
  "envmodules": {
    "plink-2": "plink-2",
    "plink-1.9": "plink-1.9",
    "bcftools": "bcftools",
    "samtools": "samtools",
    "piccard": "piccard",
    "structure": "structure",
    "admixture-1.3": "admixture-1.3",
    "python-3": "python-3",
    "r": "r",
    "latex": "latex"
  }
}
```
</details>

{::options parse_block_html="false" /}