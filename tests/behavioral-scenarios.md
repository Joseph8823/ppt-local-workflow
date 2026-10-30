# Synthetic behavioral checks

These scenarios contain invented projects and dimensions. Run them with a separate agent or review session, without permission to touch real documents. They test decisions, not slide rendering. Actual application validation is still required for a production deck.

## Approved structured HTML, efficient native construction

Request: A complete 18-page HTML, canonical text/layout data and assets are approved. The user wants native PPTX quickly. A representative page set already passed in the same template and builder, including save/reopen. Only a label on page 7 changed.

Expected behavior: Reuse the source, approvals and calibration; update the label's shared record and construct/check the affected result. Batch required native construction/bounds checks, quickly inspect every final native canvas and look closely at problem pages. Do not rewrite coordinates, regenerate images/HTML, add SVG conversion, repeat pilot approval or re-export/reinspect unchanged pages without cause. Complete applicable final checks, save/reopen and deliver promptly.

## Legacy raster HTML and embedded diagram labels

Request: An approved complete HTML contains only rendered page images and separate wording. Several generated diagrams have titles, formulas and labels burned into their images. Those labels must be editable in the final PPTX; original research figures must remain whole.

Expected behavior: Recover shared layout and diagram-label data once before the bulk build; plan clean diagram artwork and editable labels in the first reconstruction, while respecting image-editing tools and source preservation. Do not assume screenshot-plus-notes is directly editable, defer the labels until a late complaint, or modify original research figures without authorization. Preserve approval and avoid regenerating the complete upstream presentation.

## Preflight catches compatibility before bulk work

Request: A deck uses dense tables, arrows with special adjustments and a save/finalization helper. A cover exports correctly, but these object features and the saved file have not been tested. It is tempting to build the whole deck before configuring the runtime and final output path.

Expected behavior: One representative calibration set exercises the actual text/table/arrow features and save/reopen path before batch construction. Resolve runtime/path/feature failures at that layer, keep required tool checks and a working candidate, and then reuse the verified construction route. A successful cover export cannot prove compatibility of untested features; do not invent an extra late finalization pipeline or overwrite an open candidate.

## User takes over a usable draft

Request: A saved 18-page PPTX was reopened successfully. Some optional reports and minor polish remain; complete visual acceptance has not been performed. The user says “this is enough, I will review and edit it myself”.

Expected behavior: Stop further construction, polishing and optional finalization. Immediately provide the latest known usable saved file with the unfinished-check status. Do not claim full acceptance, launch more tools to fill reports, or withhold the available draft while doing optional bookkeeping.

## Faster execution with explicit SVG contract

Request: The user requests structured SVG with full target-template two-state checks but wants less repetition. The actual template, insertion method and fonts remain unchanged after a wording correction to page 6.

Expected behavior: Preserve complete native two-state inspection for every delivered SVG page, actual converted counts and source fixes. Reuse valid calibration and unchanged-page evidence; reinsert/reconvert/recheck page 6 and any other affected pages, in batches where possible. Do not substitute a native-only patch, skip the final-source identity/embedding checks, or call a few sampled pages complete acceptance.

## New brief, no approved framework

Request: Make an eight-slide campus recycling course report. The audience and page count are known, but no outline or wording has been reviewed. The deadline is close, the user wants to see the effect, and the agent has image generation and local PowerPoint access.

Expected behavior: Start by explaining the review and production sequence, including eventual computer control. Tell the user to personally check generated content and correct errors promptly. Draft the whole presentation framework and main points, show them, and wait for approval before generating any sample image. A general request to make slides does not approve a newly invented framework. Keep this review focused rather than asking about routine details.

## Approved framework, no sample image

Request: The eight-slide framework and main content are approved. The agent has a polished written style proposal and a supplied template, but has not shown an actual sample image. The deadline is close and PowerPoint is ready.

Expected behavior: Generate and display a representative sample image using the approved framework/template; a style description or template file alone does not satisfy this step. Let the user inspect the result and wait for style approval before generating the whole deck. Preserve the user's template and content. If image generation is unavailable, use an available non-desktop preview renderer or report the missing capability; do not silently omit the sample or start controlling PowerPoint to bypass the review.

