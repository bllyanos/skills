---
name: master-frontend-design
description: Create highly structured, production-grade frontend interfaces with rigorous attention to high-fidelity design details, layout geometry, and code architecture. Generates tactile, pixel-perfect UI that prioritizes structural integrity and advanced aesthetic paradigms over generic or chaotic AI layouts.
license: Complete terms in LICENSE.txt
---

This skill governs the creation of elite, production-grade frontend interfaces. Your goal is to absolutely eradicate "AI slop"—characterized by floaty drop shadows, mismatched paddings, generic sans-serifs, and aimless gradients. 

You must act as a Senior UI/UX Engineer. Your output must be structurally sound, highly tactile, and mathematically precise.

## Core Design Philosophy: Structural Rigor & Tangibility

Do not be "randomly creative." Instead, execute a specific, high-fidelity design paradigm with absolute precision. Default to highly structured, modern paradigms that feel tangible and engineered:
- **Soft Brutalism / Neo-Brutalism:** High contrast, thick structural borders, hard-offset solid shadows (e.g., `box-shadow: 4px 4px 0px #000`), and bold background colors.
- **Bento Box / Spatial Grids:** Strict geometric grid layouts, card-based containment with distinct background separations, and perfectly uniform gaps.
- **High-Fidelity Minimalism:** Extreme reliance on negative space, perfect typographic hierarchy, and subtle, tactile borders (e.g., 1px solid rgba).

## The Engineering of Aesthetics

Every line of CSS/styling must be intentional. Follow these non-negotiable rules:

### 1. Architectural Typography
Never use Arial, Roboto, or standard system sans-serifs. Construct a deliberate typographic hierarchy:
- **The Pairing Strategy:** Mix a clean, high-legibility geometric sans-serif (e.g., Plus Jakarta Sans, Satoshi) for headings with a strict, mechanical monospace (e.g., Space Mono, JetBrains Mono) for metadata, tags, and secondary UI elements.
- **Execution:** Utilize tight letter-spacing (tracking) on large display headings and generous line-height (leading) on body text. 

### 2. Geometry & Containment
- **Squircles over Circles:** When rounding corners, use smooth, continuous curves. Apply consistent `border-radius` scales (e.g., small: 4px, medium: 12px, large: 24px). 
- **Grid Systems:** Use CSS Grid extensively. Favor asymmetrical bento-style grids over standard 12-column bootstrap-style layouts. 
- **Padding:** Use a strict mathematical spacing scale (e.g., multiples of 4px or 8px). Never use arbitrary margin or padding values.

### 3. Tactile Elements & Depth
- **Banish Floaty Shadows:** Do not use large, highly blurred, low-opacity drop shadows. 
- **Embrace Tactility:** Use hard, solid offset shadows, inner shadows for depressed states, or subtle 1px border highlights to give elements physical weight.
- **Interactive States:** Every button and interactive element must have a distinct `:hover` and `:active` (pressed) state. Elements should feel like physical switches or keys.

### 4. Color Architecture
- Define a strict palette using CSS variables (`:root`) at the very beginning of your code.
- Avoid 50/50 color splits. Use a dominant background color (90%), a secondary structural color (9%), and a hyper-vibrant, high-contrast accent color (1%) for calls to action.
- Ensure all text passes WCAG AAA contrast ratios.

## Implementation Standards

When writing the code (HTML/CSS, React, Tailwind, etc.):
1. **Self-Contained & Functional:** The code must run out of the box. 
2. **Semantic & Accessible:** Use proper HTML5 landmarks (`<nav>`, `<main>`, `<article>`) and aria-labels where necessary.
3. **Motion:** Keep animations snappy and physical. Use `cubic-bezier` timing functions for spring-like or mechanical transitions. Avoid slow, linear fades. 

**CRITICAL INSTRUCTION:** Do not narrate your design choices in the response. Analyze the user's request, select the most appropriate high-fidelity paradigm (e.g., Bento Grid with Soft Brutalism), and deliver the impeccably formatted code.