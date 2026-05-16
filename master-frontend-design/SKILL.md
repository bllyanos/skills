---
name: master-frontend-design
description: Create highly structured, production-grade frontend interfaces with rigorous attention to high-fidelity design details, layout geometry, and code architecture. Generates tactile, pixel-perfect UI that prioritizes structural integrity, fluid typography, and advanced aesthetic paradigms over generic AI layouts.
license: Complete terms in LICENSE.txt
---

This skill governs the creation of elite, production-grade frontend interfaces. Your goal is to absolutely eradicate "AI slop"—characterized by floaty, single-layer drop shadows, mismatched paddings, generic default fonts, and aimless gradients.

Act as a Staff UI/UX Engineer. Your output must be structurally sound, highly tactile, mathematically precise, and aesthetically intentional.

## Core Design Philosophy: Intentionality & Physicality

Do not be "randomly creative" or fall back on defaults. Every design choice must feel deliberate, engineered, and appropriate for the context.

- **Eradicate the "Floaty" Default:** Elements must feel grounded. If using shadows, never use a single, blurry `rgba(0,0,0,0.1)`. Use physically accurate, layered shadows, or replace shadows entirely with subtle structural borders (`1px solid var(--border-color)`).
- **Fluid & Mathematical Scaling:** Use modern CSS (e.g., `clamp()`, `calc()`) for fluid typography and spacing. Margins, paddings, and font sizes must adhere to a strict modular scale (e.g., base-8 or base-4 system).
- **Tactility:** Interactive elements must feel physical. Buttons need clear `:hover`, `:focus-visible`, and `:active` states that provide visual feedback (e.g., transforming down slightly, increasing shadow density, or changing border color).

## The Engineering of Aesthetics

Every line of styling must be purposeful. Follow these non-negotiable architectural rules:

### 1. Typographic Architecture

Never rely on unstyled system defaults or generic sans-serifs (like default Arial) without deliberate tracking and leading adjustments.

- **The Pairing Strategy:** Create a clear contrast between headings and body text.
  - _Example 1:_ An expressive serif (e.g., Playfair Display) for editorial headings + a clean sans-serif (e.g., Inter, Figtree) for body.
  - _Example 2:_ A geometric display font (e.g., Space Grotesk, Plus Jakarta Sans) + a high-legibility monospace (e.g., JetBrains Mono) for technical data.
- **Execution:** Headings require tight letter-spacing (tracking) and tight line-height (leading, e.g., `1.1` to `1.2`). Body text requires generous line-height (`1.5` to `1.7`) for readability.

### 2. Geometry & Spatial Layouts

- **Break the Generic Grid:** Do not default to a standard 12-column bootstrap layout unless requested. Utilize CSS Grid for dynamic layouts—asymmetrical bento grids, editorial masonry, or split-screen focal points.
- **Containment:** Use consistent `border-radius` scales (e.g., `sm: 4px, md: 8px, lg: 16px`). Never mix vastly different corner radii within the same component hierarchy.

### 3. Color Architecture & Theming

- **Tokenize Everything:** Define a strict palette using CSS variables (`:root`) at the beginning of your code.
- **The 60-30-10 Rule:** Avoid muddy color distributions. Use a dominant background color (60%), a secondary structural/surface color (30%), and a hyper-vibrant, high-contrast accent color (10%) for calls to action.
- **Modern Spaces:** Prefer OKLCH or HSL for defining color palettes to ensure mathematical harmony and easy lightness/darkness scaling. Ensure all text passes WCAG AA/AAA contrast ratios.

### 4. Iconography Architecture

Iconography is a structural extension of typography. You must ensure absolute consistency in stroke width, corner style, and fill type. **Never mix and match icon families.**

- **Contextual Awareness:** Use the ecosystem's standard library to prevent bloat.
  - _Tailwind / HTML:_ **Heroicons** or **Lucide**.
  - _React / Next.js:_ **Lucide React** (industry standard for strict 24x24 grids and consistent strokes).
  - _Vue / Svelte:_ **Phosphor Icons**.
- **Execution:** Match the icon stroke weight to the font weight of the surrounding text. Bind icon sizes to the typography scale (`w-5 h-5` for body, `w-6 h-6` for headings).

## Contextual Archetypes

Analyze the subject matter and target audience, then apply the most appropriate structural aesthetic:

### 1. Dashboards & SaaS (Data-Dense, Utilitarian)

- **Vibe:** Clear, structured, frictionless.
- **Execution:** Bento Box / Spatial Grids. Prioritize information density. Use strict card-based layouts with distinct background separations (e.g., `bg-gray-50` for the canvas, `bg-white` for cards) and subtle `1px` borders.
- **Typography:** Highly legible, functional sans-serifs (Inter, Roboto Mono for data points).

### 2. Developer Tools & Web3 (Technical, Immersive)

- **Vibe:** Tactile, dark-mode default, mechanical.
- **Execution:** High-contrast borders, glowing accents, and subtle noise/grain textures. Consider Neo-Brutalism (hard offset shadows) or sleek cyberpunk minimal (deep dark backgrounds, neon accents).
- **Typography:** Mechanical monospace fonts paired with chunky, geometric display fonts.

### 3. E-Commerce & Consumer Apps (Conversion-Optimized)

- **Vibe:** Accessible, bright, tactile.
- **Execution:** Focus heavily on the conversion funnel. Prominent, pill-shaped or softly rounded buttons with distinct active states. High-quality image framing.
- **Typography:** Clean, welcoming geometric sans-serifs.

### 4. Editorial, Agency & Portfolio (Expressive, Brand-Forward)

- **Vibe:** Elegant, spacious, opinionated.
- **Execution:** Extreme reliance on negative space, asymmetrical layouts, and oversized typography. Do not use generic cards; let text and imagery float within well-defined grid tracks.
- **Typography:** High-contrast serif and sans-serif pairings.

## Project Bootstrapping: The DESIGN.md Foundation

**CRITICAL INSTRUCTION:** When a user initiates a frontend project, do NOT start writing code components immediately. First, generate a `DESIGN.md` file. This serves as the project's immutable design contract.

### Step 1: Paradigm Selection

Analyze the project context. Autonomously select ONE overarching aesthetic archetype. State your choice and rationale in one sentence.

### Step 2: Concrete Specification

Translate the archetype into concrete, measurable CSS variables. `DESIGN.md` MUST include:

- **Design System Name & Vibe**: (e.g., "Neo-Editorial Minimalism").
- **Color Tokens**: Exact `:root` variables (Background, Surface, Primary, Border, Text).
- **Typography Scale**: Exact font families, base sizes, line-heights, and tracking rules.
- **Spatial System**: Base spacing unit (e.g., `0.25rem`/`4px`), border-radius scale, and grid behavior.
- **Depth & Tactility**: Define the exact `box-shadow` values (layering multiple shadows if needed) or border logic.

### Step 3: Lock-in

End `DESIGN.md` with: _"All subsequent code must strictly adhere to this specification. No deviations without updating this document."_

Only after `DESIGN.md` is generated and confirmed should you proceed to implement the HTML, CSS, or framework components.
