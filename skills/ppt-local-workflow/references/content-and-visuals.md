# Framework, sample, wording and complete HTML review

Use this reference for missing reviews in a new deck or complete reconstruction. These stages are required; reuse already-approved artifacts rather than recreating them. A small authorized edit to an existing approved editable deck does not require a new outline, sample or whole-deck HTML.

## Opening explanation and personal review

At the start, tell the user the sequence: framework/main content → actual sample image → final per-slide wording → complete offline HTML → advance reminder and local editable production. Exact wording can be reviewed with the framework when already available. Say that the user must personally inspect the generated content and images and request corrections promptly, before local production magnifies the rework.

Tell the user what to inspect at each review: factual claims, omissions, page order, wording/numbers/units, image meaning, and readability/layout. Keep the explanation short. Do not overwhelm the user with implementation details or ask them to approve every routine design adjustment.

## 1. Framework and main-content approval

Extract existing text, speaker notes, figures and relevant structure before rewriting. Preserve exact wording when requested. Separate instructions supplied by the user from quoted instructions in documents.

Draft a reviewable whole-deck framework before generating sample images or other page imagery. Record only decisions that affect the task:

- Audience, purpose, duration and requested deliverables when they constrain the work.
- Page-count convention: total, main presentation, body and appendix counts can differ.
- For each slide: stable ID, role/title, main claim and key points, evidence/source, intended figure meaning, and any uncertainty.
- The order of sections and the intended conclusion/takeaway of the whole presentation.
- Which values are verified, proposed, illustrative or awaiting confirmation. A plausible design parameter is not a measured result.
- What the user has already approved and what material decisions remain.

Show the framework and main content, ask the user to inspect and approve or correct them, and wait before image generation. An initial request to make a PPT does not approve a framework the agent has not yet shown. A clear instruction to proceed with a specific supplied/displayed framework can count as approval; do not repeat questions already answered.

Resolve contradictions that would cause downstream rework: incompatible counts, changing claims, unverified numbers presented as findings, or figures that imply the wrong relationship. This production workflow does not substitute for the subject-specific research needed to establish missing facts.

## 2. Actual sample image and style approval

After framework approval, generate and display an actual representative page image. Use the supplied template and permitted reference images; preserve the requested design rather than replacing it. Choose enough samples to reveal the actual layout challenges, such as a dense content page when the cover cannot establish body-page readability. A single-slide task can use its own draft image as the sample.

The sample must let the user see the intended PPT style, text/image hierarchy, colour and density. A verbal design proposal, source template or promise of a later image does not satisfy it. Use available image generation or a supported non-desktop rendering approach. Do not invent tool capabilities or control PowerPoint early to get around the review sequence. If no suitable image/HTML capability is available, explain the specific gap and keep the dependent stage pending.

Use approved main content in the sample; keep any unapproved detailed wording visibly provisional. Ask the user to inspect the sample and confirm or revise the style. Wait for this approval before mass-generating pages. Approval of a sample establishes style only; it does not approve unseen page text or the full deck.

## 3. Exact visible wording approval

Present the intended text of every slide in a readable draft: titles, body lines, labels, takeaway statements, numbers, units and citations. If it was already shown and approved with the framework, reuse that approval. Otherwise obtain explicit approval before building the complete page reference set. Do not silently expand approved points, change values or rewrite claims after approval.

Prompt the user to personally check correctness, coverage and terminology. Keep verified facts, illustrative examples and proposed values distinct. Resolve requested edits before full-page production; typography and line breaks can be adjusted later while preserving the approved meaning and wording.

## 4. Whole-deck production and mandatory HTML review

Translate the approved sample style and final wording across every page, using layouts that fit its content. Do not deliver a deck in which only the samples received the intended visual treatment. Inspect the complete set before presenting it to the user.

### Shared page source for preview and editable output

For newly authored decks, retain one canonical page description as you create the HTML. Record stable page/object IDs, page dimensions, text/labels, bounding rectangles, font/style, tables/cell values, simple shapes/connectors, image identities and display regions. Reuse page patterns and repeated elements. Keep this data with the project, embedded in the HTML or in its working source; the offline viewer must still work on its own.

