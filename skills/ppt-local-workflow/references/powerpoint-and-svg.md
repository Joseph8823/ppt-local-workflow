# Native PowerPoint and the SVG bridge

This reference applies to desktop PowerPoint. Other presentation applications require their own actual-application validation. A compatible-looking export from a different application does not establish PowerPoint conversion behavior.

For ordinary native PPTX construction, use [local-production.md](local-production.md). This reference adds the SVG-specific contract when SVG is requested or actually used; do not run a conversion experiment for a task that has no SVG. Batch native inspection/exports and reuse calibration until changed shared settings or new failures invalidate it. All delivered SVG pages still require both native states; speed does not turn sampling into complete acceptance.

## Approved-reference and delivery contract

For structured SVG reconstruction, use the approved complete HTML and supplied PPT template as the fixed reference. Preserve wording, claims, page order, figure meaning and visual layout; do not reopen design decisions or rewrite content. Compare three views: the approved HTML, the same SVG inserted into PowerPoint, and that SVG converted to shapes. Both native states must remain close to the approved reference. Agreement between two equally enlarged native states is not acceptance.

Apply this SVG contract when SVG is the requested output or the chosen reconstruction bridge. It does not force SVG-only output on a task that explicitly requests a native editable PPTX. For an SVG-only task, do not add a final PPTX. If the user also forbids generating PPTX files, use an unsaved/untitled temporary native test presentation and do not save a new testing PPTX. If that test cannot be performed, state the missing verification rather than omitting it or changing the deliverable.

## Discover and operate the actual application

Before controlling the desktop application for a new deck or complete reconstruction, complete the framework, sample-image, exact-wording and complete-HTML reviews in [content-and-visuals.md](content-and-visuals.md). Immediately announce the upcoming local operation; reuse existing authorization rather than asking for it again. A scoped edit to an approved editable deck needs the scoped notice and affected-slide checks, not a repeated whole-deck design process.

Identify the user's intended application and available access before editing. Use supported document APIs/COM for reliable bulk operations and native UI controls for commands and canvas inspection as appropriate. If a COM alias opens another office suite, identify the mismatch rather than treating it as Microsoft PowerPoint. Do not change office registration or install software as an incidental repair.

On Windows, inspect the requested document through available PowerPoint controls or its document object model. Read slide dimensions and recurse through grouped shapes to obtain leaf counts. Record native text bounds separately from shape bounds. API access can automate measurement and exports; it does not replace deselected editing-canvas inspection.

Keep inspection output in the project output directory, outside this repository: it can contain private slide text and screenshots. When opening a saved document for inspection, use a distinct read-only/untitled copy if available, close only the copy you created, and avoid quitting the user's PowerPoint application. A list of instructions for the user to perform manually is not a completed local-edit task.

## Template and mapping

Read the target template's actual `PageSetup.SlideWidth` and `PageSetup.SlideHeight` in points, rather than inferring them from the aspect ratio, a file label or another presentation. Record the final insertion rectangle `(left, top, width, height)` in points, SVG root dimensions and `viewBox=(vx, vy, vw, vh)`. Also record the approved HTML page's coordinate size and how it is normalized to the same slide/insertion rectangle for comparison. Do not calibrate at a convenient default size and reuse that result at the real size.

For a matching aspect ratio with no letterboxing:

```text
sx = insertion_width / vw
sy = insertion_height / vh
xppt = left + (xsvg - vx) * sx
yppt = top  + (ysvg - vy) * sy
```

For example, a synthetic 1280 × 720 viewBox inserted at `(0, 0, 1000, 562.5)` pt gives `sx=sy=0.78125`. This is an example, not a calibration constant. If ratios differ, account for `preserveAspectRatio`, alignment, letterboxing or cropping explicitly, or choose matching coordinates and retest.

Do not reuse a different template's test merely because both are 16:9. Changing root dimensions, using `pt`, or adding a scale transform is a hypothesis, not a verified fix. PowerPoint's rendered SVG and converted text can interpret units or font metrics differently. Test any compensation at the actual target size and insertion rectangle and write it into the final SVG.

