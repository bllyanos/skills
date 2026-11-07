---
name: github-issue-writing
description: Write, refine, audit, or break down GitHub issues, epics, sub-issues, and milestones. Use when planning work in GitHub Projects, reviewing issue quality or hierarchy, or preparing actionable feature, task, bug, and discussion issues.
---

# GitHub issue writing and audit

Help a small team communicate the problem, desired outcome, and completion criteria without unnecessary process. Follow the user's instructions and the repository's existing conventions when they differ from these defaults.

## Workflow

1. Inspect relevant repository documentation, issue templates, existing issues, milestones, and project conventions when accessible. Identify duplicates and related work.
2. Understand the problem, desired outcome, scope, and known constraints. Inspect relevant code when useful.
3. Choose the smallest useful work item: epic, feature or task, bug, or discussion. Break down work only when it makes planning or delivery clearer.
4. Use the structures below as guides, not mandatory forms. Include only useful sections. Distinguish verified facts, assumptions, open decisions, and suggestions.
5. When asked to create or update GitHub items, use the specified repository and its existing conventions. Preserve existing intent, relationships, and metadata unless the user requests a change or it is necessary to carry out the request. Do not invent labels, milestones, owners, requirements, or dependencies.
6. Ask about missing information only when it blocks the work. Otherwise, mark unresolved product decisions as open questions.

## Organization

- **Project:** Track work across a product.
- **Milestone:** Group work toward a release or delivery target, for example `MVP v0.1`.
- **Epic:** Use a parent issue for a meaningful feature or outcome. A whole roadmap is usually better represented by a milestone or project view.
- **Sub-issue:** Track a coherent piece of work contributing to a parent outcome. Roughly 1–2 days is a heuristic, not a hard limit.
- **Pull request:** Link implementation to the relevant issue using an appropriate closing keyword, such as `Closes #123`.

Keep hierarchy shallow, normally no more than three issue levels. Add native dependencies when one issue genuinely blocks another and the relationship is confirmed or already explicit. Use native sub-issues where available; otherwise, link related issues clearly without claiming a native relationship exists.

## Title convention

Use concise, specific titles that reveal the outcome or action. Prefer labels or native issue types for classification; do not require a type prefix. Follow an existing repository convention or the user's explicit preference if they use prefixes.

- **Epic:** Name the outcome or capability: `User authentication`.
- **Task or feature:** Start with a specific verb: `Implement email magic-link sign-in`.
- **Bug:** State the problem or corrective action: `Fix incorrect stock after order cancellation`.
- **Discussion:** Name the decision to make: `Decide how guest checkout handles customer details`.

Avoid vague titles such as `Fix stuff` or `Implement MVP`. Do not add `Epic:`, `Task:`, or `Discussion:` just to duplicate labels.

## Writing standards

- Explain the problem and who is affected before the proposed solution.
- State observable, verifiable acceptance criteria; scale detail to the issue.
- Separate requirements from implementation suggestions. Do not prescribe a solution without a reason.
- Make scope and exclusions explicit where they prevent ambiguity.
- Use short paragraphs and checklists; use the language requested by the user or established in the repository.
- Do not invent metrics, deadlines, root causes, product behavior, or technical decisions.

## Feature or task

Adapt as needed:

- **Context:** Problem, users, and why it matters.
- **Expected outcome:** What will be possible.
- **Acceptance criteria:** Observable outcomes and relevant edge cases.
- **Scope and notes:** Boundaries, constraints, references, or open questions when useful.

## Bug

Include the problem, reproduction steps, expected and actual behavior, relevant environment and evidence, and verifiable completion criteria. Explicitly mark unknown details; redact credentials and sensitive data. Do not invent reproduction steps or root causes.

## Epic

Describe the user or business outcome, context, scope, and outcome-based success criteria. Link sub-issues when they exist and record consequential open questions. Completing every sub-issue is not by itself proof that the outcome was achieved.

## Discussion

State the decision needed, context, relevant constraints, and questions. Define a concrete closure condition, such as recording the agreed decision and follow-up work. Avoid presenting an undecided proposal as a decision.

## Audit

When asked to audit existing work:

1. Inspect each requested item and available metadata: title, body, state, milestone, labels, parent and sub-issue links, and dependencies. Inspect the project or code only as needed for context.
2. Evaluate titles and descriptions against the standards above. Check whether the outcome, scope, acceptance or completion criteria, and open decisions are clear and proportionate to the work.
3. Evaluate whether the milestone represents a release target, whether epics group a coherent outcome, and whether sub-issues and dependencies are meaningful. Check whether milestone descriptions and assigned items reflect the intended release; do not assume an unassigned issue belongs in it.
4. Distinguish actual native relationships from plain text references and distinguish missing data from information the tools could not retrieve. Do not treat a lack of assignees, due dates, labels, or a fixed template as inherently wrong.
5. Report findings by item with evidence, impact, and concise proposed changes, prioritizing material ambiguity or planning risks. Acknowledge what is already good. Do not assume the current issue list is a complete product roadmap.
6. If asked to fix issues, preserve intent and verified details; record unresolved behavior as questions. Respect exclusions and verify the resulting changes.

## GitHub Projects

Follow existing project fields and workflows. When designing a new workflow, prefer a small set of statuses, such as Backlog, Todo, In Progress, and Done. Suggest fields, labels, milestones, and automation only when useful. Verify changes before saying they were configured.