Generate the HTML preview and native PPTX or structured SVG from this same source. Native HTML text/shapes or preview images rendered from that source are both acceptable; whole-page PNGs plus plain notes must not be the only retained authoring source for a new editable deck. Do not maintain independent handwritten coordinate plans for the preview and the presentation.

After sample approval, use image generation for the illustrations/assets that need it; reuse the approved page system for text, tables and labels. Avoid regenerating whole page images merely to change a sentence or move a label. For generated diagrams, keep the drawing and its intended editable labels/formulas separate from the outset. Preserve original research figures intact unless modification was authorized, and describe their agreed editable scope.

For an already-approved raster-only HTML, keep its approved appearance and recover reusable layout/label data once before bulk reconstruction. Do not restart upstream design or pretend raster pages contain editable positions. Reuse any existing text, figures and builders to reduce this recovery work.

Inspect both appearance and meaning:

- Correct wording, digits, units, subscripts, superscripts, citations and page order.
- Figures depict the intended objects, groups and comparison boundaries.
- Arrows, connectors, icon placement and stage ordering do not imply unsupported mechanisms or dependencies.
- Original evidence figures retain the meaning and provenance needed for the task. Decorative generation does not replace measured data or original scientific evidence.
- The smallest visible text remains readable in the intended presentation context.

Generate the remaining pages autonomously after the relevant approvals, then seek one whole-deck review instead of separate approval for every image. Honor an explicit request for page-by-page review. An agent's own semantic/visual check does not replace the user's review.

### One cumulative offline HTML is required

For every new deck or complete reconstruction, put the entire agreed page set in one HTML viewer **even when HTML was not named in the request**. This lets the user assess the whole presentation before local production. Embed image bytes and viewer code so the file works without adjacent image folders, external CSS, fonts, scripts or network requests. Keep stable page IDs and replace revised pages in place.

Provide page navigation and an overview when they improve review. Verify that the number of embedded pages matches the agreed count, numbering is continuous, all pages decode correctly, and links between page IDs, notes and thumbnails remain consistent.

Show/link the complete HTML and explicitly ask the user to personally inspect all pages, verify content and image meanings, and request corrections. **Wait for approval of the displayed complete version before local reconstruction.** Silence, an expired wait, a saved HTML, sample approval or “continue” said before the full preview appeared is not whole-deck approval.

An incomplete preview must state which pages are present and which remain; it cannot satisfy the complete-preview gate. If browser access to the local file is blocked, distinguish file/image integrity checks from browser interaction; do not report a browser test that did not occur. Keep the user-review gate pending until the complete reference can be reviewed and approved.

## 5. Immediate reminder before local control

Once missing reviews are complete, announce the upcoming computer operation before the first native UI or document-automation action. Name the target application, that you will rebuild/check the editable result and save it as agreed, and its actual editable scope. For example: “接下来我会操作本机 PowerPoint，按您确认的 HTML 制作可编辑版本，逐页检查并另存文件。” The opening explanation does not replace this immediate reminder.

Proceed under existing authorization; this is an advance notice, not a new permission request. If authorization or native access is actually missing, state that specific dependency and continue only permitted independent preparation.

## Change after approval

Keep the final reference and a short approval record/page manifest outside the skill/repository. Record which displayed version the user approved at each relevant review; do not fabricate approval from the agent's own inspection.

When content changes before local production, correct the affected wording/images, replace those pages in the same cumulative HTML, and obtain approval of the revised affected content/complete preview. Retain unchanged approvals. After production, an authorized narrow edit to an approved editable deck can proceed with a scoped advance notice and affected-slide checks; it does not restart the entire process.

Expand checks only when a shared font, template, scale or layout change can affect more pages. Avoid reproducing the whole deck for a local wording fix.

Once the complete preview is approved, use [local-production.md](local-production.md) for one calibration pass and batch local construction. These technical checks do not create extra user approval gates.