## Structured SVG

- One complete title, label or body visual line should normally be one editable `text` object. For stable multiline content, separate complete lines are acceptable; disclose the resulting frames.
- Explicitly set `font-family`, `font-size`, `font-weight`, `fill`, `x`, `y`, and the appropriate `text-anchor`. Prefer common fonts already available to PowerPoint on the target system. Do not require extra font installation, plugins, network fonts or external CSS. Record the font family/weight actually used and explain that font substitution on another device can change visual size, width, baseline and wrapping. Check mixed Latin/CJK, bold weights, references and chemical/mathematical notation when relevant.
- Avoid per-character `text`/`tspan`, per-character `x/y/dx/dy` coordinate lists, text-to-path outlines and rasterized text. Never wrap a full-page screenshot as an allegedly editable slide or make text into small pictures. Use `tspan` sparingly only for necessary colour/weight changes within the same visual line; test whether native conversion splits frames or shifts text.
- Keep each original research/complex figure as one complete embedded `image`, with a stable source identity in the project manifest. Avoid linked images, slices, tiles or mosaics. Verify actual conversion also preserves the figure as one whole picture; source element counts alone cannot establish this. Use few native shapes for backgrounds, borders and separators.
- Preserve logos or complex figures as bitmaps when appropriate, while describing their editability honestly. Do not call a bitmap wrapped in SVG an editable vector illustration.

Run the optional structural checker from the skill directory:

```text
python scripts/audit_svg.py ./work/svg --output ./work/svg-audit.json
```

It checks structure and embedding only. It cannot prove font availability, original-image fidelity, absence of hidden outlined text, native conversion behavior or visual acceptance.

## Actual two-state test

1. After the review gates and immediate local-control notice, use a separate temporary/untitled copy of the target presentation. Keep it unsaved when new PPTX generation is forbidden. Insert the final SVG using the user's intended insertion method at the recorded rectangle.
2. Duplicate the slide so both states use the same template/page dimensions and insertion rectangle. Keep one inserted SVG; convert the other using PowerPoint's actual **Convert to Shape** command. Where supported, Office exposes this command as `SVGEdit`. Discover its availability before executing it; inspect actual objects to confirm conversion happened.
3. Preserve both states' original placement and scale throughout the comparison. Deselect objects and inspect both actual PowerPoint editing canvases. Selection handles and active text edits can obscure the result. A slide export, browser view, SVG viewer or source inspection alone cannot replace this native check.
4. Export both at equal resolution and normalize the approved HTML page to the same coordinate space. Check **all three views**, slide by slide and line by line: visible glyph height, complete line width, character spacing, text start, baseline, line/paragraph spacing, wrapping, right boundary, text bounds, figure positions, page overflow and text/text or text/image collisions.
5. Separate source text anchors from visible glyph ink and native frame/text bounds, using the measurement rules below. A stable `x/y` does not pass a line whose enlarged font metrics make it overrun its column or figure.
6. If a material difference appears, correct the SVG source, reinsert it, reconvert and repeat affected checks at the real target size. Do not stretch, squeeze, move, retype or replace only the temporary converted objects to conceal source drift. Write verified compensation into the delivered SVG, not just the test presentation.
7. Inspect **every delivered page** in both states, even after representative calibration passes. Recurse into converted groups and record actual leaf text frames, complete pictures and other shapes without double-counting group containers. Attribute the counts to the converted SVG objects; report pre-existing template objects separately. Reject body text split into character frames and original figures split into many pictures; disclose permitted complete-line paragraph fragmentation.

### Text measurement and bounding-box evidence

Use stable page/text IDs to relate the approved wording, SVG elements and native converted objects. Report these as distinct observations:

