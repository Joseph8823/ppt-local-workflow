# Native PowerPoint and the SVG bridge

This reference applies to desktop PowerPoint. Other presentation applications require their own actual-application validation. A compatible-looking export from a different application does not establish PowerPoint conversion behavior.

## Discover and operate the actual application

Before controlling the desktop application for a new deck or complete reconstruction, complete the framework, sample-image, exact-wording and complete-HTML reviews in [content-and-visuals.md](content-and-visuals.md). Immediately announce the upcoming local operation; reuse existing authorization rather than asking for it again. A scoped edit to an approved editable deck needs the scoped notice and affected-slide checks, not a repeated whole-deck design process.

Identify the user's intended application and available access before editing. Use supported document APIs/COM for reliable bulk operations and native UI controls for commands and canvas inspection as appropriate. If a COM alias opens another office suite, identify the mismatch rather than treating it as Microsoft PowerPoint. Do not change office registration or install software as an incidental repair.

On Windows, inspect the requested document through available PowerPoint controls or its document object model. Read slide dimensions and recurse through grouped shapes to obtain leaf counts. Record native text bounds separately from shape bounds. API access can automate measurement and exports; it does not replace deselected editing-canvas inspection.

Keep inspection output in the project output directory, outside this repository: it can contain private slide text and screenshots. When opening a saved document for inspection, use a distinct read-only/untitled copy if available, close only the copy you created, and avoid quitting the user's PowerPoint application. A list of instructions for the user to perform manually is not a completed local-edit task.

## Template and mapping

Read `PageSetup.SlideWidth` and `PageSetup.SlideHeight` in points. Record the actual SVG insertion rectangle `(left, top, width, height)` in points and SVG `viewBox=(vx, vy, vw, vh)`.

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
- Explicitly set `font-family`, `font-size`, `font-weight`, `fill`, `x`, `y`, and the appropriate `text-anchor`. Use fonts available on the target system. Check mixed Latin/CJK, bold weights, references and chemical/mathematical notation when relevant.
- Avoid per-character `text`/`tspan`, lists of character coordinates, text outlines and rasterized text. Use `tspan` sparingly for real within-line emphasis; test whether conversion splits or shifts it.
- Keep each original complex figure as one complete embedded `image`. Avoid linked images, slices or mosaics. Use simple native shapes for backgrounds and separators.
- Preserve logos or complex figures as bitmaps when appropriate, while describing their editability honestly. Do not call a bitmap wrapped in SVG an editable vector illustration.

Run the optional structural checker from the skill directory:

```text
python scripts/audit_svg.py ./work/svg --output ./work/svg-audit.json
```

It checks structure and embedding only. It cannot prove font availability, original-image fidelity, absence of hidden outlined text, native conversion behavior or visual acceptance.

## Actual two-state test

1. Use a separate temporary copy of the target presentation. Insert SVG using the user's intended method at the recorded rectangle.
2. Duplicate the slide. Keep one inserted SVG; convert the other using PowerPoint's actual **Convert to Shape** command. Where supported, Office exposes this command as `SVGEdit`. Discover its availability before executing it; do not assume a command succeeded without inspecting the result.
3. Keep both states at identical placement and scale. Deselect objects and inspect both editing canvases. Selection handles and active text edits can obscure the result.
4. Export both at equal resolution. Compare visible glyph height, complete line width, character spacing, start point, baseline, line spacing, wrapping, right edge, figure positions and all overflow/collisions.
5. Record native text bounds separately from glyph ink. A box can expand even when x/y stays fixed. Shape bounds include margins and are not glyph bounds. The bottom edge of rasterized glyphs is only a baseline proxy.
6. If a material difference appears, correct the SVG source, reinsert, reconvert and repeat affected checks. Do not squeeze or reposition converted objects to conceal source drift.
7. Inspect every delivered page. Record actual nested/leaf text, picture and other-object counts. Check automatic wrapping, per-character frames and split images; source element counts do not establish converted counts.

Suggested calibration targets, unless the user specifies another standard:

- Visible glyph height and complete line width: difference within 5% where practical.
- Text start and baseline: displacement within 1% of the relevant page dimension where practical.
- No out-of-page text or unintended visible text/image overlap.

These numerical targets are review criteria, not a claim that any font/template will satisfy them. Report exceptions, measurement methods and unresolved cases. Intentional text-over-image composition must match the approved reference.

## Native editability and final saving

Check the editable result in the actual app. One SVG `text` element does not guarantee one PowerPoint paragraph frame; grouping frames is not merging them. If a single native paragraph is a firm requirement, try a native text box with explicit line breaks and compare its layout; disclose limitations rather than claiming unsupported behavior.

For a requested PPTX, save an editable copy and reopen it. Check content, slide count, missing media/fonts and representative editable objects. Keep any image-backed elements clearly identified. For SVG-only requests, do not create a final PPTX as an extra deliverable; temporary native test documents may be necessary and should be identified and cleaned up after inspection.

Move/copy the final SVGs to the delivery directory and reinsert there to check embedding. Verify delivered files match the tested source versions. Font substitution or application-version changes on another computer can require a new native check.
