# ctm-consistency-checker

Script to check consistency of CTM files

### Background

CTM (ISO 13250-6: Topic Maps — Compact Syntax (CTM); http://www.isotopicmaps.org/ctm/) is 'a textual notation to describe topic maps'. Because we currently create these files manually and all concept types need to be defined, we needed a script to perform a very basic format check.

The script locates all mentions (named 'concepts' in the script) of one of the CONCEPT_TYPES and checks whether each of these concepts occurs twice. If a concept occurs only once, it is considered undefined and should be checked and corrected.

### Usage

> python checkCTMconsistency.py example.ctm

### Sample output

```
Checking example.ctm
SINGLE mention of concept: group:PT_TestCase_AgeOver18_inclusion_criteria
SINGLE mention of concept: cell:PT_TestCase_AgeOver18_adults
SINGLE mention of concept: group:PT_TestCase_AgeOver18_inclusion
SINGLE mention of concept: cell:PT_TestCase_AgeOver18_adult
Done checking
```
