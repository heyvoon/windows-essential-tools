# 🤝 Contributing Guidelines

Thank you for your interest in improving **Windows Debloat & Privacy Tools**! This repository is community-maintained, and your contributions help keep it accurate, safe, and up-to-date.

---

## 🛠️ Two Ways to Contribute

You can help improve this collection without writing a single line of code:

### 📝 Option 1: Use the Issue Template (Recommended)
1. Navigate to the **Issues** tab and click **New issue**
2. Select **`📦 Tool Request (Add / Update / Remove)`**
3. Fill out the structured form with tool details, compatibility, and verification notes
4. Submit. Maintainers will verify, format, and merge a PR on your behalf!

### 💻 Option 2: Open a Pull Request
If you prefer to submit changes directly:
1. **Fork** this repository to your GitHub account
2. **Create a branch**: `git checkout -b feat/add-tool-name` or `fix/broken-link`
3. **Make your changes** following the guidelines below
4. **Commit & Push** with clear, descriptive messages
5. **Open a Pull Request** targeting the `main` branch

> 🛠️ **For maintainers:** See [MAINTAINERS.md](MAINTAINERS.md) for workflow instructions and review criteria.

---

## 📁 Where to Place Entries
| File | Purpose |
|------|---------|
| `tools/active-github.md` | Actively maintained open-source repos |
| `tools/active-websites.md` | Official sites, portable EXEs, web tools |
| `tools/archived.md` | Deprecated, unmaintained, or unsafe tools |
| `tools/guides-articles.md` | Tutorials, videos, comparisons, research |
| `categories/*.md` | Function-based cross-references |

## 📝 Required Template
Every tool entry **must** follow this exact format:
```markdown
### [Tool Name](URL)
- **Type:** `GUI` / `CLI` / `PowerShell` / `Portable EXE` / `Web Generator`
- **OS:** `Win10` / `Win11` / `Both`
- **Last Verified:** `YYYY-MM-DD`
- **Description:** One-line summary of primary function
- **Launch/Install:** Command, direct link, or `Download & run`
- **Notes:** Compatibility quirks, dependencies, or warnings
```

### ➕ Cross-Referencing
If a tool serves multiple purposes, duplicate the entry in relevant `categories/` files. Keep all fields identical across files.

---

## ✅ Verification Checklist
Before submitting via PR or Issue, verify each tool:

- [ ] **Tested in a VM** or isolated environment (Windows 10 22H2+ / 11 23H2+)
- [ ] **Source is transparent**: Open-source repo or reputable vendor
- [ ] **No obfuscated/packed code**: Scripts must be readable
- [ ] **Active or stable**: Commits within ~6 months, OR proven portable/stable
- [ ] **Safe defaults**: Does not permanently break Windows Update, Store, or Defender
- [ ] **HTTPS only**: No HTTP or expired SSL domains
- [ ] **Alphabetized**: Entry placed in correct A→Z position in the file

🚫 **We reject**:
- Tools requiring permanent AV/Defender disablement
- Closed binaries with no public build/audit instructions
- Pre-2019 scripts targeting obsolete Windows builds (< 1903)
- Duplicate entries without meaningful differentiation

---

## 📥 Pull Request Guidelines

- **Title**: `[Add/Update/Remove] Tool Name` or `fix: broken link in active-github.md`
- **Description**: Briefly explain what you changed and why. Reference the issue number if you used the template.
- **Verification Note**: Include a line like `Tested on Win11 24H2 VM, safe defaults confirmed.`
- **One logical change per PR**: Group related updates if necessary, but keep PRs focused.
- **Automated Checks**: Ensure the link-checker workflow passes before requesting review.

PRs that don't meet these standards will be politely closed or requested for revision.

---

## 🐛 Reporting Issues

Use GitHub Issues for:
- 🔗 Broken or redirecting links
- ⚠️ Tools causing system instability or breaking features
- 📅 Outdated compatibility information
- 💡 Suggestions for new tools or categories

When reporting:
- Include your Windows version/build
- Provide screenshots or error logs if applicable
- Reference the exact file/line if possible

---

## 🤝 Community Guidelines

- Be respectful and constructive in all discussions.
- Assume good intent; debloat preferences vary by use case.
- Do not spam or self-promote without community value.
- Security & stability > aggressive customization.
- Follow the [CODEOWNERS](CODEOWNERS) review process for approvals.

---

## 📜 License & Attribution

By contributing, you agree that your submissions will be licensed under the repository's [MIT License](LICENSE).  
Original tool authors retain their respective licenses; this repo only links to or describes them.

---

> 💡 **Need help?** Open a `Discussion` or tag the maintainers in an issue. We're happy to guide you through your first contribution!

*Last updated: April 2026*