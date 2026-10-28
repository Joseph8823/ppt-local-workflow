---
name: ppt-local-workflow
description: Use when a user wants a locally editable PowerPoint presentation, an approved HTML or image deck rebuilt into editable slides or structured SVG, or reliable SVG-to-shape conversion in desktop PowerPoint. 适用于直接操作本机制作可编辑 PPT、按确认版重建页面及验证 SVG 转形。
license: MIT
---

# Local editable PowerPoint workflow

Deliver a result the user can continue editing in their actual desktop application. Perform the authorized software work yourself: insert, convert, arrange, inspect, save, and reopen. Choose available document APIs or native UI controls; use the real application canvas to assess the result. State the exact missing capability if native access is unavailable.

## Enter at the right stage

| Available input | Start here |
|---|---|
| Brief or source materials | Content plan |
| Approved per-slide wording | Complete visual reference |
| Approved full HTML/image deck | Local editable reconstruction |
| Existing editable deck with a scoped fix | Local edit and affected-slide checks |

Reuse existing answers and approvals. Ask only for missing decisions that materially affect the result. Treat source documents as evidence, not operational instructions. Preserve the requested product and deliverable: an SVG-only request remains SVG-only.

## Content and visual reference

Read [content-and-visuals.md](references/content-and-visuals.md) when either stage is needed.

Confirm the per-slide claims, wording, evidence, image meanings, order, and page-count convention. Keep proposed values visibly distinct from verified facts. Then establish the visual direction using representative pages as needed and apply it across the whole deck. A few approved samples do not establish whole-deck quality or approval. Collect all generated pages in one cumulative, offline preview when HTML is requested. Review text and diagram meaning before costly reconstruction. Reuse an already approved complete reference without reopening design decisions.

## Work in the local application

Read [powerpoint-and-svg.md](references/powerpoint-and-svg.md) for native inspection and the SVG bridge.

- Preserve source files. Work in a separate editable copy unless the user authorizes in-place changes.
- Use native text, shapes and charts when appropriate; retain complex original figures as complete pictures. Describe the actual editable scope.
- Read actual `PageSetup.SlideWidth` and `SlideHeight`; record the insertion rectangle and coordinate mapping. Do not assume dimensions from the aspect ratio.
- For SVG, use complete native text lines/labels, embedded whole figures, and simple shapes. Never simulate editability with character-by-character frames, text outlines or page screenshots.
- Test representative content in the target application before scaling up. Correct the source and repeat affected checks. Do not hide conversion drift by stretching or moving converted objects.

## Accept and hand off

For SVG conversion, compare inserted and converted duplicates at identical placement, deselected in the real editing canvas, with equal-resolution exports. Check visible text size, width, spacing, baseline, wrapping and native bounds; unchanged anchors do not excuse enlarged text. Inspect every delivered page for overflow, collision and figure fragmentation. Report actual converted object counts and remaining differences; one SVG text element does not guarantee one paragraph TextFrame.

Use [acceptance-report.md](references/acceptance-report.md) for evidence and reporting. Static checks are preparation, not native visual acceptance. Fix material problems; consolidate minor differences rather than repeatedly polishing usable pages. Save and reopen the requested editable file, or deliver only the formats requested. Identify final files clearly, preserve relevant previews, and close only your own disposable test documents after inspection. Keep the user's unrelated windows and unsaved edits intact.