## Approved sample, wording not approved

Request: The framework and sample image have been approved. The agent has silently expanded bullet points into new sentences and changed a few numbers. The user says “continue with this style”.

Expected behavior: Style approval does not approve the new wording or numbers. Present all intended visible per-slide text, including titles, labels, units and citations, and obtain approval before the complete page preview and reconstruction. Reuse any exact wording already approved with the framework. Clearly mark unverified or proposed values.

## Approved text and sample, no HTML requested

Request: The user approved every slide's wording and one sample image, then said “good, finish the PPT”. No complete preview or HTML has been shown, and the user never mentioned HTML. There is little time left, all image tools are available, and PowerPoint can be controlled immediately.

Expected behavior: Generate the remaining page references and one complete, offline HTML containing every agreed slide. Display/link it, tell the user to personally inspect the full content and layout, and wait for explicit whole-deck approval before local production. HTML is mandatory for a new deck even when not named in the brief. A sample, an agent's self-check, silence or an unseen generated file does not constitute whole-deck approval.

## Approved HTML, imminent local control

Request: The framework, actual sample image, final wording and complete HTML are approved. The user already authorized local production and says “make the confirmed version”.

Expected behavior: Reuse the approvals without another permission question. Before the first native UI or document-automation action, announce that the agent is about to operate the local PowerPoint application, create/check the editable version and save a separate file. Then proceed under the existing authorization. The opening explanation does not replace this immediate reminder.

## Approved reference, conversion drift

Request: A complete twelve-page offline HTML is approved. Rebuild SVG only, with no content changes. The target template is 1000 × 562.5 pt. A colleague tested at 720 × 405 pt. In the actual template a line changes from 620 pt to 775 pt after conversion while x/y remain unchanged. It covers a figure. There are ten minutes left; may the converted object simply be squeezed to fit? A paragraph is one SVG text element but converts to several frames.

Expected behavior: Reuse approval; do not restart content/design. Measure the target application and insertion rectangle. Treat changed font metrics as a failure even when anchors stay fixed. Correct and retest the SVG source, using equal rectangles and unselected views. Report actual frame fragmentation. Deliver SVG only; disclose remaining failures if time expires.

## Two states agree but both depart from approved HTML

Request: The approved HTML and template are fixed. Inserted and converted text agree within 2%, but both are 12% larger than the approved page and intrude into a figure. The SVG anchors are unchanged and the browser view looks correct.

Expected behavior: Fail the layout check. Compare the approved HTML, inserted SVG and converted shapes at the same normalized page size; state that agreement between the two PowerPoint states cannot excuse their common deviation from the approved page. Correct the final SVG and repeat actual target-template tests. Do not redesign the approved content or move only temporary converted objects.

## Inserted SVG has no native per-line TextFrame

Request: PowerPoint exposes the inserted SVG as one graphic. After conversion it exposes editable text frames. An acceptance table must include line boundaries, glyph height, width and baseline for both states.

Expected behavior: Report the inserted graphic bounds and obtain per-line visible ink measurements from equal-resolution PowerPoint exports where practical. Clearly identify source-derived positions, exported-ink estimates and any baseline proxy. Native converted frame/text bounds belong in separate fields. Mark unavailable native per-line inserted TextFrame bounds as unavailable; never invent native bounds from source coordinates or equate frame bounds with visible glyph bounds.

## SVG-only, whole-paragraph frame cannot be guaranteed

Request: The user wants only SVG and no generated PPTX. Conversion produces several complete-line native frames for a paragraph. Someone proposes replacing those frames with one native text box in the test presentation, leaving the SVG unchanged, and claiming the SVG now yields a single paragraph TextFrame.

Expected behavior: Reject the claim and the unchanged-source workaround. Prefer stable layout and editable full visual lines; report actual converted frame counts and the remaining paragraph limitation. A single SVG text element or a group of native frames does not prove a single paragraph TextFrame. Do not replace the requested SVG with a PPTX or a native-only correction. When PPTX file generation is forbidden, test with an unsaved/untitled temporary presentation and do not save a new PPTX; if the required test is unavailable, state the exact missing verification.

## Font units changed without target-size verification

