"""Validate public DaoRoute marketplace assets.

This checker intentionally avoids network calls and secrets. It verifies the
public repository shape that marketplace submissions depend on.
"""

from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
CANONICAL_LANDING = "https://www.daoroute.com/"
OLD_LANDING = "https://" + "daltieri86.github.io" + "/DAORoute-landing/"
EXPECTED_TOOLS = {
    "get_market_snapshot",
    "get_pool_evidence",
    "get_protocol_security_status",
    "get_optimal_allocation",
}
REQUIRED_MARKETPLACE_FILES = {
    "marketplaces/GLAMA.md",
    "marketplaces/PULSEMCP.md",
    "marketplaces/OFFICIAL_REGISTRY.md",
    "marketplaces/SMITHERY.md",
    "marketplaces/AWESOME_MCP_SERVERS.md",
    "marketplaces/MCP_MARKET_SUBMISSION.md",
    "marketplaces/README.md",
}


def _read_json(path: str) -> dict[str, Any]:
    with (ROOT / path).open() as handle:
        data = json.load(handle)
    if not isinstance(data, dict):
        raise AssertionError(f"{path} must contain a JSON object")
    return data


def _iter_public_text_files() -> list[Path]:
    files: list[Path] = []
    for pattern in ("*.md", "*.json", "*.html", "*.js", "*.css"):
        files.extend(ROOT.rglob(pattern))
    return [
        path
        for path in files
        if ".git" not in path.parts and "__pycache__" not in path.parts
    ]


def validate_json_files() -> None:
    for path in ROOT.rglob("*.json"):
        if ".git" in path.parts:
            continue
        _read_json(str(path.relative_to(ROOT)))


def validate_canonical_landing() -> None:
    for path in _iter_public_text_files():
        text = path.read_text()
        if OLD_LANDING in text:
            raise AssertionError(f"old landing URL found in {path}")

    landing_refs = [
        path
        for path in _iter_public_text_files()
        if CANONICAL_LANDING in path.read_text()
    ]
    if not landing_refs:
        raise AssertionError("canonical landing URL is not referenced")


def validate_server_example() -> None:
    data = _read_json("server.example.json")
    assert data["name"] == "io.github.daltieri86/daoroute-mcp"
    assert data["title"] == "DaoRoute"
    assert data["websiteUrl"] == CANONICAL_LANDING
    assert data["repository"]["url"] == "https://github.com/DAltieri86/DAORoute-mcp"
    assert data["repository"]["source"] == "github"
    assert data["remotes"][0]["type"] == "streamable-http"
    assert data["remotes"][0]["headers"][0]["name"] == "x-api-key"
    assert data["remotes"][0]["headers"][0]["isSecret"] is True


def validate_server_card() -> None:
    data = _read_json(".well-known/mcp/server-card.json")
    tools = data.get("tools")
    if not isinstance(tools, list):
        raise AssertionError("server-card tools must be a list")

    tool_names = {tool["name"] for tool in tools}
    if tool_names != EXPECTED_TOOLS:
        raise AssertionError(f"unexpected tool set: {sorted(tool_names)}")

    for tool in tools:
        annotations = tool.get("annotations")
        if annotations != {
            "readOnlyHint": True,
            "idempotentHint": True,
            "destructiveHint": False,
        }:
            raise AssertionError(f"bad annotations for {tool['name']}")

        props = tool.get("inputSchema", {}).get("properties", {})
        verbosity = props.get("verbosity")
        if verbosity is None:
            raise AssertionError(f"missing verbosity for {tool['name']}")
        if set(verbosity.get("enum", [])) != {"full", "compact"}:
            raise AssertionError(f"bad verbosity enum for {tool['name']}")


def validate_marketplace_files() -> None:
    missing = [path for path in REQUIRED_MARKETPLACE_FILES if not (ROOT / path).exists()]
    if missing:
        raise AssertionError(f"missing marketplace files: {missing}")

    listing_index = (ROOT / "marketplaces/README.md").read_text()
    for directory in ("Glama", "PulseMCP", "Official MCP Registry", "Smithery"):
        if directory not in listing_index:
            raise AssertionError(f"marketplaces/README.md missing {directory}")


def validate_no_obvious_secrets() -> None:
    secret_patterns = [
        re.compile(r"sk-[A-Za-z0-9_-]{20,}"),
        re.compile(r"AIza[A-Za-z0-9_-]{20,}"),
        re.compile(r"BEGIN (?:RSA |EC |OPENSSH |)PRIVATE KEY"),
    ]
    allowed_placeholder = "YOUR_PILOT_API_KEY"
    for path in _iter_public_text_files():
        text = path.read_text()
        redacted = text.replace(allowed_placeholder, "")
        for pattern in secret_patterns:
            if pattern.search(redacted):
                raise AssertionError(f"possible secret found in {path}")


def main() -> None:
    validate_json_files()
    validate_canonical_landing()
    validate_server_example()
    validate_server_card()
    validate_marketplace_files()
    validate_no_obvious_secrets()
    print("public assets ok")


if __name__ == "__main__":
    main()
