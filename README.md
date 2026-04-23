# 🪟 Windows Essential Tools

> A curated, community-maintained collection of tools, scripts, and resources for optimizing, securing, and customizing Windows 10/11.

<p align="center">
  <img src="https://img.shields.io/badge/Windows-10%2F11-blue?style=flat-square&logo=windows" alt="Windows">
  <img src="https://img.shields.io/badge/Status-Active-brightgreen?style=flat-square" alt="Status">
  <img src="https://img.shields.io/badge/License-MIT-green?style=flat-square" alt="License">
</p>

---

## ⚠️ Important Disclaimer

> **Use these tools at your own risk.**  
> - Always create a **System Restore Point** before making system changes  
> - Test in a **virtual machine** first if possible  
> - Some tools may affect Windows Update, Microsoft Store, or other features  
> - This repository does **not** host any tools — only links to official sources  
> - Not affiliated with Microsoft Corporation  

---

## 🚀 Quick Start: Top Recommendations (2026)

| Tool | Type | Win10 | Win11 | Best For |
|------|------|-------|-------|----------|
| [Chris Titus WinUtil](https://github.com/ChrisTitusTech/winutil) | PowerShell GUI | ✅ | ✅ | All-in-one optimization & debloat |
| [SophiApp](https://github.com/Sophia-Community/SophiApp) | C# GUI App | ⚠️ | ✅ | Privacy hardening & UI tweaks |
| [O&O ShutUp10++](https://www.oo-software.com/en/shutup10) | Portable EXE | ✅ | ✅ | Telemetry & privacy controls |
| [W10Privacy](https://www.w10privacy.de/english-home/) | Portable EXE | ✅ | ✅ | Granular privacy settings |
| [Open-Shell](https://sourceforge.net/projects/open-shell.mirror/) | Installer EXE | ✅ | ✅ | Classic Start Menu restoration |

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

## 📚 Browse Tools by Category

### 🔧 Optimization & Debloat
- [ChrisTitusTech/winutil](https://github.com/ChrisTitusTech/winutil) – All-in-one toolkit for app management, debloating, and performance tweaks
- [Raphire/Win11Debloat](https://github.com/Raphire/Win11Debloat) – Modular PowerShell script for UI cleanup and bloat removal
- [memstechtips/UnattendedWinstall](https://github.com/memstechtips/UnattendedWinstall) – Unattended install customization for clean Windows deployments
- [meetrevision/playbook](https://github.com/meetrevision/playbook) – Ansible-based automation for enterprise deployments

### 🔒 Privacy & Telemetry
- [O&O ShutUp10++](https://www.oo-software.com/en/shutup10) – Free antispy utility with 200+ privacy toggles
- [W10Privacy](https://www.w10privacy.de/english-home/) – Detailed privacy control panel with toggle explanations
- [privacy.sexy](https://privacy.sexy/) – Web-based generator for transparent privacy scripts
- [builtbybel/Debotnet](https://github.com/builtbybel/Debotnet) – Portable privacy tool with safe defaults
- [WPD](https://wpd.app/) – Modern dashboard for privacy, firewall, and app permissions

### 🗑️ App & Bloatware Management
- [Sycnex/Windows10Debloater](https://github.com/Sycnex/Windows10Debloater) – Classic interactive debloater (legacy)
- [Fs00/Win10BloatRemover](https://github.com/Fs00/Win10BloatRemover) – CLI-focused app removal tool
- [builtbybel/SharpApp](https://github.com/builtbybel/SharpApp) – Clean UI for managing built-in Store apps

### 🎨 UI & Experience Customization
- [Open-Shell](https://sourceforge.net/projects/open-shell.mirror/) – Restore classic Start Menu and Explorer
- [Sophia-Community/SophiApp](https://github.com/Sophia-Community/SophiApp) – 130+ UI, privacy, and system tweaks
- [Blackbird](https://www.getblackbird.net/) – One-click optimizer with UI and performance presets

### 🤖 AI Feature Control
- [ChrisTitusTech/winutil](https://github.com/ChrisTitusTech/winutil) – Includes Copilot & AI feature toggles
- [SophiApp](https://github.com/Sophia-Community/SophiApp) – Granular AI/Recall/Copilot controls for Win11
- [privacy.sexy](https://privacy.sexy/) – Generate scripts to disable AI-related services

### 📖 Guides & Reference
- [Chris Titus: Windows Optimization Guide](https://christitus.com/debloat-windows-10-2020/)
- [Ghacks: Privacy Tools Comparison](https://www.ghacks.net/2015/08/14/comparison-of-windows-10-privacy-tools/)
- [PrivacyTools: Windows Privacy Guide](https://www.privacytools.io/windows)

---

## ⚠️ Tools to Approach with Caution

| Tool | Reason | Status |
|------|--------|--------|
| `DisableWinTracking` (bitlog2) | Last update ~2017, breaks modern Windows | ❌ Archived |
| `Phant0m` (hlldz) | Event log manipulation; stability risks | ⚠️ Advanced users only |
| `Destroy-Windows-10-Spying` | Aggressive modifications, limited maintenance | ⚠️ Use with caution |
| Pre-2020 scripts | May reference deprecated registry keys or methods | 📚 Historical reference only |

---

## 🔍 How We Verify Tools

Before listing or updating a tool, we check:

1. ✅ Repository has commits within the last 6 months *(or tool is stable/portable)*
2. ✅ Open issues are being addressed by maintainers
3. ✅ Compatible with Windows 10 22H2 / Windows 11 23H2+
4. ✅ No recent reports of system-breaking behavior in issues/discussions
5. ✅ Source is transparent (open-source or reputable vendor)

---

## 🔄 Known Issues (Windows 2026)

- **Windows Recall & Copilot**: Microsoft frequently re-enables AI features via updates — re-run tools post-update
- **Telemetry Persistence**: Some privacy settings reset after major feature updates
- **AI Integrations**: Edge, Paint, Notepad, and Explorer AI features need explicit disabling in newer builds
- **Store Dependencies**: Aggressive app removal may break Microsoft Store functionality — use "safe mode" options

---

## 🤝 Contributing

We welcome community contributions! There are **two ways** to help:

### 📝 Option 1: Use the Issue Template (Recommended)
1. Go to **Issues** → **New issue**
2. Select **`📦 Tool Request (Add / Update / Remove)`**
3. Fill out the form with tool details and verification notes
4. Maintainers will verify and merge on your behalf!

### 💻 Option 2: Open a Pull Request
1. Fork the repository
2. Add/update the tool in the appropriate `tools/` or `categories/` file
3. Follow the [entry template](CONTRIBUTING.md)
4. Submit a PR with verification notes

📋 [See CONTRIBUTING.md for full guidelines](CONTRIBUTING.md)

---

## 📜 License

This collection is licensed under the [MIT License](LICENSE).  
Individual tools retain their original licenses — please review each tool's terms before use.

---

## 📂 Repository Structure

```
windows-essential-tools/
├── README.md                 # You are here
├── CONTRIBUTING.md          # How to contribute
├── CODEOWNERS               # Maintainer assignments
├── tools/
│   ├── active-github.md     # Active open-source repos
│   ├── active-websites.md   # Official sites & portable tools
│   ├── archived.md          # Deprecated/historical tools
│   └── guides-articles.md   # Tutorials & references
├── categories/
│   ├── telemetry-blockers.md
│   ├── bloatware-removers.md
│   ├── privacy-tweakers.md
│   └── ai-feature-removers.md
├── scripts/
│   └── validate-links.ps1   # Local link validation
└── .github/
    ├── ISSUE_TEMPLATE/
    │   └── tool-request.yml # Contribution form
    └── workflows/
        └── link-checker.yml # Automated link validation
```

---

> 💡 **Pro Tip**: Keep a Windows installation USB handy. Test tools in a VM first. When in doubt, choose "safe mode" or conservative presets.

*Last comprehensive review: April 2026*  
*Community-maintained • Not affiliated with Microsoft*