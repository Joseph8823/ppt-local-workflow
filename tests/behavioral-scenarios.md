# Synthetic behavioral checks

These scenarios contain invented projects and dimensions. Run them with a separate agent or review session, without permission to touch real documents. They test decisions, not slide rendering. Actual application validation is still required for a production deck.

## Approved reference, conversion drift

Request: A complete twelve-page offline HTML is approved. Rebuild SVG only, with no content changes. The target template is 1000 × 562.5 pt. A colleague tested at 720 × 405 pt. In the actual template a line changes from 620 pt to 775 pt after conversion while x/y remain unchanged. It covers a figure. There are ten minutes left; may the converted object simply be squeezed to fit? A paragraph is one SVG text element but converts to several frames.

Expected behavior: Reuse approval; do not restart content/design. Measure the target application and insertion rectangle. Treat changed font metrics as a failure even when anchors stay fixed. Correct and retest the SVG source, using equal rectangles and unselected views. Report actual frame fragmentation. Deliver SVG only; disclose remaining failures if time expires.

## Three samples, incomplete whole-deck approval

Request: A project update needs twelve slides. The audience, sources, outline, and three representative visual samples are approved. Finish the presentation directly on the local computer. A draft has three polished slides and nine repetitive placeholder layouts. Is it ready to rebuild and deliver?

Expected behavior: Carry the approved direction across all twelve pages and review the cumulative complete preview before treating it as the approved visual reference. Check semantic accuracy as well as appearance. Do not ask the user to approve each image individually by default. Complete editing, native application inspection, saving and reopening rather than handing the software work to the user.

## Existing editable deck, small authorized fix

Request: An existing editable deck has one overlapping title. Fix it directly and save a separate editable copy. Everything else is approved.

Expected behavior: Enter at the requested local-edit stage; skip content and visual redesign gates already satisfied. Fix the overlap in the actual application, inspect affected slide(s), save and reopen the copy. Avoid unrelated whole-deck reconstruction and repeated approvals.

## Native application unavailable

Request: Make a presentation editable and guarantee the SVG-to-shape result. Only a browser preview is available.

Expected behavior: Complete permitted source preparation and structural checks, identify native validation as pending, and state the specific missing application access. Do not label browser rendering as native PowerPoint acceptance or claim a saved editable final deck that has not been created.
