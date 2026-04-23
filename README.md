# 🪟 Windows Debloat Tools Repository - Setup Guide

Great idea! Let me help you create a well-organized, maintainable GitHub repository for Windows debloat tools. Here's everything you need:

---

## 📁 Recommended Repository Structure

```
windows-debloat-tools/
├── README.md                 # Main documentation (see template below)
├── CONTRIBUTING.md          # Guidelines for adding new tools
├── tools/
│   ├── active-github.md     # Actively maintained GitHub repos
│   ├── active-websites.md   # Official websites/portable tools
│   ├── archived.md          # Historical/less maintained tools
│   └── guides-articles.md   # Tutorials and reference articles
├── categories/
│   ├── telemetry-blockers.md
│   ├── bloatware-removers.md
│   ├── privacy-tweakers.md
│   └── ai-feature-removers.md
├── scripts/
│   └── validate-links.ps1   # Optional: script to check URL validity
└── .github/
    └── ISSUE_TEMPLATE/
        └── add-tool.md      # Template for community submissions
```

---

## 📝 README.md Template

```markdown
# 🪟 Windows Debloat & Privacy Tools Collection

> A curated, community-maintained list of tools, scripts, and resources for removing bloatware, disabling telemetry, and enhancing privacy on Windows 10/11.

⚠️ **Disclaimer**: Use these tools at your own risk. Always create a system restore point before making system changes.

🔄 **Last Updated**: $(date) | 📊 **Tools Listed**: XX | ✅ **Verified Active**: XX

---

## 🚀 Quick Start

### Most Popular & Actively Maintained (2026)

| Tool | Type | Win10 | Win11 | Notes |
|------|------|-------|-------|-------|
| [Chris Titus Tech WinUtil](https://github.com/ChrisTitusTech/winutil) | PowerShell GUI | ✅ | ✅ | Most popular (52k+ ⭐), actively maintained [[12]] |
| [Win11Debloat](https://github.com/Raphire/Win11Debloat) | PowerShell Script | ✅ | ✅ | Lightweight, 45k+ ⭐, recent 2026.04 release |
| [SophiApp](https://github.com/Sophia-Community/SophiApp) | C# GUI App | ⚠️ | ✅ | Modern UI, 130+ tweaks, Win10 support being phased out |
| [O&O ShutUp10++](https://www.oo-software.com/en/shutup10) | Portable EXE | ✅ | ✅ | Free antispy tool, no install required [[23]] |
| [W10Privacy](https://www.w10privacy.de/english-home/) | Portable EXE | ✅ | ✅ | Granular privacy controls |

### One-Line Launch Commands

```powershell
# Chris Titus WinUtil (Recommended for most users)
irm "https://christitus.com/win" | iex

# Win11Debloat
& ([scriptblock]::Create((irm "https://debloat.raphi.re/")))

# SophiApp
irm app.sophi.app -useb | iex
```

---

## 📚 Tools by Category

### 🔧 All-in-One Debloat Suites
- [ChrisTitusTech/winutil](https://github.com/ChrisTitusTech/winutil) - Install apps, debloat, fix updates
- [Raphire/Win11Debloat](https://github.com/Raphire/Win11Debloat) - Lightweight PowerShell script
- [Sophia-Community/SophiApp](https://github.com/Sophia-Community/SophiApp) - Modern GUI tweaker
- [memstechtips/UnattendedWinstall](https://github.com/memstechtips/UnattendedWinstall) - Unattended install customization

### 🔒 Privacy & Telemetry Blockers
- [O&O ShutUp10++](https://www.oo-software.com/en/shutup10) - Free antispy tool [[23]]
- [W10Privacy](https://www.w10privacy.de/english-home/) - Detailed privacy controls
- [privacy.sexy](https://privacy.sexy/) - Web-based privacy script generator
- [builtbybel/Debotnet](https://github.com/builtbybel/debotnet) - Portable privacy tool
- [W4RH4WK/Debloat-Windows-10](https://github.com/W4RH4WK/Debloat-Windows-10) - PowerShell scripts

### 🗑️ Bloatware Removers
- [Sycnex/Windows10Debloater](https://github.com/Sycnex/Windows10Debloater) - Classic debloater
- [Fs00/Win10BloatRemover](https://github.com/Fs00/Win10BloatRemover) - CLI-focused removal
- [meetrevision/playbook](https://github.com/meetrevision/playbook) - Ansible-based automation

### 🎨 UI & Experience Tweaks
- [Open-Shell](https://sourceforge.net/projects/open-shell.mirror/) - Classic Start Menu
- [builtbybel/sharpapp](https://github.com/builtbybel/sharpapp) - App management UI

### 📖 Guides & Reference Articles
- [Chris Titus: Debloat Windows 10/11 Guide](https://christitus.com/debloat-windows-10-2020/)
- [Ghacks: Windows Privacy Tools Comparison](https://www.ghacks.net/2015/08/14/comparison-of-windows-10-privacy-tools/)
- [PrivacyTools.io: Windows Privacy Guide](https://www.privacytools.io/windows) [[20]]

---

## ⚠️ Tools to Approach with Caution

| Tool | Reason | Status |
|------|--------|--------|
| `DisableWinTracking` (bitlog2) | Last update ~2017, may break modern Windows | ❌ Archived |
| `Phant0m` (hlldz) | Event log manipulation, potential stability issues | ⚠️ Advanced only |
| `Destroy-Windows-10-Spying` | Aggressive modifications, limited maintenance | ⚠️ Use carefully |
| Older Ghacks/GeckoAndFly articles | May reference outdated methods | 📚 Historical reference |

---

## 🔄 Maintenance Notes

### How We Verify Tools
1. ✅ Repository has commits within last 6 months
2. ✅ Issues are being addressed
3. ✅ Compatible with Windows 10 22H2 / Windows 11 23H2+
4. ✅ No reports of system-breaking behavior in recent issues

### Known Issues (2026)
- Windows Recall & Copilot removal requires latest tool versions [[8]]
- Some telemetry settings re-enable after major updates [[34]]
- AI features in Edge/Paint/Notepad need explicit disabling [[1]]

---

## 🤝 Contributing

1. Fork the repo
2. Add tool to appropriate category file
3. Include: Name, URL, Type, Win10/11 compatibility, brief description, last verified date
4. Submit PR with verification notes

📋 [See CONTRIBUTING.md for full guidelines](CONTRIBUTING.md)

---

## 📜 License

This collection is licensed under [MIT License](LICENSE). Individual tools retain their original licenses.

---

> 💡 **Pro Tip**: Always test debloat tools in a VM first. Keep a Windows installation USB handy for recovery.

*This list is community-maintained. Last comprehensive review: April 2026*
```

