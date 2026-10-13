#!/bin/bash
# Installs the Python libraries for the Google Ads and Meta APIs at the start of each cloud session.
set -euo pipefail

if [ "${CLAUDE_CODE_REMOTE:-}" != "true" ]; then
  exit 0
fi

pip install --quiet --disable-pip-version-check --break-system-packages \
  -r "$CLAUDE_PROJECT_DIR/requirements.txt" >/dev/null 2>&1 || \
  echo "session-setup: pip install failed; run 'pip install -r requirements.txt' manually" >&2
