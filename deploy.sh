#!/usr/bin/env bash
# Push + manuellen Render-Deploy anstoßen (öffentliches Repo ohne GitHub-App → kein Auto-Deploy).
set -e
git push
echo "Pushed. Render-Deploy wird über die Render-API/MCP ausgelöst."
