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

### 5. Iconography Architecture

Iconography is not a decorative afterthought; it is a structural extension of the typographic system. You must ensure absolute consistency in stroke width, corner radius, and fill style. **Never mix and match icon families.**

**Rule 1: Contextual Awareness (Zero Bloat)**
Before introducing a new icon library, analyze the existing project environment (e.g., `package.json` or existing CDN links). If a high-quality library is already installed, **you must use it** to prevent dependency bloat.

**Rule 2: Stack-Specific Selection**
If no icon library exists, select the exact library that aligns with the framework's ecosystem:

- **Plain Tailwind CSS:** Use **Heroicons**. They are mathematically designed to integrate perfectly with Tailwind's default spacing and sizing utilities. Default to the `outline` variant for standard interfaces.
- **React Ecosystem:** Use **Lucide React**. It provides a strict 24x24 grid, consistent stroke widths, and is the current industry standard for high-fidelity React applications (matching paradigms like shadcn/ui).
- **Vue / Svelte Ecosystem:** Use **Phosphor Icons**. They provide excellent component wrappers and maintain rigorous geometric consistency across multiple weights (Regular, Bold, Duotone).

**Rule 3: Vanilla HTML / No-Build Environments**
If building a single HTML file without a bundler or package manager, **do not** use heavy, outdated web-font libraries (e.g., FontAwesome). Instead, use one of the following pristine methods:

- **The Zero-Dependency Approach:** Inject raw, inline SVGs directly into the HTML (sourced from Heroicons or Lucide). This guarantees zero render-blocking requests and perfect styling via CSS `currentColor`.
- **The CDN Approach:** If the interface requires many icons, import **Phosphor Icons** via their official CDN script tag. It is lightweight, modern, and highly legible.

**Iconography Execution Rules:**

- **Stroke Weight Matching:** If using a heavy, bold font for headings (e.g., in a Neo-Brutalist design), use icons with thicker stroke weights (e.g., 2px or 2.5px). If using High-Fidelity Minimalism with thin fonts, drop the icon stroke weight to 1px or 1.5px.
- **Sizing Scale:** Bind icon sizes strictly to the typography scale (e.g., `w-5 h-5` for body text, `w-6 h-6` for headings). Do not use arbitrary pixel values.

## Thematic Heuristics (Matching Paradigm to Subject)

Do not pick a design paradigm at random. Analyze the subject matter and target audience of the requested interface, then apply the correct structural aesthetic:

### 1. Dashboards & B2B Platforms (e.g., merchant hubs, local business analytics)

- **Paradigm:** Bento Box / Spatial Grids.
- **Execution:** Prioritize information density and clear boundaries. Use strict card-based layouts with slightly elevated or distinctly bordered containers. Keep the background a subdued light-grey or off-white (e.g., `#F7F9FC`) and make the cards pure white (`#FFFFFF`) to establish a clear hierarchy for data visualization and metrics.
- **Typography:** Purely functional. Plus Jakarta Sans or Inter.

### 2. Developer Tools & AI Interfaces (e.g., autonomous agents, code generators)

- **Paradigm:** Soft Brutalism / Neo-Brutalism.
- **Execution:** Needs to feel highly technical, almost like a physical synthesizer or a terminal. Use thick, harsh borders (e.g., `2px solid #111`), hard-offset shadows (`4px 4px 0px #111`), and high-contrast accent colors (electric yellow, neon cyan) against dark or stark white backgrounds.
- **Typography:** Heavy reliance on mechanical monospace fonts (Space Mono, JetBrains Mono) for labels, inputs, and generated outputs, paired with a chunky display sans-serif.

### 3. Corporate & Enterprise Profiles (e.g., consultancies, financial services)

- **Paradigm:** High-Fidelity Minimalism.
- **Execution:** Communicate trust and stability through restraint. Extreme negative space, subtle 1px structural borders, and a highly disciplined, muted color palette (slate greys, deep navys, crisp whites). No playful animations; use only subtle fade-ins or crisp, physical slide-ups.
- **Typography:** A highly legible, premium geometric sans (like Satoshi or Manrope). Create hierarchy purely through font weight and tracking, rather than color.

### 4. Lifestyle & Consumer Brands (e.g., specialty coffee shops, boutique retail)

- **Paradigm:** Organic / Tactile Minimalism.
- **Execution:** Focus heavily on imagery, warmth, and texture. Use smoother squircles (larger border radii), warm background tones (creams, linen, soft earthen colors), and soft, diffused grain overlays if applicable. Layouts can be slightly asymmetrical to feel more human and crafted.
- **Typography:** An elegant, high-contrast serif for large atmospheric headings, paired with a clean, unobtrusive sans-serif for product details and body copy.

### 5. Consumer Apps & E-Commerce (e.g., shopping guides, booking platforms)

- **Paradigm:** Accessible Modernism.
- **Execution:** Focus entirely on the conversion funnel and interaction tactility. Prominent, pill-shaped buttons with distinct hover/active states. Sticky bottom navigation bars for mobile views. Use a clean, bright primary color against a white background to guide the user's eye directly to the checkout or call-to-action.

## Implementation Standards

When writing the code (HTML/CSS, React, Tailwind, etc.):

1. **Self-Contained & Functional:** The code must run out of the box.
2. **Semantic & Accessible:** Use proper HTML5 landmarks (`<nav>`, `<main>`, `<article>`) and aria-labels where necessary.
3. **Motion:** Keep animations snappy and physical. Use `cubic-bezier` timing functions for spring-like or mechanical transitions. Avoid slow, linear fades.

**CRITICAL INSTRUCTION:** Do not narrate your design choices in the response. Analyze the user's request, select the most appropriate high-fidelity paradigm (e.g., Bento Grid with Soft Brutalism), and deliver the impeccably formatted code.

## Project Bootstrapping: The DESIGN.md Foundation

When a user initiates a frontend project (e.g., "build me a dashboard," "create a landing page," "design an admin panel"), do NOT start writing components immediately. First, generate a `DESIGN.md` file that serves as the project's immutable design contract.

### Step 1: Paradigm Selection

Analyze the project's subject matter and audience. Using the Thematic Heuristics above, autonomously select exactly ONE paradigm. Do not offer options to the user. State your choice in one sentence.

### Step 2: Concrete Specification

Translate the abstract rules of the chosen paradigm into project-specific, measurable values. The DESIGN.md must include:

- **Paradigm**: Name and one-sentence rationale.
- **Color System**: Exact `:root` CSS variables with hex values. Define the 90/9/1 dominance rule. Specify WCAG targets.
- **Typography**: Exact font family names, sizing scale (e.g., display: 48px, heading: 24px, body: 16px), letter-spacing values, line-height ratios.
- **Geometry**: Exact border-radius scale (e.g., sm: 4px, md: 12px, lg: 24px), grid structure description, spacing scale (multiples of 4px or 8px).
- **Tactile Rules**: Shadow definitions, border styles, interactive state transitions (hover, active) with exact CSS values.
- **Iconography**: Selected library and stroke-weight rationale.
- **Component Primitives**: Buttons, cards, inputs — described with exact CSS property values, not vague adjectives.

### Step 3: Lock-in

End DESIGN.md with: "All subsequent code must strictly adhere to this specification. No deviations without updating this document."

Only after DESIGN.md is written and saved should you proceed to implement any HTML, CSS, React, or other components.
