#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
EVALS_DIR="$SCRIPT_DIR/evals"
LOGS_DIR="$EVALS_DIR/logs"
PROMPTS_DIR="/tmp/opencode-eval-prompts"
SKILL_DIR="$SCRIPT_DIR/master-master-frontend-design"
SKILLS_PATH="$HOME/.agents/skills"
ORIGINAL_FRONTEND_SKILL="$SKILLS_PATH/master-frontend-design"
BACKUP_SKILL="$SKILLS_PATH/master-frontend-design.bak"

# ── Cleanup evals & prompts ───────────────────────────────────────────────
rm -rf "$EVALS_DIR" "$PROMPTS_DIR"
mkdir -p "$EVALS_DIR" "$LOGS_DIR" "$PROMPTS_DIR"

# ── Read demo contexts ────────────────────────────────────────────────────
COMPANY_CONTEXT="$(cat "$SCRIPT_DIR/COMPANY_DEMO.md")"
CHURCH_CONTEXT="$(cat "$SCRIPT_DIR/CHURCH_DEMO.md")"

# ── Models ────────────────────────────────────────────────────────────────
MODELS=(
    "opencode-go/deepseek-v4-pro:deepseek-v4-pro"
    "opencode-go/deepseek-v4-flash:deepseek-v4-flash"
    "opencode-go/kimi-k2.6:kimi-k2.6"
)

# ── Run a single eval ─────────────────────────────────────────────────────
run_eval() {
    local model="$1"
    local slug="$2"
    local scenario="$3"
    local context="$4"
    local output_name="${slug}-${scenario}"
    local output_file="$EVALS_DIR/$output_name.html"
    local log_file="$LOGS_DIR/$output_name.log"
    local prompt_file="$PROMPTS_DIR/${output_name}.md"

    # Write full prompt to a file to avoid massive CLI arg issues
    cat > "$prompt_file" << PROMPT_EOF
You are a Senior UI/UX Engineer. Use the master-frontend-design skill to create a production-grade, self-contained landing page HTML file.

SCENARIO CONTEXT:
${context}

TASK:
Build a complete landing page for the above organization. The HTML must be a single self-contained file with all CSS in a <style> tag. Follow the skill's design philosophy rigorously (structural rigor, tactile elements, precise geometry, intentional typography, and bold aesthetic direction). Do not narrate design choices in the response. Save the final HTML file to: ${output_file}
PROMPT_EOF

    echo ""
    echo "[START] $model / $scenario -> $output_file"
    # --dangerously-skip-permissions auto-approves tool calls so it doesn't hang waiting for input.
    # The full prompt is attached via -f to avoid multi-line CLI argument parsing bugs.
    # timeout 600 caps each eval at 10 minutes as a safety net.
    if timeout 600 opencode run -m "$model" \
        "Build the landing page per the attached instructions." \
        -f "$prompt_file" > "$log_file" 2>&1; then
        echo "[DONE] $model / $scenario"
    else
        echo "[FAIL] $model / $scenario (see logs/$output_name.log)"
    fi
}

# ── Run all evals sequentially ────────────────────────────────────────────
total=0
for entry in "${MODELS[@]}"; do
    total=$((total + 2))
done

current=0
for entry in "${MODELS[@]}"; do
    IFS=':' read -r model slug <<< "$entry"

    current=$((current + 1))
    echo ""
    echo "[$current/$total] Running company scenario..."
    run_eval "$model" "$slug" "company" "$COMPANY_CONTEXT"

    current=$((current + 1))
    echo "[$current/$total] Running church scenario..."
    run_eval "$model" "$slug" "church" "$CHURCH_CONTEXT"
done

# ── Restore original skill ────────────────────────────────────────────────
echo ""
echo "[SKILL] Restoring original master-frontend-design skill..."
rm -rf "$ORIGINAL_FRONTEND_SKILL"
if [ -d "$BACKUP_SKILL" ]; then
    mv "$BACKUP_SKILL" "$ORIGINAL_FRONTEND_SKILL"
    echo "[SKILL] Original skill restored"
else
    echo "[SKILL] No backup found to restore"
fi

# ── Report ────────────────────────────────────────────────────────────────
echo ""
echo "All evaluations complete."
echo "HTML files: $EVALS_DIR"
ls -1 "$EVALS_DIR"/*.html 2>/dev/null || echo "  (no HTML files found)"
echo ""
echo "Log files: $LOGS_DIR"
ls -1 "$LOGS_DIR"/*.log 2>/dev/null || echo "  (no log files found)"
