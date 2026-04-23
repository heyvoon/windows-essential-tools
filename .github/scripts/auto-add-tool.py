#!/usr/bin/env python3
"""
Auto-add tool submission from GitHub issue to markdown files.
Security: Never auto-merge. Always create PR for review.
"""
import os
import re
import sys
import json
import urllib.parse
from pathlib import Path

# === CONFIG ===
REPO_ROOT = Path(os.environ.get('GITHUB_WORKSPACE', '.'))
TOOLS_DIR = REPO_ROOT / 'tools'
CATEGORIES_DIR = REPO_ROOT / 'categories'
ENTRY_TEMPLATE = """### [{name}]({url})
- **Type:** `{type}`
- **OS:** `{os}`
- **Last Verified:** `{verified}`
- **Description:** {description}
- **Launch/Install:** {launch}
- **Notes:** {notes}
"""

def parse_issue_body(body: str) -> dict:
    """Extract form fields from GitHub issue body (YAML-like format)."""
    fields = {}
    # Simple parser for GitHub form output (key: value lines)
    for line in body.split('\n'):
        if ':' in line and not line.strip().startswith('#'):
            key, _, value = line.partition(':')
            key = key.strip().lower().replace(' ', '_')
            value = value.strip().strip('"').strip("'")
            if value and key not in ['details_and_justification', 'verification_evidence_optional']:
                fields[key] = value
    return fields

def validate_entry(data: dict) -> list[str]:
    """Return list of validation errors (empty = valid)."""
    errors = []
    required = ['tool_name', 'tool_url', 'tool_type', 'os_compatibility', 'reasoning']
    for field in required:
        if not data.get(field):
            errors.append(f"Missing required field: {field}")
    
    # Basic URL validation
    url = data.get('tool_url', '')
    if url and not url.startswith(('https://', 'http://')):
        errors.append("URL must start with https://")
    
    # Block obvious malicious patterns
    if any(bad in url.lower() for bad in ['javascript:', 'data:', 'vbscript:']):
        errors.append("URL contains unsafe protocol")
    
    return errors

def find_insert_position(lines: list[str], tool_name: str) -> int:
    """Find alphabetical insert position for new entry."""
    for i, line in enumerate(lines):
        if line.strip().startswith('### ['):
            existing = re.search(r'### \[(.*?)\]', line)
            if existing and existing.group(1).lower() > tool_name.lower():
                return i
    return len(lines)  # Append at end

def format_entry(data: dict) -> str:
    """Format tool entry using standard template."""
    # Map form values to template fields
    os_val = 'Both'
    if 'windows_10' in data.get('os_compatibility', '').lower():
        os_val = 'Win10' if 'windows_11' not in data.get('os_compatibility', '').lower() else 'Both'
    elif 'windows_11' in data.get('os_compatibility', '').lower():
        os_val = 'Win11'
    
    launch = data.get('launch_command', 'Download & run').strip() or 'Download & run'
    notes = data.get('notes_warnings', 'None').strip() or 'None'
    
    return ENTRY_TEMPLATE.format(
        name=data['tool_name'].strip(),
        url=data['tool_url'].strip(),
        type=data['tool_type'].strip(),
        os=os_val,
        verified=os.environ.get('TODAY_DATE', 'YYYY-MM-DD'),
        description=data.get('reasoning', 'No description provided').strip(),
        launch=launch,
        notes=notes
    )

def update_file(filepath: Path, entry: str, tool_name: str):
    """Insert entry alphabetically into markdown file."""
    if not filepath.exists():
        return
    content = filepath.read_text()
    lines = content.split('\n')
    
    # Find section to update (skip frontmatter if any)
    insert_idx = find_insert_position(lines, tool_name)
    lines.insert(insert_idx, entry)
    lines.insert(insert_idx + 1, '')  # Blank line after entry
    
    filepath.write_text('\n'.join(lines))

def determine_target_files(data: dict) -> list[Path]:
    """Determine which files to update based on tool type/category."""
    targets = []
    tool_type = data.get('tool_type', '').lower()
    url = data.get('tool_url', '').lower()
    
    # GitHub repos → active-github.md
    if 'github.com' in url:
        targets.append(TOOLS_DIR / 'active-github.md')
    # Vendor sites/portable → active-websites.md  
    elif any(x in url for x in ['.com/', '.org/', '.de/', 'download', 'portable']):
        targets.append(TOOLS_DIR / 'active-websites.md')
    
    # Category mapping (simplified)
    keywords = {
        'telemetry': [CATEGORIES_DIR / 'telemetry-blockers.md'],
        'bloat': [CATEGORIES_DIR / 'bloatware-removers.md'],
        'privacy': [CATEGORIES_DIR / 'privacy-tweakers.md'],
        'copilot': [CATEGORIES_DIR / 'ai-feature-removers.md'],
        'recall': [CATEGORIES_DIR / 'ai-feature-removers.md'],
    }
    reasoning = data.get('reasoning', '').lower()
    for keyword, files in keywords.items():
        if keyword in reasoning:
            targets.extend(files)
    
    # Default fallback
    if not targets:
        targets.append(TOOLS_DIR / 'active-github.md' if 'github' in url else TOOLS_DIR / 'active-websites.md')
    
    return [t for t in targets if t.exists()]

def main():
    # Get issue data from GitHub context
    issue_body = os.environ.get('ISSUE_BODY', '')
    issue_number = os.environ.get('ISSUE_NUMBER', 'unknown')
    
    if not issue_body:
        print("❌ No issue body found")
        sys.exit(1)
    
    # Parse and validate
    data = parse_issue_body(issue_body)
    errors = validate_entry(data)
    if errors:
        print(f"❌ Validation failed: {errors}")
        # Comment on issue with errors (would use GitHub API)
        sys.exit(1)
    
    # Format entry
    entry = format_entry(data)
    tool_name = data['tool_name'].strip()
    
    # Update files
    targets = determine_target_files(data)
    for filepath in targets:
        print(f"✏️  Updating {filepath.relative_to(REPO_ROOT)}")
        update_file(filepath, entry, tool_name)
    
    print(f"✅ Prepared changes for tool: {tool_name}")
    print(f"🔗 Issue: #{issue_number}")

if __name__ == '__main__':
    main()