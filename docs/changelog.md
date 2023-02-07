---
layout: page
title: Changelog
permalink: /changelog
nav_order: 5
---

# Changelog
{: .no_toc }

Recent changes to the _{{ site.title }}_.
{: .fs-6 .fw-300 }

Changelog
{: .label }

<details markdown="block">
  <summary>
    Table of contents
  </summary>
  {: .text-delta }
1. TOC
{:toc}
</details>

---

## [v1.1.1-ALPHA](https://github.com/Tuks-ICMM/Vcf-Validation/compare/v1.1.0-ALPHA...v1.1.1-ALPHA) (2023-02-07)

### Bugs
- the `Tabix` program provided as part of `HTSLib` was not properly called. The appropriate package load command has been added to ensure a tabix-index is produced and copied over to teh proceeding rule. Thank you to <a href="https://github.com/MeganHolborn" target="_blank">{% avatar MeganHolborn size=15 %} Megan Holborn</a>.

---
## [v1.1.0-ALPHA](https://github.com/Tuks-ICMM/Vcf-Validation/compare/e4a612a...v1.1.0-ALPHA) (2023-01-24)

### Features
- remove unnecessary `FORMAT` annotations in incoming `.vcf.gz` files genotype columns.
