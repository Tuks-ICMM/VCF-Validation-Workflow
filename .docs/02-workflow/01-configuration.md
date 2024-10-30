---
title: Configuration
layout: page
permalink: workflow/configuration
nav_order: 1
has_children: false
parent: Workflow
---

# Configuration
{: .no_toc }

Workflow design and input requirements
{: .fs-6 .fw-300 }

<details markdown="block">
  <summary>
    Table of contents
  </summary>
  {: .text-delta }
1. TOC
{:toc}
</details>

---

<h2><code>config</code> folder</h2>
To perform an analysis with this workflow, users will need to configure the workflow. This involves providing environment-related information like output locations.

<details markdown="block">
  <summary>
    <code>manifest.json</code> format example
  </summary>
  {: .text-delta }

  <dl>
    <dt>output-dir <code>&lt;Array&lt;Str&gt;&gt;</code></dt>
    <dd>A list representing the file-path for the location at which the workflow should save its output. If the folder does not exist, the workflow will automatically create it.</dd>
  </dl>

  ```json
  {
      "output-dir": [
          "/",
          "path",
          "to",
          "my",
          "output",
          "location"
      ]
  }
  ```
</details>
