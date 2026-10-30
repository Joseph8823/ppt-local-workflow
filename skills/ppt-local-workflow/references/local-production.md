# Efficient local editable production

Use this route for an ordinary native PPTX task after the required content/style/HTML reviews. Read [powerpoint-and-svg.md](powerpoint-and-svg.md) additionally only when SVG is requested or actually used as a bridge. Faster execution does not remove that route's two-state requirements.

## 1. Reuse the approved source once

Keep the approved HTML, page manifest, text, assets and existing layout data. Feed the same page source to preview and presentation construction; do not manually re-enter positions or rewrite approved text in another layout description. Reuse existing builder helpers and repeated page layouts instead of writing a new conversion framework for every deck.

If the approved HTML contains only page screenshots and notes, recover a reusable page description once. Include diagram labels in this first pass. This is reconstruction, not an automatic lossless format conversion; do not pretend the screenshots already contain editable geometry. Do not regenerate approved images or HTML merely to enter the workflow.

## 2. Preflight and calibrate one representative set

Give the immediate local-control notice, then verify the actual PowerPoint application, target PageSetup, fonts, required runtime and save location once. Use the supported environment/document interfaces; keep required tool checks, and configure their existing save/validation path before bulk production rather than inventing a second finalization system later.

Default to one calibration pass on one or two representative pages covering the features actually used: dense Chinese text, long lines, tables, formulas, figure labels and arrows where applicable. Include a save/reopen test using the same shape features as the final deck. A cover alone rarely tests those risks. Reuse this calibration until a changed font, template, scale, builder or new object feature invalidates it. It is an internal test, not another user approval after the complete HTML was approved.

## 3. Build the whole deck in a batch

Use native editable text, tables, arrows and simple shapes, with complete complex figures as separate pictures. Construct intended editable diagram titles, labels and formulas in the first build; do not defer them until the user notices rasterized text. Keep original research figures whole unless changes to them were authorized, and disclose the agreed editable scope.

Use the canonical layout data and reusable page patterns for all slides. Write new candidates to separate versioned paths so an open presentation does not lock the output being overwritten. Keep a known working candidate while repairing a newer version.

## 4. Inspect once, repair affected pages together

Run one batch of object/text-bound checks and one export set for the candidate; review a whole-deck overview and quickly inspect every actual PowerPoint editing canvas. Inspect identified problem pages and the calibration features in detail. Do not manually measure every unchanged text line or repeatedly export already-verified slides in an ordinary native task.

Collect issues into one repair batch. Correct their source records, update the affected pages, and repeat the affected checks. Expand only for a shared font/template/scale/builder change or a new concern; if the authoring tool requires a full rebuild, reuse the source and avoid repeating unrelated inspections or exports. Do not add a fresh pilot round after each local wording fix.

SVG tasks still require every page in both native states at the actual target size, equal-resolution comparisons, actual converted counts and the evidence specified by the SVG contract. Batch those operations and repeat only affected checks; do not call sampling complete two-state acceptance.

## 5. Save, reopen and hand off promptly

After the final repair, save the authorized editable deliverable and reopen that saved version once. Check page count, media and editable objects, and complete applicable required checks. Supply the file as soon as those checks are satisfied; list small residuals once. Preserve evidence already gathered instead of generating an additional report/export/preview set without a concrete need.

If the user says the current result is enough, wants to take over editing, or asks to stop, stop further building and polishing. Provide the latest known usable saved file and identify pending checks or limitations. Do not label an interim file fully validated, launch more finalization work or delay handing over an available file to finish optional bookkeeping.

Report progress as completed pages, a concrete remaining defect or a blocker. Do not repeatedly restate the plan or treat a tool-packaging failure as proof that PowerPoint cannot open an already-tested file. Repair compatibility, environment and delivery problems at their actual layer; retain successful evidence from other layers.
