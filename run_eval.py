#!/usr/bin/env python3
"""
Run evaluation suite for the master-frontend-design skill.

Spawns an LLM for each model+scenario pair, instructing it to generate
a self-contained landing page HTML file. Output is printed to the terminal
in real-time; generated HTML files are saved to the evals/ directory.
"""

import subprocess
import sys
import shutil
from pathlib import Path
from dataclasses import dataclass


# ── Configuration ───────────────────────────────────────────────────────────


@dataclass(frozen=True)
class Model:
    id: str
    slug: str
    variant: str | None = None


MODELS = [
    Model("opencode-go/minimax-m2.7", "minimax", variant="medium"),
    # Model("opencode-go/deepseek-v4-flash", "deepseek-v4-flash", variant="medium"),
    # Model("opencode-go/deepseek-v4-pro", "deepseek-v4-pro", variant="medium"),
    # Model("opencode-go/kimi-k2.6", "kimi-k2.6"),
    # Usage with variant:
    # Model("opencode-go/some-model", "some-slug", variant="some-variant"),
]

SCENARIOS = {
    "company": "COMPANY_DEMO.md",
    "church": "CHURCH_DEMO.md",
}

SKILL_NAME = "master-frontend-design"
TIMEOUT_SECONDS = 600  # 10 minutes per eval

PROMPT_TEMPLATE = """\
You are a Senior UI/UX Engineer. Use the {skill} skill to create a production-grade, self-contained landing page HTML file.

SCENARIO CONTEXT:
{context}

TASK:
Build a complete landing page for the above organization. The HTML must be a single self-contained file with all CSS in a <style> tag. Follow the skill's design philosophy rigorously (structural rigor, tactile elements, precise geometry, intentional typography, and bold aesthetic direction). Do not narrate design choices in the response.

Use the evals folder in the current directory for all outputs:
- Save the DESIGN.md to: {design_file}
- Save the final HTML file to: {output_file}
"""

# ── Paths ───────────────────────────────────────────────────────────────────

SCRIPT_DIR = Path(__file__).resolve().parent
EVALS_DIR = SCRIPT_DIR / "evals"
PROMPTS_DIR = Path("/tmp/opencode-eval-prompts")

SKILLS_PATH = Path.home() / ".agents" / "skills"
ORIGINAL_SKILL = SKILLS_PATH / SKILL_NAME
BACKUP_SKILL = SKILLS_PATH / f"{SKILL_NAME}.bak"


# ── Helpers ─────────────────────────────────────────────────────────────────


def ensure_clean_dirs() -> None:
    """Remove old eval artifacts and recreate directories."""
    for directory in (EVALS_DIR, PROMPTS_DIR):
        if directory.exists():
            shutil.rmtree(directory)
        directory.mkdir(parents=True, exist_ok=True)


def read_context(filename: str) -> str:
    """Read a scenario context file from the script directory."""
    path = SCRIPT_DIR / filename
    if not path.exists():
        print(f"[WARN] Context file not found: {path}", file=sys.stderr)
        return ""
    return path.read_text(encoding="utf-8")


def run_single_eval(model: Model, scenario: str, context: str) -> bool:
    """Run one evaluation and return True if it succeeds."""
    run_name = f"{model.slug}-{scenario}"
    run_dir = EVALS_DIR / run_name
    run_dir.mkdir(parents=True, exist_ok=True)

    design_file = run_dir / "DESIGN.md"
    output_file = run_dir / "index.html"
    prompt_file = PROMPTS_DIR / f"{run_name}.md"

    prompt = PROMPT_TEMPLATE.format(
        skill=SKILL_NAME,
        context=context,
        design_file=design_file,
        output_file=output_file,
    )
    prompt_file.write_text(prompt, encoding="utf-8")

    print(f"\n[START] {model.id} / {scenario} -> {run_dir}")

    cmd = [
        "opencode",
        "run",
        "-m",
        model.id,
    ]
    if model.variant:
        cmd += ["--variant", model.variant]
    cmd += [
        "Build the landing page per the attached instructions.",
        "-f",
        str(prompt_file),
    ]

    try:
        result = subprocess.run(cmd, timeout=TIMEOUT_SECONDS)
    except subprocess.TimeoutExpired:
        print(f"[TIMEOUT] {model.id} / {scenario}")
        return False

    if result.returncode == 0:
        print(f"[DONE] {model.id} / {scenario}")
        return True

    print(f"[FAIL] {model.id} / {scenario}")
    return False


def restore_original_skill() -> None:
    """Restore the original skill from backup."""
    print("\n[SKILL] Restoring original skill...")
    if BACKUP_SKILL.exists():
        if ORIGINAL_SKILL.exists():
            shutil.rmtree(ORIGINAL_SKILL)
        shutil.move(str(BACKUP_SKILL), str(ORIGINAL_SKILL))
        print("[SKILL] Original skill restored")
    else:
        print("[SKILL] No backup found to restore")


def print_report() -> None:
    """Print a summary of generated artifacts."""
    print("\nAll evaluations complete.")

    run_dirs = sorted(d for d in EVALS_DIR.iterdir() if d.is_dir())
    print(f"Results directory: {EVALS_DIR}")
    if run_dirs:
        for d in run_dirs:
            files = sorted(f.name for f in d.iterdir())
            print(f"  {d.name}/")
            for f in files:
                print(f"    {f}")
    else:
        print("  (no results found)")


# ── Main ────────────────────────────────────────────────────────────────────


def main() -> int:
    ensure_clean_dirs()

    # Load scenario contexts once
    contexts = {name: read_context(file) for name, file in SCENARIOS.items()}

    total = len(MODELS) * len(SCENARIOS)
    current = 0
    results: list[tuple[str, str, bool]] = []

    for model in MODELS:
        for scenario, context in contexts.items():
            current += 1
            print(f"\n[{current}/{total}] Running {scenario} scenario...")
            success = run_single_eval(model, scenario, context)
            results.append((model.id, scenario, success))

    restore_original_skill()
    print_report()

    # Exit non-zero if any eval failed
    failures = [r for r in results if not r[2]]
    if failures:
        print(f"\n{len(failures)} evaluation(s) failed.")
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