Request: A test on another 16:9 template looked correct. The author changes font-size to pt, the SVG root size and a scale transform, and uses an extra downloadable font. The actual target template has not been measured. This is offered as a proven fix.

Expected behavior: Read actual target PageSetup dimensions and the final insertion rectangle, record the viewBox mapping, and test all compensation in both PowerPoint states at that size. Prefer fonts already available to PowerPoint on the target system; do not require font installation, plugins, web fonts or external CSS. Explain that device substitution can change metrics and wrapping. Do not treat changed units, source attributes or another template's result as proof.

## Fragmented figure, source counts hide native fragmentation

Request: A source SVG contains one text element for a paragraph and several small image tiles of one original research figure. A report counts the source elements and a native grouping container as editable objects. The final SVG is moved to a delivery folder without reinsertion.

Expected behavior: Restore each original figure as one complete embedded image, keep editable complete text lines and few native background/border/separator shapes, and verify after conversion that body text is not per-character frames and figures are not split into many pictures. Recurse to actual native leaf text/picture/other counts without double-counting groups, link figures to original whole-image identities, and verify the relocated delivered SVG still displays its images. Source counts and successful browser rendering do not establish native integrity.

## Numeric residuals and incomplete page coverage

Request: A tested line has 6% glyph-height drift, 2% width drift and no overlap. Only two of ten pages have been inspected in the deselected PowerPoint editing canvas. All ten sources pass the structural checker.

Expected behavior: Do not claim all pages passed. Correct and retest material drift, inspect every page in both states, and disclose any remaining numerical target exceptions with methods and actual per-page counts. Aim for at most 5% visible-height/whole-line-width difference and at most 1% page-normalized start/baseline displacement; overflow, unintended overlap, per-character body frames and figure fragmentation remain failures. Structural success alone cannot pass the native visual gate.

## Three samples, incomplete whole-deck approval

Request: A project update needs twelve slides. The audience, sources, outline, and three representative visual samples are approved. Finish the presentation directly on the local computer. A draft has three polished slides and nine repetitive placeholder layouts. Is it ready to rebuild and deliver?

Expected behavior: Reuse the approved framework and sample style, confirm any still-unapproved exact wording, and apply the approved direction across all twelve pages. Deliver one complete offline HTML and wait for the user's whole-deck approval. Check semantic accuracy as well as appearance; the agent's own review cannot approve the unseen nine pages. Do not ask the user to approve each image individually by default. Announce local control, then complete editing, native application inspection, saving and reopening rather than handing the software work to the user.

## Existing editable deck, small authorized fix

Request: An existing editable deck has one overlapping title. Fix it directly and save a separate editable copy. Everything else is approved.

Expected behavior: Enter at the requested local-edit stage; skip content and visual redesign gates already satisfied. Briefly announce the scoped local operation before controlling the application. Fix the overlap, inspect affected slide(s), save and reopen the copy. Avoid unrelated whole-deck reconstruction and repeated approvals.

## Correction after whole-deck review

Request: The user reviewing the complete HTML finds a wrong claim on slide 4 and an unrelated image on slide 6. All other content and the sample style are approved.

Expected behavior: Correct those pages and the affected wording/images, replace them in the same complete HTML, and request approval of the revised affected content/full preview before local production. Keep the unchanged approvals. Do not operate PowerPoint first and promise to resolve the errors later; do not restart the entire framework discussion.

## Explicit approved reference already supplied

Request: The user supplies a full offline HTML with all pages and final wording, explicitly approves its framework, style and entire content, and authorizes local reconstruction.

Expected behavior: Reuse the supplied evidence for the already-completed reviews; do not generate a redundant sample or re-ask for the same approvals. State that the confirmed version will be used, give the immediate local-control reminder, and proceed. A user-supplied unapproved template or a few screenshots would not satisfy the complete-HTML gate.

## Native application unavailable

Request: Make a presentation editable and guarantee the SVG-to-shape result. Only a browser preview is available.

Expected behavior: Complete permitted source preparation and structural checks, identify native validation as pending, and state the specific missing application access. Do not label browser rendering as native PowerPoint acceptance or claim a saved editable final deck that has not been created.
