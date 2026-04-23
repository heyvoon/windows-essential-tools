# 📦 Tools Directory

This folder contains the curated, verified list of Windows debloat, privacy, and optimization utilities. Entries are organized by **maintenance status** and **distribution method** to ensure reliability and quick reference.

---

## 📂 File Structure

| File | Purpose | When to Use |
|------|---------|-------------|
| `active-github.md` | Open-source projects with recent commits & active maintainers | Preferred for transparency, audits, and community updates |
| `active-websites.md` | Official vendor sites, portable EXEs, and web-based generators | Trusted standalone tools with GUI/web interfaces |
| `archived.md` | Deprecated, unmaintained, or historically significant tools | Reference only. Do **not** run on modern Windows builds |
| `guides-articles.md` | Tutorials, comparisons, videos, and documentation | Learning material & step-by-step walkthroughs |

---

## 📝 Entry Template

All tools must follow this exact format for consistency, readability, and potential automated parsing:

```markdown
### [Tool Name](URL)
- **Type:** `GUI` / `CLI` / `PowerShell` / `Portable EXE` / `Web Generator`
- **OS:** `Win10` / `Win11` / `Both`
- **Last Verified:** `YYYY-MM-DD`
- **Description:** One-line summary of primary function
- **Launch/Install:** Command, direct link, or `Download & run`
- **Notes:** Compatibility quirks, dependencies, or warnings
```

---

## 🔍 Verification & Maintenance Rules

1. **Active Status**: Requires commits, releases, or issue triage within the last 6 months, OR proven stability across recent Windows builds (10 22H2+ / 11 23H2+).
2. **Archival Threshold**: Move to `archived.md` if:
   - No updates in >12 months
   - Critical unresolved issues report system instability or broken features
   - Superseded by a modern, actively maintained fork
3. **Monthly Check**: Run `scripts/validate-links.ps1`, update `Last Verified` dates, and fix broken URLs.
4. **Sorting**: Entries must be alphabetized A→Z by tool name.
5. **Cross-Referencing**: A tool may appear in multiple files if it serves different purposes, but maintain a single canonical entry here.

---

## 🤝 Adding or Updating Tools

- **New Tool**: Add to the appropriate file using the template. Include a brief verification note in your PR (e.g., "Tested on Win11 24H2 VM, safe defaults confirmed").
- **Status Change**: If a tool goes inactive, move it to `archived.md` and append `⛔ Archived: YYYY-MM-DD` to the Notes field.
- **Risk Warning**: If a tool works but carries known risks, prepend `⚠️` to the description and detail mitigations in Notes.

---

## 🚫 What Not to Include

- Obfuscated, packed, or closed-source binaries without public build instructions
- Tools requiring permanent antivirus/Defender disablement
- Pre-2019 scripts targeting Windows 10 builds < 1903 (unless historical)
- Duplicate entries without meaningful differentiation (e.g., identical forks)

> 💡 **Tip**: When in doubt, test in a VM, review recent GitHub issues/discussions, and prefer transparent PowerShell scripts over closed executables.

*Last reviewed: April 2026 • Maintained by community contributors*