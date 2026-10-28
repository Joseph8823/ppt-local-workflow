# Acceptance and handoff record

Keep this record with the project deliverables, outside the public skill source. Scale detail to the task: a single title fix needs a short affected-slide report; a reconstructed whole deck needs page-level evidence.

Record:

1. **Scope:** requested formats, agreed page counts, entry stage, approved content/visual-reference version and any affected page IDs.
2. **Native environment:** application identity/version and measured page dimensions. For SVG, include root dimensions, viewBox, insertion rectangle and mapping ratios.
3. **Checks actually performed:** source/static checks, editing-canvas inspection, inserted/converted comparison where relevant, export resolution, relocation and reopen checks. Mark unavailable checks as pending.
4. **Per-page object counts:** actual converted/native text frames, whole picture objects and other leaf shapes. Describe table cells or charts separately when present. Do not count grouping containers twice.
5. **Visual outcome:** wrapping, line width/height, baseline/start positions, boundaries, spacing, picture placement and visible collisions. Specify measured versus visual observations and any use of a baseline proxy.
6. **Remaining differences:** fonts, frame splitting, approximation of complex art, numeric target exceptions and uncompleted checks. State the actual editable scope.
7. **Final files:** exact saved paths, tested file version/integrity and which preview is for review. Distinguish final deliverables from temporary test documents.

Example page summary, using invented counts:

| Page | Native text frames | Whole pictures | Other leaf shapes | Review |
|---|---:|---:|---:|---|
| 01 | 3 | 1 | 2 | No visible overflow; two-state check performed |
| 02 | 8 | 1 | 5 | One short label has a documented height difference |

Do not infer visual success from this table or from an SVG source count. Static validation, exported-image review and native application review are distinct evidence. A screenshot demonstrates appearance at a moment in time, not text editability. A saved PPTX establishes a file exists, not that its media, text and layout survived reopening.

After relevant checks pass, stop expanding verification unless a new change or unresolved concern justifies it. Consolidate minor acceptable differences. Never hide a material failure behind “all checks passed.”
