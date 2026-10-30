# Acceptance and handoff record

Keep this record with the project deliverables, outside the public skill source. Scale detail to the task: a single title fix needs a short affected-slide report; a reconstructed whole deck needs page-level evidence.

Record:

1. **Scope:** requested formats, agreed page counts, entry stage, approved content/visual-reference version and any affected page IDs.
2. **Reviews and advance notices:** opening workflow/personal-review reminder; approved framework, actual sample image, exact wording and complete offline HTML versions; evidence of the user's approvals; immediate notice before local control. Identify any reused reviews or the scoped-edit route. Keep missing approvals pending rather than treating a generated artifact as approved.
3. **Native environment:** application identity/version and measured page dimensions. For SVG, include root dimensions, viewBox, final insertion rectangle, mapping ratios and HTML-to-slide normalization. Record template identity and actual target-system font families/weights; do not silently reuse another template's calibration.
4. **Checks actually performed:** source/static checks, deselected editing-canvas inspection for every inserted/converted page where relevant, three-way comparison against approved HTML, equal export resolution, final-directory reinsertion and authorized reopen checks. Record tested/delivered source identities. Distinguish missing native per-line inserted TextFrames from unavailable native access; mark unperformed checks/pages pending.
5. **Per-page object counts:** actual converted/native text frames, whole picture objects and other leaf shapes. For SVG, separate converted objects from pre-existing template objects. Describe table cells or charts separately when present. Do not count grouping containers twice.
6. **Visual outcome:** per-state wrapping, visible glyph height, complete line width, character spacing, baseline/start positions, right edge, line/paragraph spacing, picture placement and visible collisions. Record source anchors, visible ink boxes, converted native text bounds and shape bounds separately. Specify measured versus visual observations, comparison denominators, coordinate units and any baseline proxy; do not report source-derived bounds as native measured bounds.
7. **Remaining differences:** fonts, frame splitting, approximation of complex art, numeric target exceptions and uncompleted checks. State the actual editable scope.
8. **Final files:** exact saved paths, tested file version/integrity and which preview is for review. Distinguish final deliverables from temporary test documents.

Example page summary, using invented counts:

| Page | Native text frames | Whole pictures | Other leaf shapes | Review |
|---|---:|---:|---:|---|
| 01 | 3 | 1 | 2 | No visible overflow; two-state check performed |
| 02 | 8 | 1 | 5 | One short label has a documented height difference |

## SVG page and text evidence

For an SVG reconstruction, keep a short entry for **every** delivered page. Record the approved HTML page ID/version, final SVG identity/hash, target template/page size, insertion method/rectangle, viewBox/mapping, font family/weight and same-resolution export names for both native states. State whether both editing canvases were inspected deselected and whether reinsertion from the final directory preserved every embedded figure. Keep a source-figure-to-converted-picture mapping when a figure's integrity needs checking.

For each visible text line/label, use a stable ID and capture these fields in a table or equivalent record:

| Evidence | Approved HTML | Inserted SVG | Converted shapes |
|---|---|---|---|
| Wording, line breaks, start/baseline and right edge | Normalized reference | Native export/canvas observation | Native export/canvas observation |
| Visible glyph height and whole-line width | Reference/estimate with method | Measured/estimated ink with method | Measured/estimated ink with method |
| Source anchor/geometry | Reference coordinate mapping | SVG source value mapped to slide; not a native text bound | Source association, kept separate from native values |
| Native text/frame bounds | Not a PowerPoint measurement | Not applicable if only one SVG graphic exists; record graphic bounds separately | Actual native text bounds and frame bounds, or explicit access limitation |
| Spacing, wrapping, overflow/collision | Intended layout | Observed outcome | Observed outcome |

Record inserted/converted glyph-height and whole-line-width differences with the inserted measurements as denominators; normalize start displacement by actual slide width/height and baseline displacement by actual slide height. Record measurable normalized HTML deviations separately, using the HTML reference measurements as denominators rather than silently reusing the two-state calculation. State numerical target exceptions separately from layout failures. If exact ink or baseline measurement is unavailable, identify the visual estimate/proxy and its limits instead of implying precise metrology.

Report **actual converted leaf counts**, including all frames created from multiline text; neither the number of SVG elements nor a native group count proves editable object granularity. Complete-line paragraph splitting can be disclosed, but per-character body frames and fragmented original figures are failures. If pure SVG cannot meet a required single native paragraph TextFrame, explicitly state that limitation; a native-only repair in a temporary test file is not proof that the delivered SVG meets it.

Use separate per-page and overall statuses: passed, checked with documented numerical exceptions, pending, or failed. Unchecked pages cannot be included in an all-pages-passed claim. A numerical exception may be reported once checks are complete, but cannot waive layout/object-integrity failures or be described as within tolerance. Preserve practical residuals in one consolidated record instead of repeatedly revising usable pages.

Do not infer visual success from this table or from an SVG source count. Static validation, exported-image review and native application review are distinct evidence. A screenshot demonstrates appearance at a moment in time, not text editability. A saved PPTX establishes a file exists, not that its media, text and layout survived reopening.

After relevant checks pass, stop expanding verification unless a new change or unresolved concern justifies it. Consolidate minor acceptable differences. Never hide a material failure behind “all checks passed.”