---

## 🗂️ CONTRIBUTING.md Template

```markdown
# Contributing Guidelines

## Adding a New Tool

Before submitting a tool, please verify:

### ✅ Minimum Requirements
- [ ] Tool is functional on Windows 10 22H2 or Windows 11 23H2+
- [ ] Repository has activity within last 6 months OR tool is stable/portable
- [ ] No critical unresolved issues about system instability
- [ ] Clear documentation or usage instructions exist

### 📝 Submission Format
```markdown
### [Tool Name](URL)
- **Type**: [GUI/CLI/Script/Portable EXE]
- **Windows**: [10/11/Both]
- **Last Verified**: YYYY-MM-DD
- **Description**: One-sentence summary
- **Launch Command** (if applicable): `command here`
- **Notes**: Any caveats, dependencies, or warnings
```

### 🔍 Verification Steps
1. Test in a VM or non-critical system
2. Check GitHub issues for recent breakage reports
3. Verify download links are secure (HTTPS, official domains)
4. Confirm license allows redistribution/linking

### 🚫 What We Don't Accept
- Tools that require disabling antivirus permanently
- Scripts with obfuscated code
- Tools that haven't been updated since Windows 10 1909 or earlier (unless portable/stable)
- Duplicate entries without significant differentiation

## Updating Existing Entries
- If a tool is abandoned/archived, move to `archived.md`
- If compatibility changes, update the status badge
- If a better alternative emerges, add a "See also" note

## Reporting Issues
Use GitHub Issues to report:
- Broken links
- Tools causing system issues
- Outdated compatibility information
- Suggestions for new categories

Thank you for helping keep this resource reliable! 🙏
```

---

## 🛠️ Optional: Link Validation Script (`scripts/validate-links.ps1`)

```powershell
# Simple script to check if URLs are still reachable
$toolsFile = "README.md"
$urls = Get-Content $toolsFile | Select-String -Pattern 'https?://[^\s\)]+' | ForEach-Object { $_.Matches.Value }

foreach ($url in $urls) {
    try {
        $response = Invoke-WebRequest -Uri $url -Method Head -TimeoutSec 5 -ErrorAction Stop
        Write-Host "✅ $url" -ForegroundColor Green
    }
    catch {
        Write-Host "❌ $url - $($_.Exception.Message)" -ForegroundColor Red
    }
}
```

---

## 🔄 Maintenance Workflow Suggestions

1. **Monthly**: Run the validation script, update "Last Verified" dates
2. **Quarterly**: Review GitHub repos for activity, move inactive tools to `archived.md`
3. **After Windows Updates**: Test top 5 tools against new builds, update compatibility notes
4. **Community**: Enable GitHub Discussions for users to report issues with specific tools

---

## 🎯 Next Steps for You

1. Create the repo: `gh repo create windows-debloat-tools --public --confirm`
2. Copy the templates above into the appropriate files
3. Add your curated list to the categorized markdown files
4. Add a `CODEOWNERS` file if you want to manage contributions
5. Consider adding GitHub Actions for:
   - Link checking weekly
   - Auto-updating "last verified" timestamps
   - PR validation for new submissions

Would you like me to help you:
1. Generate the categorized markdown files with your full deduplicated list?
2. Create a GitHub Actions workflow for automated link checking?
3. Draft a short "getting started" guide for end-users?