- **Source anchors/geometry:** SVG `x/y`, font attributes and their mapped positions. These describe the source, not measured native glyph size.
- **Visible glyph ink:** measure height, complete line width, start/right edge and inter-line spacing from the equal-resolution PowerPoint exports when practical; retain editing-canvas observations. Label visual estimates as estimates. Do not report the bottom of a raster glyph as a true baseline; label it as a proxy when used.
- **Native frame/text bounds:** record converted frame bounds and actual native text bounds when supported, separately from glyph ink. Shape bounds can include margins. In the inserted state, PowerPoint may expose only one SVG graphic with no native per-line TextFrame: record the graphic bounds and mark per-line native bounds as not applicable. Source-derived positions or exported-ink boxes are not native inserted TextFrame bounds.
- **Unavailable measurements:** distinguish an absent per-line TextFrame from a native API/access failure. Describe alternative evidence or mark the relevant check pending; do not fill a missing field with invented native measurements.

If a native box expands, determine whether its anchor changed, font family/weight substituted, font metrics scaled, automatic wrapping changed or margins differ. Check the resulting visible layout regardless of cause; unchanged anchors cannot excuse expansion, wrapping or overlap.

Suggested calibration targets, unless the user specifies another standard:

- Visible glyph height and complete line width: inserted/converted difference within 5% where practical, using `100 * abs(converted - inserted) / inserted` for positive measured values and consistent measurement methods.
- Text start: horizontal/vertical displacement within 1% of actual slide width/height respectively; baseline displacement within 1% of actual slide height, where practical.
- Both native states must also match the approved HTML's visual scale, line breaks and placement after normalization. Two-state agreement cannot pass shared deviation from that reference.
- No out-of-page text, unintended text/text or text/image overlap, per-character body frames or fragmented original figures. Intentional text-over-image composition must match the approved reference.

These numerical targets are review criteria, not a claim that any font/template will satisfy them. Correct material failures and repeat affected checks. Report remaining numerical exceptions, measurement methods and uncompleted pages; do not label a target exception as within tolerance or an uninspected page as passed. Keep layout/object-integrity failures explicit rather than hiding them in an overall success statement.

For measurable comparisons with HTML, normalize its page first and use the corresponding positive HTML measurement as the denominator; keep these reference deviations separate from inserted/converted deviations. If the approved page is raster-only, identify ink/position estimates and their uncertainty. The default 5%/1% targets above describe the two native states; do not invent an additional HTML tolerance or claim a precise reference measurement that was not made. Honor any user-specified reference tolerance and otherwise preserve the approved visual scale, placement and line breaks, with visible residuals disclosed.

Close the review with a truthful status: **passed** when required checks and targets are met; **checked with documented numerical exceptions** when all required checks are complete and only disclosed numerical residuals remain; **pending** when required pages/checks are unperformed; or **failed** for layout/object-integrity failures or an unmet mandatory requirement. Small stable residuals do not call for endless polishing. They must not be called within tolerance, and no exception status can excuse overflow, unintended overlap, per-character body frames or fragmented figures.

## Native editability and final saving

Check the editable result in the actual app. One SVG `text` element does not guarantee one PowerPoint paragraph frame; grouping frames is not merging them. For multiline SVG content, prioritize stable layout and editable complete visual lines. If pure SVG cannot reliably produce one native paragraph TextFrame, explicitly report the resulting line/frame split and the unmet single-paragraph requirement; do not claim it was achieved.

For a task that requests PPTX, a native paragraph text box with explicit line breaks can be a tested alternative. It does not prove that the unchanged SVG converts that way, and is not a replacement deliverable or a source repair in an SVG-only task. Save/reopen a PPTX only when that format is authorized; check content, slide count, missing media/fonts and representative editable objects. Keep image-backed elements clearly identified. Close only temporary test documents you created after inspection, respecting any no-PPTX-generation instruction.

Copy final SVGs to the delivery directory and reinsert from there to verify that all embedded original figures still display without adjacent assets or network access. Complete native tests against the same final SVG bytes; if they change, repeat affected dual-state checks. Record delivered/tested source identities, page-to-export mappings, actual object counts and remaining limitations in [acceptance-report.md](acceptance-report.md). Font substitution or application-version changes on another computer can require a new native check.
