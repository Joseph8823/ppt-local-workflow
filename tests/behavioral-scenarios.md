# Synthetic behavioral checks

These scenarios contain invented projects and dimensions. Run them with a separate agent or review session, without permission to touch real documents. They test decisions, not slide rendering. Actual application validation is still required for a production deck.

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
