#!/usr/bin/env python3
"""Verify the template scaffold without pretending full build-eips support is ready."""
from pathlib import Path
import tomllib

ROOT = Path(__file__).resolve().parents[1]
manifest = tomllib.loads((ROOT / ".build-eips.repo.toml").read_text())
for stage in ("production", "staging"):
    config = manifest[stage]
    assert config["repository"] == "https://github.com/ritovision/eip-template.git"
    assert config["base_url"] == "https://ritovision.github.io/eip-template/"
assert not (ROOT / "Build.toml").exists(), "Template build support remains deferred"
assert (ROOT / "docs/template.md").is_file()
placeholder = (ROOT / ".github/actions/build-eips/action.yml").read_text()
assert "exit 1" in placeholder, "Deferred build action must fail closed"
assert "eips-wg/preprocessor" not in placeholder
print("Template scaffold check passed; full build-eips integration remains deferred")
