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
## [v1.1.2-ALPHA](https://github.com/Tuks-ICMM/Vcf-Validation/compare/v1.1.1-ALPHA...v1.1.2-ALPHA) (2023-02-20)

### VALIDATE and LIFTOVER changes
Changes to `VALIDATE`:

- Reordered steps to ensure that file sizes are reduced as early as possible.
- Added parameters to subset samples according to user specified list `/input/{dataset}_samples_subset.txt`
- Added parameters to filter out variants not passing QC checks ('PASS' in FILTER column of VCF).
- Added file for naming chromosomes according to custom parameters `/input/rename_chr.txt`

Changes to `00 - LIFTOVER.py` file:

- Files that have undergone the `LIFTOVER` process are unsorted. This can interfere with downstream analyses. Functionality has been added to sort the files by chromosome. 
- Variants of files that have undergone `LIFTOVER` are renamed; however, this was not the case for files that did not need `LIFTOVER`. Functionality was added to rectify this.

## [v1.1.1-ALPHA](https://github.com/Tuks-ICMM/Vcf-Validation/compare/v1.1.0-ALPHA...v1.1.1-ALPHA) (2023-02-07)

### Bugs
- the `Tabix` program provided as part of `HTSLib` was not properly called. The appropriate package load command has been added to ensure a tabix-index is produced and copied over to the proceeding rule. Thank you to <a href="https://github.com/MeganHolborn" target="_blank">{% avatar MeganHolborn size=15 %} Megan Holborn</a>.

---
## [v1.1.0-ALPHA](https://github.com/Tuks-ICMM/Vcf-Validation/compare/e4a612a...v1.1.0-ALPHA) (2023-01-24)

### Features
- remove unnecessary `FORMAT` annotations in incoming `.vcf.gz` files genotype columns.
