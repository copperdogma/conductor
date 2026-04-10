# Scout 011 — Evaluate MyFamilyTree and GEDCOM Adapter Opportunities

**Source**: `https://chronoplexsoftware.com/myfamilytree/updates/index.php`
**Status**: Defer
**Projects Reviewed**: dossier, storybook, doc-web, cine-forge

## Summary

My Family Tree is a live Windows genealogy app with explicit GEDCOM
interoperability work, including current GEDCOM 7 / GEDZIP support, direct
import for a wide set of older genealogy databases, merge tooling, and
documented vendor extensions for both GEDCOM 5.5.1 and GEDCOM 7 output.

The useful takeaway is not "adopt My Family Tree." The useful takeaway is that
Storybook has a plausible future interoperability lane if real user demand for
external family-tree import appears: accept GEDCOM 7 / GEDZIP as the first
honest exchange boundary, treat My Family Tree as a human-operated conversion
bridge and test corpus for older genealogy software, and avoid pretending the
Windows desktop app is a reusable runtime dependency.

That still does **not** justify action now. Storybook's active genealogy value
today is still conversation/artifact capture plus the accepted Dossier-backed
SCOPEEL pipeline. Dossier already covers genealogy-flavored prose and table
extraction, and Storybook already carries GEDCOM fixtures in its golden set.
What is missing is not standards awareness; it is a concrete product need for
importing existing external tree files.

## Project Relevance

- **dossier**: Low incremental value. Dossier already uses GEDCOM-informed
  relationship vocabulary and already owns genealogy prose/table extraction.
  Structured family-tree file parsing would be a separate adapter concern, not a
  good reason to widen Dossier core right now.
- **storybook**: Clear future owner if this ever ripens. Storybook already has
  an inbox note asking for a standalone genealogy parser, carries GEDCOM as a
  structured-data fixture shape, and is the product most likely to benefit from
  ingesting pre-existing family trees. The right future shape is a bounded
  Storybook-owned GEDCOM 7 / GEDZIP intake lane into SCOPEEL, not a new generic
  genealogy platform.
- **doc-web**: Low relevance. GEDCOM is already structured genealogy data, not
  document-to-HTML intake.
- **cine-forge**: No meaningful direct relevance.

## Recommendation

- Defer. Do **not** adopt My Family Tree as infrastructure, and do **not**
  start a new shared genealogy-parser subproject from this source alone.
- Hand the idea to Storybook as a future interoperability note:
  - if real import demand shows up, start with a narrow GEDCOM 7 / GEDZIP
    adapter story
  - keep ownership in Storybook until a real shared adapter boundary is proven
  - use My Family Tree only as a manual conversion bridge and regression corpus
    for older genealogy exports
- Keep one design guardrail:
  - Dossier remains the current lane for narrative/table genealogy extraction;
    any future GEDCOM work should focus on structured tree-file intake/export,
    not duplicate Dossier's text understanding role

## Confidence

- Medium-high. The source is concrete, current, and official, and the main
  uncertainty is product demand rather than source interpretation.

## Evidence

- Official My Family Tree source pages:
  - `https://chronoplexsoftware.com/myfamilytree/`
  - `https://chronoplexsoftware.com/myfamilytree/updates/index.php`
  - `https://chronoplexsoftware.com/myfamilytree/updates/versionhistory.htm`
  - `https://chronoplexsoftware.com/myfamilytree/help/faq.htm`
  - `https://chronoplexsoftware.com/myfamilytree/help/importingadatabase.htm`
  - `https://chronoplexsoftware.com/myfamilytree/help/merge.htm`
- My Family Tree extension references:
  - `https://chronoplexsoftware.com/gedcomextensions/mft-gedcom551-extensions-3.4.pdf`
  - `https://chronoplexsoftware.com/gedcomextensions/mft-gedcom7-extensions-1.3.pdf`
- GEDCOM standard references:
  - `https://gedcom.io/changelog/`
  - `https://gedcom.io/specifications/FamilySearchGEDCOMv7.pdf`
- Local product pressure:
  - `/Users/cam/Documents/Projects/Storybook/storybook/docs/inbox.md`
  - `/Users/cam/Documents/Projects/Storybook/storybook/docs/stories/story-026-golden-references.md`
  - `/Users/cam/Documents/Projects/Dossier/README.md`
  - `/Users/cam/Documents/Projects/Dossier/docs/stories/story-031-relationship-type-taxonomy.md`

## Open Questions

- Does Storybook actually need user-facing external family-tree import soon
  enough to outrank current conversation, artifact, and memory UX pressure?
- If import becomes real, is GEDCOM 7 alone sufficient for the first slice, or
  do real target users arrive with enough legacy-database formats to justify a
  manual conversion/test harness around My Family Tree immediately?
